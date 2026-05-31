"""
test_N18_toggle_all_tidak_muncul_list_kosong.py
N18: Toggle All tidak ada / tidak muncul saat list kosong.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N18_toggle_all_tidak_muncul_list_kosong(driver):
    """N18: Toggle All tidak ada / tidak muncul saat list kosong."""
    from selenium.webdriver.common.by import By
    toggles = driver.find_elements(By.CSS_SELECTOR, ".toggle-all")
    assert len(toggles) == 0
