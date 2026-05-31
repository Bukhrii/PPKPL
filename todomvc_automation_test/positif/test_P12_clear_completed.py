"""
test_P12_clear_completed.py
P12: Clear completed hanya hapus task selesai, task aktif tetap.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P12_clear_completed(driver):
    """P12: Clear completed hanya hapus task selesai, task aktif tetap."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task Aktif")
    add_task(driver, "Task Selesai")
    complete_task(driver, 1)
    driver.find_element(By.CSS_SELECTOR, ".clear-completed").click()
    time.sleep(0.3)
    tasks = get_tasks(driver)
    assert len(tasks) == 1
    assert "Task Aktif" in tasks[0].text
