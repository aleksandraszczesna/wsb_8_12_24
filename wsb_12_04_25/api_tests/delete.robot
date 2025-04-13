*** Settings ***
Documentation     Test metody DELETE
Library           RequestsLibrary
Library           Collections

*** Test Cases ***
Usunięcie istniejącego posta
    [Documentation]  Test wysyła DELETE aby usunąć posta i sprawdzić odpowiedź
    ${response}=    DELETE  http://jsonplaceholder.typicode.com/posts/1
    Log    ${response.status_code}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.content}    {}