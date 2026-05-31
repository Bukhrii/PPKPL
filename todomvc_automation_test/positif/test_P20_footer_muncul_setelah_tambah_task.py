"""
test_P20_footer_muncul_setelah_tambah_task.py
P20: Footer muncul setelah task pertama ditambahkan.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P20_footer_muncul_setelah_tambah_task(driver):
    """P20: Footer muncul setelah task pertama ditambahkan."""
    from selenium.webdriver.common.by import By
    assert len(driver.find_elements(By.CSS_SELECTOR, ".footer")) == 0
    add_task(driver, "Task Pertama")
    assert driver.find_element(By.CSS_SELECTOR, ".footer").is_displayed()
