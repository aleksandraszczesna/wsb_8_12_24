from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #utworzenie kontekstu API - inny niż przeglądarki
    request_context = p.request.new_context()
    #wysyłanie żądania GET do API
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
    #sprawdzenie statusu odpowiedzi
    status = response.status

    print("Status odpowiedzi:", status)
    assert status == 200

    body = response.json()
    print(body)

    id = body["id"] #spodziewany zwrot 1
    user_id = body["userId"]
    print("Id to:", id)
    print("UserId to:", user_id)

    assert id == 1
    assert user_id == 1

    title = body["title"]
    print("Typ title to string: ", isinstance(title, str))
    assert isinstance(title, str)

