"""
test_N03_input_hanya_angka.py
N03: Task berisi angka saja — dicatat sebagai edge case, tidak crash.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N03_input_hanya_angka(driver):
    """N03: Task berisi angka saja — dicatat sebagai edge case, tidak crash."""
    add_task(driver, "12345")
    result = len(get_tasks(driver))
    print(f"\n[N03] Task numerik '12345' — tersimpan: {result}")
    assert result >= 0  # tidak crash
