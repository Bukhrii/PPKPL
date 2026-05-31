"""
test_P02_tambah_3_task_berturut.py
P02: Tambah 3 task berturut-turut, counter harus = 3.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P02_tambah_3_task_berturut(driver):
    """P02: Tambah 3 task berturut-turut, counter harus = 3."""
    add_task(driver, "Task Pertama")
    add_task(driver, "Task Kedua")
    add_task(driver, "Task Ketiga")
    tasks = get_tasks(driver)
    assert len(tasks) == 3
    assert "3" in get_counter_text(driver)
