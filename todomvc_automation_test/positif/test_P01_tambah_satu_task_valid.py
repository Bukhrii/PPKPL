"""
test_P01_tambah_satu_task_valid.py
P01: Tambah satu task baru dengan teks valid.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P01_tambah_satu_task_valid(driver):
    """P01: Tambah satu task baru dengan teks valid."""
    add_task(driver, "Belajar Selenium")
    tasks = get_tasks(driver)
    assert len(tasks) == 1
    assert "Belajar Selenium" in tasks[0].text
