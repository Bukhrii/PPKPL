"""
test_P15_filter_active.py
P15: Filter 'Active' hanya menampilkan task yang belum selesai.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P15_filter_active(driver):
    """P15: Filter 'Active' hanya menampilkan task yang belum selesai."""
    from selenium.webdriver.common.by import By
    add_task(driver, "Task Aktif")
    add_task(driver, "Task Selesai")
    complete_task(driver, 1)
    click_filter(driver, "Active")
    tasks = get_tasks(driver)
    assert len(tasks) == 1
    assert "Task Aktif" in tasks[0].text
