import os

import pytest
from selenium import webdriver

from pages.web_form_page import WebFormPage

DEFAULT_BASE_URL = "https://www.selenium.dev"


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        default=os.getenv("BASE_URL", DEFAULT_BASE_URL),
        help="Base URL of the website under test",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Show the browser window instead of running headless",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    # Selenium Manager downloads a matching chromedriver automatically.
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def web_form(driver, base_url):
    return WebFormPage(driver, base_url).open()
