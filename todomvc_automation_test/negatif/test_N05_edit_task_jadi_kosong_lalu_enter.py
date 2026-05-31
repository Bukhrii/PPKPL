"""
test_N05_edit_task_jadi_kosong_lalu_enter.py
N05: Edit task, hapus semua teks, tekan Enter.

Perilaku deployed version: input kosong + Enter → edit mode tidak di-commit
(task tetap ada). Ini berbeda dari source code original yang memanggil removeItem().
Test memverifikasi bahwa task tidak hilang secara tidak sengaja.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers import add_task, get_tasks, get_counter_text, click_filter, complete_task


def test_N05_edit_task_jadi_kosong_lalu_enter(driver):
    """N05: Edit task jadi kosong + Enter — task tidak terhapus secara tidak sengaja."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    add_task(driver, "Task Untuk Diedit")
    assert len(get_tasks(driver)) == 1

    label = driver.find_element(By.CSS_SELECTOR, "[data-testid='todo-item-label']")
    ActionChains(driver).double_click(label).perform()
    edit = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".input-container input"))
    )
    # Set nilai kosong dan tekan Enter
    driver.execute_script("""
        var el=arguments[0];
        Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value')
            .set.call(el, '');
        el.dispatchEvent(new Event('input',{bubbles:true}));
        el.dispatchEvent(new KeyboardEvent('keydown',{
            key:'Enter',code:'Enter',keyCode:13,which:13,
            bubbles:true,cancelable:true
        }));
    """, edit)
    time.sleep(0.5)
    # Verifikasi: task masih ada (tidak terhapus secara tidak sengaja oleh Enter kosong)
    assert len(get_tasks(driver)) == 1
