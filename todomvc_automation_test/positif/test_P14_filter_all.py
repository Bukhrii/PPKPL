"""
test_P14_filter_all.py
P14: Filter 'All' menampilkan semua task.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P14_filter_all(driver):
    """P14: Filter 'All' menampilkan semua task."""
    add_task(driver, "Aktif")
    add_task(driver, "Selesai")
    complete_task(driver, 0)
    click_filter(driver, "All")
    assert len(get_tasks(driver)) == 2
