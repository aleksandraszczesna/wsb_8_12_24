*** Variables ***
${USER}    Ola

*** Test Cases ***
Test Zmiennej
    Log     Uzytkownik: ${USER}
    Should Be Equal     ${USER}     Ola