*** Settings ***
Documentation     Test metody POST
Library           RequestsLibrary
Library           Collections

*** Test Cases ***
Dodanie nowego posta (POST)
    [Documentation]  Test wysyła POST do API tworząc nowy wpis i weryfikuje odpowiedź
    ${body}=    Create Dictionary    title=Testowy post    body=To jest treść testowego posta    userId=1
    ${response}=    POST    http://jsonplaceholder.typicode.com/posts    json=${body}
    ${response_body}=    Evaluate    json.loads("""${response.text}""")    json
    Should Be Equal As Integers     ${response.status_code}     201
    Should Be Equal     ${response_body}[title]     Testowy post
    Should Be Equal     ${response_body}[body]      To jest treść testowego posta
    Should Be Equal As Integers     ${response_body}[userId]    1
    Dictionary Should Contain Key   ${response_body}     id