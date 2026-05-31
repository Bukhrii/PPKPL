"""
conftest.py
Fixture pytest yang dipakai bersama oleh semua file test.
Driver dibuka sebelum tiap test dan ditutup otomatis sesudahnya.

Cara pakai:
  Normal (headed)  : pytest
  Headless (new)   : pytest --headless
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import URL


def pytest_addoption(parser):
    """Tambah opsi --headless ke CLI pytest."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Jalankan browser dalam mode headless=new (tanpa tampilan)",
    )


@pytest.fixture
def driver(request):
    options = Options()
    if request.config.getoption("--headless"):
        # Mode headless modern Chrome (lebih stabil dari --headless lama)
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")

    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)
    drv.get(URL)
    yield drv
    drv.quit()
