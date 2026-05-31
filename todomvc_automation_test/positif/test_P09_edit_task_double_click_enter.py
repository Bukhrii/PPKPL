"""
test_P09_edit_task_double_click_enter.py
P09: Double-click task, ubah teks, tekan Enter.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def _edit_and_commit(driver, element, new_value, commit="enter"):
    """
    Set nilai edit input React dan commit.
    commit='enter' → tekan Enter via JS KeyboardEvent
    commit='blur'  → klik luar untuk trigger blur
    """
    # Set DOM value + dispatch input event agar React mendeteksi perubahan
    driver.execute_script("""
        var el = arguments[0], val = arguments[1];
        Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value')
            .set.call(el, val);
        el.dispatchEvent(new Event('input', {bubbles: true}));
    """, element, new_value)
    if commit == "enter":
        driver.execute_script("""
            arguments[0].dispatchEvent(new KeyboardEvent('keydown', {
                key: 'Enter', code: 'Enter', keyCode: 13,
                which: 13, bubbles: true, cancelable: true
            }));
        """, element)


def test_P09_edit_task_double_click_enter(driver):
    """P09: Double-click task, ubah teks, tekan Enter."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    add_task(driver, "Teks Lama")
    label = driver.find_element(By.CSS_SELECTOR, "[data-testid='todo-item-label']")
    ActionChains(driver).double_click(label).perform()
    edit = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".input-container input"))
    )
    _edit_and_commit(driver, edit, "Teks Baru", commit="enter")
    time.sleep(0.5)
    assert "Teks Baru" in driver.find_element(
        By.CSS_SELECTOR, "[data-testid='todo-item-label']"
    ).text
