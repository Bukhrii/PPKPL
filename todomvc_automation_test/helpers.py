"""
helpers.py
Fungsi-fungsi reusable untuk semua test TodoMVC.
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL     = "https://todomvc.com/examples/react/dist/"
TIMEOUT = 10


def wait_for(driver, by, value, timeout=TIMEOUT):
    """Tunggu hingga elemen muncul di DOM."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )


def add_task(driver, text):
    """Tambah satu task ke list."""
    input_box = wait_for(driver, By.CLASS_NAME, "new-todo")
    input_box.send_keys(text)
    input_box.send_keys(Keys.RETURN)
    time.sleep(0.3)


def get_tasks(driver):
    """Ambil semua elemen task yang sedang tampil."""
    return driver.find_elements(By.CSS_SELECTOR, ".todo-list li")


def get_counter_text(driver):
    """Ambil teks counter 'X items left'."""
    try:
        return driver.find_element(By.CSS_SELECTOR, ".todo-count").text
    except Exception:
        return ""


def click_filter(driver, label):
    """Klik tombol filter: 'All', 'Active', atau 'Completed'."""
    driver.find_element(By.LINK_TEXT, label).click()
    time.sleep(0.3)


def complete_task(driver, index=0):
    """Centang checkbox task pada posisi index."""
    checkboxes = driver.find_elements(By.CSS_SELECTOR, ".todo-list li .toggle")
    checkboxes[index].click()
    time.sleep(0.2)
