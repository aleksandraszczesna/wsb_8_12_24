*** Settings ***
Documentation     Pobranie użytkownika i sprawdzenie poprawność danych
Library           RequestsLibrary
Library           Collections

*** Test Cases ***
Pobranie użytkownika i sprawdzenie poprawność danych
    [Documentation]     Test pobiera dane użytkownika i weryfikuje poprawność danych
    ${response}=    GET     https://jsonplaceholder.typicode.com/users/5
    ${body}=    Evaluate    ${response.text}
    Log    ${body}
    Should Be Equal As Integers     ${body}[id]     5
    Should Be Equal     ${body}[username]       Kamren
    Should Be Equal As Integers     ${body}[address][zipcode]        33263