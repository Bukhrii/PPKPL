"""
test_P18_counter_berkurang_saat_complete.py
P18: Counter 'items left' berkurang saat task di-complete.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P18_counter_berkurang_saat_complete(driver):
    """P18: Counter 'items left' berkurang saat task di-complete."""
    add_task(driver, "Task 1")
    add_task(driver, "Task 2")
    assert "2" in get_counter_text(driver)
    complete_task(driver, 0)
    assert "1" in get_counter_text(driver)
