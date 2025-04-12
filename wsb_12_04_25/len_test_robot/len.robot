*** Settings ***
Documentation    Test for len function

*** Test Cases ***
String Length Test
    [Documentation]    Test the length of a string
    ${text}=    Set Variable    Hello, World!       #ustawiamy zmienną tekstową
    ${length}=  Evaluate    len("${text}")      #obliczamy długość tekstu
    Should Be Equal As Numbers    ${length}    13