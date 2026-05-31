"""
test_P17_filter_tetap_aktif_setelah_tambah.py
P17: Filter yang aktif tidak reset saat task baru ditambahkan.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P17_filter_tetap_aktif_setelah_tambah(driver):
    """P17: Filter yang aktif tidak reset saat task baru ditambahkan."""
    from selenium.webdriver.common.by import By
    add_task(driver, "Task Awal")
    click_filter(driver, "Active")
    add_task(driver, "Task Baru")
    active = driver.find_element(By.CSS_SELECTOR, ".filters .selected")
    assert active.text == "Active" 
