"""
test_N20_refresh_semua_task_hilang.py
N20: Setelah refresh, semua task hilang (tidak ada persistence).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N20_refresh_semua_task_hilang(driver):
    """N20: Setelah refresh, semua task hilang (tidak ada persistence)."""
    import time
    add_task(driver, "Task Sebelum Refresh")
    assert len(get_tasks(driver)) == 1
    driver.refresh()
    time.sleep(1)
    assert len(get_tasks(driver)) == 0
