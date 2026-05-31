"""
test_N12_filter_completed_tidak_tampilkan_aktif.py
N12: Filter 'Completed' tidak menampilkan task aktif.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N12_filter_completed_tidak_tampilkan_aktif(driver):
    """N12: Filter 'Completed' tidak menampilkan task aktif."""
    add_task(driver, "Aktif"); add_task(driver, "Selesai")
    complete_task(driver, 1)
    click_filter(driver, "Completed")
    for t in get_tasks(driver):
        assert "completed" in t.get_attribute("class")
