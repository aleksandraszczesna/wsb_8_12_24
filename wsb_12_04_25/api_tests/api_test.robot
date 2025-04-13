*** Settings ***
Documentation   Pierwszy test aplikacji API
Library     RequestsLibrary         #pip install robotframework-requests
Library     Collections

*** Test Cases ***
Przykładowy GET na API      #nazwa testu
    [Documentation]  Test GET na API
    ${response}=    GET     http://jsonplaceholder.typicode.com/posts/1
    Should Be Equal As Integers     ${response.status_code}  200        #sprawdzamy kod odpowiedzi
    Log     ${response.text}
    Log     ${response.json()}      #logujemy odpowiedź w formacie json

Sprawdzenie zawartości JSON
    [Documentation]  Test GET na API
    ${response}=    GET     http://jsonplaceholder.typicode.com/posts/1
    ${body}=    Evaluate    ${response.text}
    Should Be Equal As Integers     ${body}[id]     1       #sprawdzamy id
    Should Be Equal As Integers     ${body}[userId]     1       #sprawdzamu user id

Sprawdzenie Dwóch Elementów Z Nagłówka
    [Documentation]    Test GET na API
    Create Session    jsonplaceholder    http://jsonplaceholder.typicode.com
    ${response}=    Get Request    jsonplaceholder    /posts
    ${header}=    Set Variable    ${response.headers}
    Should Be Equal    ${header}[content-type]    application/json; charset=utf-8
    Should Contain    ${header}[date]    GMT

Sprawdzenie tekstu z body
    [Documentation]  Test GET na API
    ${response}=    GET     http://jsonplaceholder.typicode.com/posts/1
    ${body}=    Evaluate    ${response.text}
    Should Not Be Empty    ${body}[title]

Sprawdzenie czy pole title istnieje i nie jest puste
    [Documentation]    Sprawdza, czy pole 'title' istnieje i ma wartość (nie jest puste)
    ${response}=    GET     http://jsonplaceholder.typicode.com/posts/1
    ${body}=    To Json    ${response.content}
    Dictionary Should Contain Key   ${body}     title
    Should Not Be Empty    ${body}[title]