"""
test_P19_counter_bertambah_saat_uncheck.py
P19: Counter bertambah kembali saat task completed di-uncheck.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P19_counter_bertambah_saat_uncheck(driver):
    """P19: Counter bertambah kembali saat task completed di-uncheck."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task")
    cb = driver.find_element(By.CSS_SELECTOR, ".todo-list li .toggle")
    cb.click(); time.sleep(0.2)
    assert "0" in get_counter_text(driver)
    cb.click(); time.sleep(0.2)
    assert "1" in get_counter_text(driver)
