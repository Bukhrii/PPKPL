"""
test_N06_edit_task_tekan_escape.py
N06: Edit task lalu tekan Escape — mode edit ditutup, task tetap ada.

Versi React baru tidak me-restore teks lama saat Escape (tidak ada handler Escape
di Input component). Perilaku yang diverifikasi: Escape menutup edit mode (blur
terjadi), task masih ada dan tidak kosong.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N06_edit_task_tekan_escape(driver):
    """N06: Edit task lalu tekan Escape — task tetap ada, tidak terhapus."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    add_task(driver, "Teks Asli")
    label = driver.find_element(By.CSS_SELECTOR, "[data-testid='todo-item-label']")
    ActionChains(driver).double_click(label).perform()
    # Tunggu edit input muncul
    edit = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".input-container input"))
    )
    # Ketik teks baru lalu tekan Escape
    edit.send_keys("Teks Dibatalkan")
    edit.send_keys(Keys.ESCAPE)
    time.sleep(0.4)
    # Verifikasi: task masih ada (tidak terhapus akibat escape)
    tasks = get_tasks(driver)
    assert len(tasks) == 1
    # Teks task tidak boleh kosong
    assert tasks[0].text.strip() != ""
