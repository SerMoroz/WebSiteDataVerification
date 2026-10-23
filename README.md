# WebSiteDataVerification

Automated UI checks for a website, written in Python with **Selenium WebDriver** and **pytest**.

The suite verifies two things:

- **Website address**: the page opens on the expected URL, over HTTPS, on the right domain, with the right title, and the form submits to the expected result address.
- **Buttons and GUI elements**: the Submit button is visible, enabled and shows a confirmation; checkboxes toggle; radio buttons are mutually exclusive; disabled fields can't be used.

By default the tests run against the public Selenium practice page
[`https://www.selenium.dev/selenium/web/web-form.html`](https://www.selenium.dev/selenium/web/web-form.html).

## Project structure

```
WebSiteDataVerification/
├── pages/
│   └── web_form_page.py     # Page Object: URL, locators, actions
├── tests/
│   ├── conftest.py          # WebDriver fixture and CLI options
│   ├── test_url.py          # Website address checks
│   └── test_buttons_gui.py  # Button and GUI element checks
├── pytest.ini
└── requirements.txt
```

## Requirements

- Python 3.9+
- Google Chrome. Selenium Manager (part of Selenium 4) downloads a matching chromedriver automatically.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the tests

Run everything (headless Chrome):

```bash
pytest
```

Watch the browser while the tests run:

```bash
pytest --headed
```

Run only one group of checks:

```bash
pytest -m url    # website address checks
pytest -m gui    # button / GUI checks
```

Point the suite at another host serving the same page:

```bash
pytest --base-url https://example.com
```

`BASE_URL` can be set as an environment variable instead of passing `--base-url`.

## Test cases

| File | Test | What it checks |
|------|------|----------------|
| `test_url.py` | `test_page_opens_on_expected_address` | Browser lands on the exact expected URL |
| | `test_page_is_served_over_https` | URL scheme is `https` |
| | `test_page_domain_matches_base_url` | Domain matches the configured base URL |
| | `test_page_title` | Page title is `Web form` |
| | `test_submit_navigates_to_result_address` | Submitting goes to `submitted-form.html` with form data in the query |
| `test_buttons_gui.py` | `test_heading_is_displayed` | Page heading is visible with the right text |
| | `test_submit_button_is_visible_and_enabled` | Submit button is shown, clickable and labelled |
| | `test_submit_button_shows_confirmation` | Clicking Submit shows `Received!` |
| | `test_checkbox_toggles` | Checkbox can be checked and unchecked |
| | `test_radio_buttons_are_mutually_exclusive` | Selecting one radio button deselects the other |
| | `test_disabled_input_is_not_enabled` | Disabled input cannot be interacted with |

## Adapting to your own website

1. Change `PATH` and the locators in `pages/web_form_page.py` to match your page.
2. Set `DEFAULT_BASE_URL` in `tests/conftest.py`, or pass `--base-url`.
3. Update the expected title and texts in the tests.
