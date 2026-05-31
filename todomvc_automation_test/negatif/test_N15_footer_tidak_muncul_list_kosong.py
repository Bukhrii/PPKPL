"""
test_N15_footer_tidak_muncul_list_kosong.py
N15: Footer tidak muncul saat belum ada task sama sekali.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N15_footer_tidak_muncul_list_kosong(driver):
    """N15: Footer tidak muncul saat belum ada task sama sekali."""
    from selenium.webdriver.common.by import By
    assert len(driver.find_elements(By.CSS_SELECTOR, ".footer")) == 0
