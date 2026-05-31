"""
test_N10_hapus_semua_task_list_kosong.py
N10: Hapus semua task → list kosong dan footer menghilang.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N10_hapus_semua_task_list_kosong(driver):
    """N10: Hapus semua task → list kosong dan footer menghilang."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    add_task(driver, "Task 1"); add_task(driver, "Task 2")
    for _ in range(2):
        item = driver.find_element(By.CSS_SELECTOR, ".todo-list li")
        ActionChains(driver).move_to_element(item).perform()
        time.sleep(0.2)
        driver.find_element(By.CSS_SELECTOR, ".todo-list li .destroy").click()
        time.sleep(0.3)
    assert len(get_tasks(driver)) == 0
    assert len(driver.find_elements(By.CSS_SELECTOR, ".footer")) == 0
