"""
test_N07_edit_task_jadi_hanya_spasi.py
N07: Edit task, isi hanya spasi, tekan Enter.

Perilaku deployed version: spasi-only + Enter → tidak di-commit (task tetap ada).
Test memverifikasi bahwa task tidak hilang secara tidak sengaja akibat input spasi.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N07_edit_task_jadi_hanya_spasi(driver):
    """N07: Edit task jadi hanya spasi + Enter — task tidak terhapus secara tidak sengaja."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    add_task(driver, "Task Normal")
    assert len(get_tasks(driver)) == 1

    label = driver.find_element(By.CSS_SELECTOR, "[data-testid='todo-item-label']")
    ActionChains(driver).double_click(label).perform()
    edit = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".input-container input"))
    )
    # Set nilai hanya spasi dan tekan Enter
    driver.execute_script("""
        var el=arguments[0];
        Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value')
            .set.call(el, '   ');
        el.dispatchEvent(new Event('input',{bubbles:true}));
        el.dispatchEvent(new KeyboardEvent('keydown',{
            key:'Enter',code:'Enter',keyCode:13,which:13,
            bubbles:true,cancelable:true
        }));
    """, edit)
    time.sleep(0.5)
    # Verifikasi: task masih ada (tidak hilang karena input spasi saja)
    assert len(get_tasks(driver)) == 1
