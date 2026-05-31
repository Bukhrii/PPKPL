"""
test_N16_counter_konsisten_complete_lalu_hapus.py
N16: Counter konsisten setelah task di-complete lalu langsung dihapus.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N16_counter_konsisten_complete_lalu_hapus(driver):
    """N16: Counter konsisten setelah task di-complete lalu langsung dihapus."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    add_task(driver, "Task A"); add_task(driver, "Task B")
    complete_task(driver, 0)
    items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
    ActionChains(driver).move_to_element(items[0]).perform()
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, ".todo-list li .destroy").click()
    time.sleep(0.3)
    assert "1" in get_counter_text(driver)
