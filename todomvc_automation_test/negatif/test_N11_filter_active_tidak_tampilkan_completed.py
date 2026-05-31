"""
test_N11_filter_active_tidak_tampilkan_completed.py
N11: Filter 'Active' tidak menampilkan task completed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N11_filter_active_tidak_tampilkan_completed(driver):
    """N11: Filter 'Active' tidak menampilkan task completed."""
    add_task(driver, "Aktif"); add_task(driver, "Selesai")
    complete_task(driver, 1)
    click_filter(driver, "Active")
    for t in get_tasks(driver):
        assert "completed" not in t.get_attribute("class")
