"""
test_P07_toggle_all_selesaikan_semua.py
P07: Klik 'Toggle All' untuk selesaikan semua task sekaligus.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P07_toggle_all_selesaikan_semua(driver):
    """P07: Klik 'Toggle All' untuk selesaikan semua task sekaligus."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task A")
    add_task(driver, "Task B")
    driver.find_element(By.CSS_SELECTOR, ".toggle-all").click()
    time.sleep(0.3)
    tasks = get_tasks(driver)
    for t in tasks:
        assert "completed" in t.get_attribute("class")
    assert "0" in get_counter_text(driver)
