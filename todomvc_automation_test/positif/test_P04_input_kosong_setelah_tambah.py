"""
test_P04_input_kosong_setelah_tambah.py
P04: Input field kembali kosong setelah task berhasil ditambah.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P04_input_kosong_setelah_tambah(driver):
    """P04: Input field kembali kosong setelah task berhasil ditambah."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from helpers import wait_for
    input_box = wait_for(driver, By.CLASS_NAME, "new-todo")
    input_box.send_keys("Task Baru")
    input_box.send_keys(Keys.RETURN)
    import time; time.sleep(0.3)
    input_box = driver.find_element(By.CLASS_NAME, "new-todo")
    assert input_box.get_attribute("value") == ""

