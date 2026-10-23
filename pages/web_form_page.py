from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebFormPage:
    """Page object for the web form under test."""

    PATH = "/selenium/web/web-form.html"

    HEADING = (By.TAG_NAME, "h1")
    TEXT_INPUT = (By.ID, "my-text-id")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CHECKBOX_CHECKED = (By.ID, "my-check-1")
    CHECKBOX_DEFAULT = (By.ID, "my-check-2")
    RADIO_CHECKED = (By.ID, "my-radio-1")
    RADIO_DEFAULT = (By.ID, "my-radio-2")
    DISABLED_INPUT = (By.NAME, "my-disabled")
    RESULT_MESSAGE = (By.ID, "message")

    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.url = base_url.rstrip("/") + self.PATH
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.url)
        self.wait.until(EC.visibility_of_element_located(self.HEADING))
        return self

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def submit(self):
        self.click(self.SUBMIT_BUTTON)
        return self.wait.until(EC.visibility_of_element_located(self.RESULT_MESSAGE))
