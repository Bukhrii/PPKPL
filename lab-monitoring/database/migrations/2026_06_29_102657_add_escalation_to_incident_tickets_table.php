<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     * Fitur ini menambahkan kolom untuk melacak kapan tiket dieskalasi 
     * dan berada di level eskalasi berapa.
     */
    public function up(): void
    {
        Schema::table('incident_tickets', function (Blueprint $table) {
            $table->timestamp('escalated_at')->nullable()->after('status')
                  ->comment('Waktu ketika insiden dieskalasi ke Manajer');
            $table->integer('escalation_level')->default(0)->after('escalated_at')
                  ->comment('0: Belum eskalasi, 1: Eskalasi Pertama, 2: Eskalasi Lanjutan');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('incident_tickets', function (Blueprint $table) {
            $table->dropColumn(['escalated_at', 'escalation_level']);
        });
    }
};