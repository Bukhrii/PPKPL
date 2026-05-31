"""
test_N08_clear_completed_tidak_hapus_aktif.py
N08: 'Clear completed' tidak boleh menghapus task aktif.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N08_clear_completed_tidak_hapus_aktif(driver):
    """N08: 'Clear completed' tidak boleh menghapus task aktif."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Aktif 1"); add_task(driver, "Aktif 2"); add_task(driver, "Selesai")
    complete_task(driver, 2)
    driver.find_element(By.CSS_SELECTOR, ".clear-completed").click()
    time.sleep(0.3)
    tasks = get_tasks(driver)
    assert len(tasks) == 2
    for t in tasks:
        assert "completed" not in t.get_attribute("class")
