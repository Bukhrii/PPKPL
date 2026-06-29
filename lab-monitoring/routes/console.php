<?php

use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;
use Illuminate\Support\Facades\Schedule;

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote');

// Mendaftarkan Scheduled Task kita untuk fitur Checklist 6 jam (US 3.1)
Schedule::command('monitor:check-overdue')->hourly();

// Mendaftarkan perintah cron lama
Schedule::command(CheckOverdueMonitoring::class)->hourly();

// Mendaftarkan CRON ESKALASI BARU
// Sistem akan mengecek setiap 15 menit apakah ada tiket yang SLA-nya bocor
Schedule::command(EscalateUnresolvedIncidents::class)->everyFifteenMinutes();