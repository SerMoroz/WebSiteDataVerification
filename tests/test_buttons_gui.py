import pytest

from pages.web_form_page import WebFormPage

pytestmark = pytest.mark.gui


def test_heading_is_displayed(web_form):
    heading = web_form.find(WebFormPage.HEADING)
    assert heading.is_displayed()
    assert heading.text == "Web form"


def test_submit_button_is_visible_and_enabled(web_form):
    button = web_form.find(WebFormPage.SUBMIT_BUTTON)
    assert button.is_displayed()
    assert button.is_enabled()
    assert button.text == "Submit"


def test_submit_button_shows_confirmation(web_form, driver):
    web_form.find(WebFormPage.TEXT_INPUT).send_keys("Selenium")
    message = web_form.submit()
    assert message.text == "Received!"
    assert "my-text=Selenium" in driver.current_url


def test_checkbox_toggles(web_form):
    checkbox = web_form.find(WebFormPage.CHECKBOX_DEFAULT)
    assert not checkbox.is_selected()
    web_form.click(WebFormPage.CHECKBOX_DEFAULT)
    assert checkbox.is_selected()
    web_form.click(WebFormPage.CHECKBOX_DEFAULT)
    assert not checkbox.is_selected()


def test_radio_buttons_are_mutually_exclusive(web_form):
    first = web_form.find(WebFormPage.RADIO_CHECKED)
    second = web_form.find(WebFormPage.RADIO_DEFAULT)
    assert first.is_selected() and not second.is_selected()
    web_form.click(WebFormPage.RADIO_DEFAULT)
    assert second.is_selected() and not first.is_selected()


def test_disabled_input_is_not_enabled(web_form):
    assert not web_form.find(WebFormPage.DISABLED_INPUT).is_enabled()
