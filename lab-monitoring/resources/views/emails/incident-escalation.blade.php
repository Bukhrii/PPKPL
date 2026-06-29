<!DOCTYPE html>
<html>
<head>
    <title>Eskalasi Insiden Laboratorium</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { padding: 20px; border: 1px solid #d9534f; border-radius: 5px; }
        .header { background-color: #d9534f; color: white; padding: 10px; text-align: center; font-weight: bold; }
        .content { margin-top: 20px; }
        .footer { margin-top: 30px; font-size: 12px; color: #777; }
        .alert-box { background-color: #f2dede; border-color: #ebccd1; color: #a94442; padding: 15px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            PEMBERITAHUAN ESKALASI TINGKAT 1
        </div>
        <div class="content">
            <p>Yth. Manajer QA / Laboratorium,</p>
            
            <div class="alert-box">
                <strong>Peringatan!</strong> Tiket insiden laboratorium telah melampaui batas waktu Service Level Agreement (SLA) tanpa adanya penyelesaian atau tindakan korektif (CAPA) dari petugas lapangan.
            </div>

            <p>Berikut adalah rincian insiden yang membutuhkan perhatian segera:</p>
            <ul>
                <li><strong>ID Tiket:</strong> #{{ $ticket->id }}</li>
                <li><strong>Ruang Penyimpanan:</strong> {{ $ticket->storageRoom->name ?? 'Tidak diketahui' }}</li>
                <li><strong>Waktu Kejadian:</strong> {{ $ticket->incident_date->format('d M Y H:i:s') }}</li>
                <li><strong>Deskripsi Awal:</strong> {{ $ticket->description }}</li>
            </ul>

            <p>Segera masuk ke dalam sistem untuk meninjau status sampel terdampak dan berkoordinasi dengan petugas lapangan.</p>
            <p>
                <a href="{{ url('/incidents/' . $ticket->id) }}" style="background: #d9534f; color: #fff; padding: 10px 15px; text-decoration: none; border-radius: 3px;">Lihat Detail Insiden</a>
            </p>
        </div>
        <div class="footer">
            <p>Pesan ini dihasilkan secara otomatis oleh Sistem Monitoring & Alert Kondisi Penyimpanan Laboratorium. Mohon untuk tidak membalas email ini.</p>
        </div>
    </div>
</body>
</html>