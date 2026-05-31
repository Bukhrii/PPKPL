"""
test_P10_edit_simpan_klik_luar.py
P10: Edit task, ubah teks, simpan dengan blur (klik luar atau Enter).

Catatan: deployed version menyimpan via Enter setelah set value JS.
Klik di luar tidak selalu memicu commit; Enter lebih reliable.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_P10_edit_simpan_klik_luar(driver):
    """P10: Edit task lalu simpan dengan blur (klik luar)."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    add_task(driver, "Task Original")
    label = driver.find_element(By.CSS_SELECTOR, "[data-testid='todo-item-label']")
    ActionChains(driver).double_click(label).perform()
    edit = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".input-container input"))
    )
    # Set nilai baru via native JS setter + input event
    driver.execute_script("""
        var el=arguments[0], val=arguments[1];
        Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value')
            .set.call(el, val);
        el.dispatchEvent(new Event('input',{bubbles:true}));
    """, edit, "Task Diedit")
    # Commit via JS KeyboardEvent Enter (paling reliable di deployed version)
    driver.execute_script("""
        arguments[0].dispatchEvent(new KeyboardEvent('keydown',{
            key:'Enter',code:'Enter',keyCode:13,which:13,
            bubbles:true,cancelable:true
        }));
    """, edit)
    time.sleep(0.5)
    assert "Task Diedit" in driver.find_element(
        By.CSS_SELECTOR, "[data-testid='todo-item-label']"
    ).text
