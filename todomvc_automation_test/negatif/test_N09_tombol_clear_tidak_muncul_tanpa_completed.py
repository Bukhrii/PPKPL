"""
test_N09_tombol_clear_tidak_muncul_tanpa_completed.py
N09: Tombol 'Clear completed' disabled jika tidak ada task selesai.

Versi React terbaru: button selalu ada di DOM dengan atribut `disabled`
saat tidak ada completed task. Button menjadi enabled saat ada completed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N09_tombol_clear_tidak_muncul_tanpa_completed(driver):
    """N09: Tombol 'Clear completed' disabled saat tidak ada task selesai."""
    from selenium.webdriver.common.by import By
    add_task(driver, "Task Aktif Saja")

    btns = driver.find_elements(By.CSS_SELECTOR, ".clear-completed")

    if not btns:
        # Tombol tidak ada di DOM sama sekali → pass
        assert len(btns) == 0
    else:
        btn = btns[0]
        # Versi React baru: gunakan atribut `disabled` untuk menyembunyikan tombol
        disabled_attr = btn.get_attribute("disabled")
        assert disabled_attr is not None, (
            "Clear completed button seharusnya disabled saat tidak ada task selesai. "
            f"disabled attribute = {disabled_attr!r}"
        )
