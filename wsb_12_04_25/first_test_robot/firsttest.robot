*** Settings ***
Documentation    Przykładowy pierwszy test w Robot Framework

*** Test Cases ***
Hello World Name
    [Documentation]    Test sprawdza czy 2+2=4
    ${result}=    Evaluate    2+2       # oblicz 2+2 i zapisz wynik w zmiennej
    Should Be Equal As Integers    ${result}    4       # porównaj wynik z result