# TodoMVC Automation Test — Python Selenium

Automation testing untuk **TodoMVC React**
URL: https://todomvc.com/examples/react/dist/

40 skenario test (20 positif + 20 negatif) menggunakan **pytest** dan **Selenium**.

---

## Prasyarat

- **Python 3.8+** ([download](https://www.python.org/downloads/))
- **Google Chrome** terpasang (Selenium 4 mengelola chromedriver otomatis)
- Koneksi internet (test mengakses URL TodoMVC)

---

## Struktur Proyek

```
todomvc_automation_test/
├── conftest.py          # Fixture driver (setup & teardown otomatis)
├── helpers.py           # Fungsi helper reusable
├── pytest.ini           # Konfigurasi pytest (pythonpath, testpaths, --headless default)
├── requirements.txt     # Dependensi Python
├── README.md
├── positif/             # 20 skenario positif (P01–P20)
└── negatif/             # 20 skenario negatif (N01–N20)
```

---

## Cara Menjalankan

> **Penting:** Semua perintah dijalankan dari folder ini (folder yang berisi `pytest.ini`).

### 1. Install dependensi

```powershell
pip install -r requirements.txt
```

### 2. Jalankan semua test (default: headless, browser tidak tampil)

```powershell
pytest
```

`pytest.ini` sudah mengatur `pythonpath`, `testpaths`, dan flag `--headless` secara default, jadi tidak perlu argumen tambahan.

### 3. Jalankan dengan browser tampil (mode headed)

Override flag `--headless` dengan `-o`:

```powershell
pytest -o addopts="-v -s"
```

### 4. Jalankan hanya skenario tertentu

```powershell
pytest positif/                                       # Hanya skenario positif
pytest negatif/                                       # Hanya skenario negatif
pytest positif/test_P01_tambah_satu_task_valid.py     # Satu file saja
pytest -k "tambah"                                    # Semua test yang nama-nya mengandung "tambah"
```

---

## Ringkasan Skenario

| Kategori        | Positif | Negatif         |
|-----------------|---------|-----------------|
| Tambah Task     | P01–P04 | N01–N04         |
| Complete/Toggle | P05–P08 | N17–N19         |
| Edit Task       | P09–P10 | N05–N07         |
| Hapus Task      | P11–P13 | N08–N10         |
| Filter          | P14–P17 | N11–N14         |
| Counter/Footer  | P18–P20 | N15–N16, N20    |

---

## Troubleshooting

- **`unrecognized arguments: --headless`** — kamu menjalankan pytest dari folder yang salah. Pastikan `cd` dulu ke folder yang berisi `pytest.ini`.
- **`no tests ran`** — pastikan struktur folder `positif/` dan `negatif/` ada di sebelah `pytest.ini`.
- **Chrome tidak terbuka / error chromedriver** — pastikan Google Chrome terpasang dan versinya tidak terlalu lama.
