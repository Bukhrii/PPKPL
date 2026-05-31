"""
test_N14_filter_completed_kosong_belum_ada_selesai.py
N14: Filter 'Completed' kosong jika belum ada task yang di-check.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N14_filter_completed_kosong_belum_ada_selesai(driver):
    """N14: Filter 'Completed' kosong jika belum ada task yang di-check."""
    add_task(driver, "Task Aktif Saja")
    click_filter(driver, "Completed")
    assert len(get_tasks(driver)) == 0
