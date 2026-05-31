"""
test_N02_submit_task_hanya_spasi.py
N02: Submit task yang hanya berisi spasi — tidak tersimpan.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N02_submit_task_hanya_spasi(driver):
    """N02: Submit task yang hanya berisi spasi — tidak tersimpan."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from helpers import wait_for
    import time
    ib = wait_for(driver, By.CLASS_NAME, "new-todo")
    ib.send_keys("     "); ib.send_keys(Keys.RETURN)
    time.sleep(0.3)
    assert len(get_tasks(driver)) == 0
