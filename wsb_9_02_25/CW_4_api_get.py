from playwright.sync_api import sync_playwright
from psutil import users

with sync_playwright() as p:
    request_context = p.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/users/1")
    if response.status == 200:
        user = response.json()
        user_name = user.get('name')
        print("Imię i nazwisko użytkownika to: ", user_name)
    else:
        print("Brak danych")


    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    try:
        page.click('#L2AGLb')  # Kliknij przycisk akceptacji cookies
    except:
        print("Nie znaleziono przycisku akceptacji cookies")
    page.fill("#APjFqb", user_name)

    # mozna szukac po dowolnym elemencie html, przyklad class czyli . , id czyli # , albo jak niżej input[value='Nazwa inputu to co w value']
    #page.click("input[value='Szukaj w Google']")
    page.click("input.gNO89b") # input to nazwa elementu html moze tez byc h1, p itp itd, dalej mozemy wpisac po kropce nazwe klasy

    # ręcznie trzeba  przeklikac captche to test działa

    first_result = page.locator(".g").first.inner_text()
    print("Pierwszy wynik wyszukiwania:", first_result)

    browser.close()