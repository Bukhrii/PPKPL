"""
test_N17_counter_nol_saat_semua_selesai.py
N17: Counter menampilkan '0 items left' saat semua task selesai.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N17_counter_nol_saat_semua_selesai(driver):
    """N17: Counter menampilkan '0 items left' saat semua task selesai."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task")
    driver.find_element(By.CSS_SELECTOR, ".todo-list li .toggle").click()
    time.sleep(0.3)
    assert "0" in get_counter_text(driver)
