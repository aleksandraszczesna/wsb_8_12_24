*** Settings ***
Documentation    Test dodawania do siebie dwóch liczb

*** Test Cases ***
Test Dodawania
    [Documentation]    Test sprawdza, czy dodawanie 2 do liczby ${liczba} daje wynik 6
    ${result}=    Dodaj liczbę    4
    Should Be Equal As Integers    ${result}    6

*** Keywords ***
Dodaj liczbę
    [Arguments]    ${liczba}
    [Documentation]    Dodaje 2 do liczby ${liczba} i zapisuje wynik w zmiennej ${result}
    ${result}=    Evaluate    2 + ${liczba}
    Log    2 + ${liczba} = ${result}
    RETURN  ${result}