"""
test_P16_filter_completed.py
P16: Filter 'Completed' hanya menampilkan task yang sudah selesai.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P16_filter_completed(driver):
    """P16: Filter 'Completed' hanya menampilkan task yang sudah selesai."""
    from selenium.webdriver.common.by import By
    add_task(driver, "Task Aktif")
    add_task(driver, "Task Selesai")
    complete_task(driver, 1)
    click_filter(driver, "Completed")
    tasks = get_tasks(driver)
    assert len(tasks) == 1
    assert "Task Selesai" in tasks[0].text
