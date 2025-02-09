from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    #startujemy przeglądarkę
    browser = p.chromium.launch()
    #otwieramy nową krtę/ stronę w przeglądarce
    page = browser.new_page()
    #przechodzimy na stronę
    page.goto("http://onet.pl")
    #pobieramy tytuł strony
    page_title = page.title()
    #drukujemy na konsole tytuł strony
    print(page_title)

    #assert - pozwala na sprawdzenie czy to co chcemy rzeczywiście jest
    assert "Onet - jesteś na bieżąco" in page_title

    #zamykamy przeglądarkę
    browser.close()
