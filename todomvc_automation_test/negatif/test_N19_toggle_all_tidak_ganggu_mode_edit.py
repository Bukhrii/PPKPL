"""
test_N19_toggle_all_tidak_ganggu_mode_edit.py
N19: Toggle All tidak crash saat ada task yang sedang dalam mode edit.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N19_toggle_all_tidak_ganggu_mode_edit(driver):
    """N19: Toggle All tidak crash saat ada task yang sedang dalam mode edit."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    add_task(driver, "Task Edit"); add_task(driver, "Task Normal")
    label = driver.find_elements(By.CSS_SELECTOR, ".todo-list li label")[0]
    ActionChains(driver).double_click(label).perform()
    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, ".toggle-all").click()
    time.sleep(0.3)
    assert len(get_tasks(driver)) > 0
