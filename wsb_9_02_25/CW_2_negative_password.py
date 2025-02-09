from playwright.sync_api import sync_playwright
file_path = "password.txt"

with open(file_path) as file:
    password = file.read().strip() #strip() - usuwa puste pola
print(f"Podane hasło to: {password}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "student")
    page.fill("#password", password)
    page.click("#submit")

    page.wait_for_selector("text=Your password is invalid!")

    assert page.locator("div#error").filter(has_text="Your password is invalid!").is_visible()

    locator_password = page.locator("div#error").filter(has_text="Your password is invalid!")
    assert locator_password.is_visible()

    browser.close()