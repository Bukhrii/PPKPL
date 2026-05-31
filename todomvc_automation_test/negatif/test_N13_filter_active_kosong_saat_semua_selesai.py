"""
test_N13_filter_active_kosong_saat_semua_selesai.py
N13: Filter 'Active' kosong setelah semua task di-Toggle All.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N13_filter_active_kosong_saat_semua_selesai(driver):
    """N13: Filter 'Active' kosong setelah semua task di-Toggle All."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task A"); add_task(driver, "Task B")
    driver.find_element(By.CSS_SELECTOR, ".toggle-all").click()
    time.sleep(0.2)
    click_filter(driver, "Active")
    assert len(get_tasks(driver)) == 0
