"""
test_N01_enter_tanpa_teks.py
N01: Tekan Enter tanpa mengetik apapun — tidak ada task baru.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N01_enter_tanpa_teks(driver):
    """N01: Tekan Enter tanpa mengetik apapun — tidak ada task baru."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from helpers import wait_for
    import time
    wait_for(driver, By.CLASS_NAME, "new-todo").send_keys(Keys.RETURN)
    time.sleep(0.3)
    assert len(get_tasks(driver)) == 0
