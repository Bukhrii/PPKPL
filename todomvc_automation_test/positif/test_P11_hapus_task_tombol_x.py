"""
test_P11_hapus_task_tombol_x.py
P11: Hover task lalu klik tombol X untuk hapus.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P11_hapus_task_tombol_x(driver):
    """P11: Hover task lalu klik tombol X untuk hapus."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    add_task(driver, "Task Dihapus")
    item = driver.find_element(By.CSS_SELECTOR, ".todo-list li")
    ActionChains(driver).move_to_element(item).perform()
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, ".todo-list li .destroy").click()
    time.sleep(0.3)
    assert len(get_tasks(driver)) == 0
