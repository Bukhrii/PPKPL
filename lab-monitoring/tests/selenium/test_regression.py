import pytest
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# FIXTURES & SETUP
# ==========================================
BASE_URL = "http://localhost:8000"

@pytest.fixture(scope="module")
def driver():
    """Setup Selenium WebDriver (Chrome Headless)"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    # Login pre-condition untuk semua test
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "email").send_keys("qa_manager@lab.com")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    yield driver
    driver.quit()

def wait_and_click(driver, by, value):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
    element.click()

# ==========================================
# SKENARIO 1: Input Data Monitoring (TC_MON_01)
# ==========================================
def test_TC_MON_01_POS(driver):
    """Positif: Input data suhu dan kelembapan valid"""
    driver.get(f"{BASE_URL}/monitoring")
    driver.find_element(By.ID, "storage_room_id").send_keys("Ruang Vaksin")
    driver.find_element(By.ID, "temperature").send_keys("4.5")
    driver.find_element(By.ID, "humidity").send_keys("45")
    wait_and_click(driver, By.ID, "btn-submit-condition")
    
    success_toast = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_SELECTOR, ".toast-success")))
    assert "berhasil disimpan" in success_toast.text

def test_TC_MON_01_NEG(driver):
    """Negatif: Input suhu kosong"""
    driver.get(f"{BASE_URL}/monitoring")
    driver.find_element(By.ID, "temperature").clear()
    wait_and_click(driver, By.ID, "btn-submit-condition")
    
    error_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_SELECTOR, ".text-danger")))
    assert "suhu wajib diisi" in error_msg.text.lower()

# ==========================================
# SKENARIO 2: Penentuan Status Kondisi (TC_STA_02)
# ==========================================
def test_TC_STA_02_POS(driver):
    """Positif: Nilai masih dalam batas normal (Hijau)"""
    # Asumsi data baru saja diinput normal di TC_MON_01_POS
    status_badge = driver.find_element(By.ID, "status-ruang-vaksin")
    assert "Normal" in status_badge.text

def test_TC_STA_02_NEG(driver):
    """Negatif: Nilai melewati batas (Merah/Bermasalah)"""
    driver.get(f"{BASE_URL}/monitoring")
    driver.find_element(By.ID, "storage_room_id").send_keys("Ruang Vaksin")
    driver.find_element(By.ID, "temperature").send_keys("15.5") # Suhu Kritis
    driver.find_element(By.ID, "humidity").send_keys("80")
    wait_and_click(driver, By.ID, "btn-submit-condition")
    
    status_badge = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "status-ruang-vaksin")))
    assert "Bermasalah" in status_badge.text

# ==========================================
# SKENARIO 3: Notifikasi Awal (TC_NOT_03)
# ==========================================
def test_TC_NOT_03_POS(driver):
    """Positif: Notifikasi pertama muncul di UI saat kondisi bermasalah"""
    driver.get(f"{BASE_URL}/monitoring")
    alert_banner = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    assert "Deviasi terdeteksi" in alert_banner.text

def test_TC_NOT_03_NEG(driver):
    """Negatif: Data normal, tidak ada notifikasi yang muncul"""
    test_TC_MON_01_POS(driver) # Reset ke normal
    alerts = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
    assert len(alerts) == 0

# ==========================================
# SKENARIO 4: Notifikasi Lanjutan / Eskalasi (TC_ESC_04)
# TERKAIT DENGAN SCHEDULER: EscalateUnresolvedIncidents
# ==========================================
def test_TC_ESC_04_POS(driver):
    """Positif: Pengingat kedua (Eskalasi) muncul jika belum ditangani"""
    # 1. Trigger cron job eskalasi secara paksa melalui subprocess (mewakili everyFifteenMinutes)
    subprocess.run(["php", "artisan", "incident:escalate"], cwd="/path/to/laravel/project")
    
    # 2. Cek apakah tiket di-update dengan status eskalasi (misal di halaman daftar insiden)
    driver.get(f"{BASE_URL}/incidents")
    escalated_badge = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".badge-escalated"))
    )
    assert "Escalated" in escalated_badge.text

def test_TC_ESC_04_NEG(driver):
    """Negatif: Masalah sudah ditangani (Closed), pengingat kedua tidak dikirim"""
    # (Asumsi data di-set closed di backend untuk testing ini)
    subprocess.run(["php", "artisan", "incident:escalate"], cwd="/path/to/laravel/project")
    driver.get(f"{BASE_URL}/incidents")
    # Pastikan tidak ada penambahan badge eskalasi baru pada tiket closed
    closed_tickets_escalated = driver.find_elements(By.XPATH, "//tr[td[contains(text(), 'Closed')]]//span[contains(@class, 'badge-escalated')]")
    assert len(closed_tickets_escalated) == 0

# ==========================================
# SKENARIO 5: Pencatatan Insiden (TC_INC_05)
# ==========================================
def test_TC_INC_05_POS(driver):
    """Positif: Insiden otomatis dibuat saat kondisi kritis"""
    driver.get(f"{BASE_URL}/incidents")
    latest_incident_status = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr:first-child td.status")))
    assert "Open" in latest_incident_status.text

def test_TC_INC_05_NEG(driver):
    """Negatif: Data normal, tidak ada insiden baru"""
    driver.get(f"{BASE_URL}/incidents")
    row_count_before = len(driver.find_elements(By.CSS_SELECTOR, "table tbody tr"))
    test_TC_MON_01_POS(driver) # Input normal
    driver.get(f"{BASE_URL}/incidents")
    row_count_after = len(driver.find_elements(By.CSS_SELECTOR, "table tbody tr"))
    assert row_count_before == row_count_after

# ==========================================
# SKENARIO 6: Data Sampel Terdampak (TC_SMP_06)
# ==========================================
def test_TC_SMP_06_POS(driver):
    """Positif: Sampel terdampak berhasil ditampilkan"""
    driver.get(f"{BASE_URL}/incidents/1/affected-samples") # Asumsi insiden ID 1
    sample_rows = driver.find_elements(By.CSS_SELECTOR, "table.affected-samples tbody tr")
    assert len(sample_rows) > 0

def test_TC_SMP_06_NEG(driver):
    """Negatif: Tidak ada insiden (Ruang normal), daftar sampel terdampak kosong"""
    driver.get(f"{BASE_URL}/storage-rooms/2/affected-samples") # Asumsi ruang 2 normal
    empty_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_SELECTOR, ".empty-data")))
    assert "Tidak ada insiden aktif" in empty_msg.text

# ==========================================
# SKENARIO 7: Tindakan Perbaikan / CAPA (TC_CAPA_07)
# ==========================================
def test_TC_CAPA_07_POS(driver):
    """Positif: Data tindakan berhasil disimpan"""
    driver.get(f"{BASE_URL}/incidents/1/capa")
    driver.find_element(By.ID, "action_taken").send_keys("Memperbaiki kompresor AC ruangan.")
    wait_and_click(driver, By.ID, "btn-submit-capa")
    success_toast = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_SELECTOR, ".toast-success")))
    assert "Tindakan berhasil disimpan" in success_toast.text

def test_TC_CAPA_07_NEG(driver):
    """Negatif: Form tindakan kosong"""
    driver.get(f"{BASE_URL}/incidents/1/capa")
    driver.find_element(By.ID, "action_taken").clear()
    wait_and_click(driver, By.ID, "btn-submit-capa")
    error_msg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-danger")))
    assert "wajib diisi" in error_msg.text

# ==========================================
# SKENARIO 8: Laporan Insiden (TC_REP_08)
# ==========================================
def test_TC_REP_08_POS(driver):
    """Positif: Laporan berhasil dibuat (Tombol Export tersedia)"""
    driver.get(f"{BASE_URL}/incidents/1")
    export_btn = driver.find_element(By.ID, "btn-export-pdf")
    assert export_btn.is_enabled()

def test_TC_REP_08_NEG(driver):
    """Negatif: Tidak ada data insiden (Belum ada insiden)"""
    # Pada UI, tombol Buat Laporan untuk ruang normal harusnya disabled/hilang
    driver.get(f"{BASE_URL}/monitoring")
    report_btns = driver.find_elements(By.ID, "btn-export-pdf")
    assert len(report_btns) == 0

# ==========================================
# SKENARIO 9: Riwayat Monitoring (TC_HIS_09)
# ==========================================
def test_TC_HIS_09_POS(driver):
    """Positif: Riwayat bertambah setelah input"""
    driver.get(f"{BASE_URL}/monitoring/history")
    history_rows_initial = len(driver.find_elements(By.CSS_SELECTOR, "table tbody tr"))
    
    test_TC_MON_01_POS(driver) # Tambah data
    
    driver.get(f"{BASE_URL}/monitoring/history")
    history_rows_final = len(driver.find_elements(By.CSS_SELECTOR, "table tbody tr"))
    assert history_rows_final == history_rows_initial + 1

def test_TC_HIS_09_NEG(driver):
    """Negatif: Data gagal disimpan (Input tidak valid), riwayat tidak bertambah"""
    driver.get(f"{BASE_URL}/monitoring/history")
    history_rows_initial = len(driver.find_elements(By.CSS_SELECTOR, "table tbody tr"))
    
    test_TC_MON_01_NEG(driver) # Gagal tambah data
    
    driver.get(f"{BASE_URL}/monitoring/history")
    history_rows_final = len(driver.find_elements(By.CSS_SELECTOR, "table tbody tr"))
    assert history_rows_final == history_rows_initial

# ==========================================
# SKENARIO 10: Peringatan Monitoring Terlambat (TC_OVD_10)
# TERKAIT DENGAN SCHEDULER: CheckOverdueMonitoring
# ==========================================
def test_TC_OVD_10_POS(driver):
    """Positif: Tidak ada data monitoring sesuai batas waktu, sistem menampilkan peringatan"""
    # 1. Trigger cron job Overdue secara paksa melalui subprocess (mewakili hourly)
    subprocess.run(["php", "artisan", "monitor:check-overdue"], cwd="/path/to/laravel/project")
    
    # 2. Cek notifikasi Overdue di dashboard
    driver.get(f"{BASE_URL}/dashboard")
    overdue_alert = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'keterlambatan monitoring')]"))
    )
    assert overdue_alert.is_displayed()

def test_TC_OVD_10_NEG(driver):
    """Negatif: Monitoring dilakukan tepat waktu, tidak ada peringatan yang muncul"""
    # 1. Input data monitoring terbaru agar tidak overdue
    test_TC_MON_01_POS(driver)
    
    # 2. Trigger cron job lagi
    subprocess.run(["php", "artisan", "monitor:check-overdue"], cwd="/path/to/laravel/project")
    
    # 3. Validasi alert tidak muncul untuk data baru
    driver.get(f"{BASE_URL}/dashboard")
    time.sleep(1) # Tunggu DOM render
    overdue_alerts = driver.find_elements(By.XPATH, "//*[contains(text(), 'keterlambatan monitoring untuk Ruang Vaksin')]")
    assert len(overdue_alerts) == 0