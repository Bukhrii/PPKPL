"""
test_P05_complete_satu_task.py
P05: Klik checkbox untuk menyelesaikan satu task (strikethrough).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P05_complete_satu_task(driver):
    """P05: Klik checkbox untuk menyelesaikan satu task (strikethrough)."""
    from selenium.webdriver.common.by import By
    add_task(driver, "Task Diselesaikan")
    driver.find_element(By.CSS_SELECTOR, ".todo-list li .toggle").click()
    import time; time.sleep(0.3)
    task = driver.find_element(By.CSS_SELECTOR, ".todo-list li")
    assert "completed" in task.get_attribute("class")
