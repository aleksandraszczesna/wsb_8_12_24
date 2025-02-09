from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "User")
    page.fill("#password", "Password123")
    page.click("#submit")

    page.wait_for_selector("text=Your username is invalid!")

    locator_username_error_text = page.locator("#error").inner_text()
    assert (locator_username_error_text == "Your username is invalid!") is True

    browser.close()