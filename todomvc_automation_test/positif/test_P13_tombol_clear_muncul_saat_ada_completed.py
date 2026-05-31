"""
test_P13_tombol_clear_muncul_saat_ada_completed.py
P13: Tombol 'Clear completed' aktif (tidak disabled) setelah ada task selesai.

Versi React terbaru: button selalu ada di DOM tetapi ber-atribut `disabled`
saat tidak ada completed task, dan `disabled` dihapus saat ada completed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P13_tombol_clear_muncul_saat_ada_completed(driver):
    """P13: Tombol 'Clear completed' aktif setelah ada task selesai."""
    from selenium.webdriver.common.by import By
    import time
    add_task(driver, "Task Test")
    # Sebelum complete: button disabled
    btn_before = driver.find_element(By.CSS_SELECTOR, ".clear-completed")
    assert btn_before.get_attribute("disabled") is not None, \
        "Tombol seharusnya disabled sebelum ada completed task"
    # Selesaikan task
    complete_task(driver, 0)
    time.sleep(0.3)
    # Setelah complete: button harus enabled (disabled attribute hilang)
    btn_after = driver.find_element(By.CSS_SELECTOR, ".clear-completed")
    assert btn_after.get_attribute("disabled") is None, \
        "Tombol seharusnya enabled setelah ada completed task"
