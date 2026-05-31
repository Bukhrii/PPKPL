"""
test_P08_toggle_all_dua_kali_aktifkan_semua.py
P08: Toggle All dua kali → semua task kembali aktif.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P08_toggle_all_dua_kali_aktifkan_semua(driver):
    """P08: Toggle All dua kali → semua task kembali aktif."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task A")
    add_task(driver, "Task B")
    toggle = driver.find_element(By.CSS_SELECTOR, ".toggle-all")
    toggle.click(); time.sleep(0.2)
    toggle.click(); time.sleep(0.2)
    for t in get_tasks(driver):
        assert "completed" not in t.get_attribute("class")
