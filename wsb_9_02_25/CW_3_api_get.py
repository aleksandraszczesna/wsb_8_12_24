from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/posts")

    status = response.status
    print("Status: ", status)
    assert status == 200

    posts = response.json()
    print("Odpowiedź JSON: ", posts)

    if len(posts) > 0:
        print(f"W odpowiedzi znajduje się {len(posts)} postów")
        for post in posts:
            print(post)
    else:
        print("W odpowiedzi nie ma żadnych postów")