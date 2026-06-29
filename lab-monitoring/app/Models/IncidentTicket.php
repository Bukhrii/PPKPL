<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class IncidentTicket extends Model
{
    use HasFactory;

    protected $fillable = [
        'storage_room_id',
        'incident_date',
        'description',
        'status',
        'reported_by',
        'escalated_at',
        'escalation_level',
    ];

    protected $casts = [
        'incident_date' => 'datetime',
        'escalated_at' => 'datetime',
    ];

    // -------------------------------------------------------------------------
    // Relasi
    // -------------------------------------------------------------------------

    public function storageRoom(): BelongsTo
    {
        return $this->belongsTo(StorageRoom::class, 'storage_room_id');
    }

    public function conditionData(): BelongsTo
    {
        return $this->belongsTo(ConditionData::class, 'condition_data_id');
    }

    // INI YANG MEMBUAT ERROR SEBELUMNYA (Karena belum ada)
    public function creator(): BelongsTo
    {
        return $this->belongsTo(User::class, 'created_by');
    }

    // INI JUGA YANG MEMBUAT ERROR SEBELUMNYA (Karena belum ada)
    public function correctiveActions(): HasMany
    {
        return $this->hasMany(CorrectiveAction::class, 'incident_ticket_id');
    }

    // -------------------------------------------------------------------------
    // Helper / Accessor
    // -------------------------------------------------------------------------

    public function getDeviationLabelAttribute(): string
    {
        return match ($this->deviation_level) {
            '1'     => 'Peringatan',
            '2'     => 'Kritis',
            default => 'Tidak Diketahui',
        };
    }

    public function getStatusLabelAttribute(): string
    {
        return match ($this->status) {
            'open'               => 'Terbuka',
            'dalam_penanganan'   => 'Diproses',
            'closed'             => 'Selesai',
            default              => 'Tidak Diketahui',
        };
    }

    public function isClosed(): bool
    {
        return in_array(strtolower($this->status), ['closed', 'tertutup']);
    }
}
