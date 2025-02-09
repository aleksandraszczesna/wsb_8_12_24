from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # utworzenie kontekstu API - inny niż przeglądarki
    request_context = p.request.new_context()
    #deklaracja danych do wysłania
    userId = 9
    new_post = {"userId": userId, "title": "title sample", "body": "body sample"}
    print("wysyłamy nowy post: ", new_post)
    # wysyłanie żądania POST do API
    response = request_context.post("https://jsonplaceholder.typicode.com/posts", data=new_post)

    status = response.status
    print("Status: ", status)
    assert status == 201

    result = response.json()
    print("Odpowiedź JSON: ", result)

    assert result["userId"] == new_post["userId"]
    assert result["title"] == new_post["title"]
    assert result["body"] == new_post["body"]

