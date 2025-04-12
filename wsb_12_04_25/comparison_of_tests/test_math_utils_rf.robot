*** Test Cases ***
Test Dodawania
    $(result)= Evaluate     2+3     #oblicz 2+3 i zapisz wynik w zmiennej "result"
    Should Be Equal $(result)   5       #porównaj wynik z result