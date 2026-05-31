"""
test_P06_uncheck_task_completed.py
P06: Uncheck task completed agar kembali aktif.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P06_uncheck_task_completed(driver):
    """P06: Uncheck task completed agar kembali aktif."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task Uncheck")
    cb = driver.find_element(By.CSS_SELECTOR, ".todo-list li .toggle")
    cb.click(); time.sleep(0.2)
    cb.click(); time.sleep(0.2)
    task = driver.find_element(By.CSS_SELECTOR, ".todo-list li")
    assert "completed" not in task.get_attribute("class")
