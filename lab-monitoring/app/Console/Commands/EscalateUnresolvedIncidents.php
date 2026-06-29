<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Models\IncidentTicket;
use App\Models\User;
use App\Mail\IncidentEscalationMail;
use Illuminate\Support\Facades\Mail;
use Carbon\Carbon;
use Illuminate\Support\Facades\Log;

class EscalateUnresolvedIncidents extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'incident:escalate';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Mengecek dan mengeskalasi tiket insiden yang belum tertangani melewati batas waktu SLA';

    /**
     * Execute the console command.
     */
    public function handle()
    {
        // Tetapkan batas waktu SLA (Contoh: 2 jam setelah insiden dibuat)
        $slaLimit = Carbon::now()->subHours(2);

        // Cari tiket dengan status Open, melebihi waktu SLA, dan belum pernah dieskalasi
        $overdueTickets = IncidentTicket::with('storageRoom')
            ->where('status', 'Open')
            ->where('created_at', '<=', $slaLimit)
            ->where('escalation_level', 0) 
            ->get();

        if ($overdueTickets->isEmpty()) {
            $this->info('Tidak ada tiket yang memerlukan eskalasi saat ini.');
            return;
        }

        // Ambil data Manajer QA / Lab yang memiliki wewenang lebih tinggi
        // Asumsi struktur role pada tabel users menggunakan kolom 'role' atau relasi
        $qaManagers = User::where('role', 'QA_Manager')->orWhere('role', 'Lab_Manager')->pluck('email');

        if ($qaManagers->isEmpty()) {
            $this->error('Gagal menemukan alamat email Manajer QA untuk pengiriman eskalasi.');
            return;
        }

        foreach ($overdueTickets as $ticket) {
            try {
                // Kirim email notifikasi darurat
                Mail::to($qaManagers)->send(new IncidentEscalationMail($ticket));
                
                // Update status eskalasi pada tiket agar tidak terjadi spam email berulang
                $ticket->update([
                    'escalated_at' => Carbon::now(),
                    'escalation_level' => 1
                ]);

                Log::channel('daily')->info("Tiket Insiden #{$ticket->id} berhasil dieskalasi ke Manajer.");
                $this->info("Tiket ID {$ticket->id} berhasil dieskalasi.");
                
            } catch (\Exception $e) {
                Log::error("Gagal mengirim email eskalasi untuk Tiket #{$ticket->id}: " . $e->getMessage());
                $this->error("Gagal memproses tiket #{$ticket->id}.");
            }
        }
    }
}