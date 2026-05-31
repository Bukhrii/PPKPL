"""
test_P03_urutan_task_fifo.py
P03: Task baru muncul di bawah task sebelumnya (urutan FIFO).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P03_urutan_task_fifo(driver):
    """P03: Task baru muncul di bawah task sebelumnya (urutan FIFO)."""
    add_task(driver, "Pertama")
    add_task(driver, "Kedua")
    tasks = get_tasks(driver)
    assert "Pertama" in tasks[0].text
    assert "Kedua" in tasks[1].text
