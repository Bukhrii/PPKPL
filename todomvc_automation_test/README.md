# TodoMVC Automation Test — Python Selenium

Automation testing untuk **TodoMVC React**  
URL: https://todomvc.com/examples/react/dist/

---

## Struktur Proyek

```
todomvc_tests/
├── conftest.py          # Fixture driver (setup & teardown otomatis)
├── helpers.py           # Fungsi helper reusable
├── requirements.txt     # Dependensi Python
├── README.md
├── positif/             # 20 skenario positif
│   ├── test_P01_tambah_satu_task_valid.py
│   ├── test_P02_tambah_3_task_berturut.py
│   ├── ... (s/d P20)
└── negatif/             # 20 skenario negatif
    ├── test_N01_enter_tanpa_teks.py
    ├── test_N02_submit_task_hanya_spasi.py
    └── ... (s/d N20)
```

---

## Cara Menjalankan

> **Penting:** Jalankan semua perintah dari folder `todomvc_tests/` (folder yang berisi `conftest.py`).

### 1. Install dependensi
```powershell
pip install -r requirements.txt
```

### 2. Jalankan semua test — mode headless (tanpa browser tampil)
```powershell
$env:PYTHONPATH = "c:\Users\haeka\Downloads\todomvc_tests\todomvc_tests"; pytest . -v --headless
```

### 3. Jalankan semua test — mode normal (browser tampil)
```powershell
$env:PYTHONPATH = "c:\Users\haeka\Downloads\todomvc_tests\todomvc_tests"; pytest . -v
```

### 4. Jalankan hanya skenario positif
```powershell
$env:PYTHONPATH = "c:\Users\haeka\Downloads\todomvc_tests\todomvc_tests"; pytest positif/ -v --headless
```

### 5. Jalankan hanya skenario negatif
```powershell
$env:PYTHONPATH = "c:\Users\haeka\Downloads\todomvc_tests\todomvc_tests"; pytest negatif/ -v --headless
```

### 6. Jalankan satu file saja
```powershell
$env:PYTHONPATH = "c:\Users\haeka\Downloads\todomvc_tests\todomvc_tests"; pytest positif/test_P01_tambah_satu_task_valid.py -v --headless
```

---

## Ringkasan Skenario

| Kategori        | Positif | Negatif |
|-----------------|---------|---------|
| Tambah Task     | P01–P04 | N01–N04 |
| Complete/Toggle | P05–P08 | N17–N19 |
| Edit Task       | P09–P10 | N05–N07 |
| Hapus Task      | P11–P13 | N08–N10 |
| Filter          | P14–P17 | N11–N14 |
| Counter/Footer  | P18–P20 | N15–N16, N20 |
