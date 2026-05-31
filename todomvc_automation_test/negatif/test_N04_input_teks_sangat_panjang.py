"""
test_N04_input_teks_sangat_panjang.py
N04: Input task 500+ karakter — halaman tidak crash.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N04_input_teks_sangat_panjang(driver):
    """N04: Input task 500+ karakter — halaman tidak crash."""
    from selenium.webdriver.common.by import By
    add_task(driver, "A" * 500)
    assert driver.find_element(By.CLASS_NAME, "new-todo") is not None
    print(f"\n[N04] 500 karakter — task tersimpan: {len(get_tasks(driver))}")
