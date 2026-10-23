from urllib.parse import urlparse

import pytest

pytestmark = pytest.mark.url


def test_page_opens_on_expected_address(web_form, driver):
    assert driver.current_url == web_form.url


def test_page_is_served_over_https(web_form, driver):
    assert urlparse(driver.current_url).scheme == "https"


def test_page_domain_matches_base_url(web_form, driver, base_url):
    assert urlparse(driver.current_url).netloc == urlparse(base_url).netloc


def test_page_title(web_form, driver):
    assert driver.title == "Web form"


def test_submit_navigates_to_result_address(web_form, driver):
    web_form.submit()
    current = urlparse(driver.current_url)
    assert current.path.endswith("/submitted-form.html")
    assert "my-text=" in current.query
