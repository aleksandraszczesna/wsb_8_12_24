from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username
    page.fill("#username","student")
    # wprowadzenie password
    page.fill("#password","Password123")
    # klikniecie przycisku Submit
    page.click("#submit")
    # czekamy na przekierowanie do strony
    page.wait_for_url("**/logged-in-successfully/") # czekamy aż URL zawiera logged-in-sccuessfully

    page_url = page.url
    assert page_url in "https://practicetestautomation.com/logged-in-successfully/"

    # Logged In Successfully
    success_message = "Logged In Successfully"
    message = page.text_content("h1")
    print(f"Zawartosc naglowka to {message}")

    assert success_message in message

    # sprawdzenie czy element z tekstem Log out jest widoczny na stronie
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True

    browser.close()
