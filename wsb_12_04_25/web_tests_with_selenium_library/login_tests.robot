*** Settings ***
Documentation   Testy logowania do aplikacji the-internet
Library     SeleniumLibrary

*** Variables ***
${LOGIN_URL}    https://the-internet.herokuapp.com/login
${BROWSER}  Chrome
${VALID_USER}   tomsmith
${VALID_PASS}   SuperSecretPassword!
${INVALID_PASS}     BledneHaslo

*** Test Cases ***
Udane Logowanie
    [Documentation]  Test logowania z poprawnymi danymi
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible   id:username     timeout=5
    Input Text  id:username     ${VALID_USER}
    Input Text  id:password     ${VALID_PASS}
    Click Button    css:.radius
    Element Should Be Visible   css:a[href="/logout"]
    Close Browser

Nieudane logowanie
    [Documentation]  Test logowania z niepoprawnymi danymi
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible   id:username     timeout=5
    Input Text  id:username     ${VALID_USER}
    Input Text  id:password     ${INVALID_PASS}
    Click Button    css:.radius
    Element Should Not Be Visible   css:a[href="/logout"]
    Close Browser

Wylogowanie
    [Documentation]  Test wylogowania
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible   id:username     timeout=5
    Input Text  id:username     ${VALID_USER}
    Input Text  id:password     ${VALID_PASS}
    Click Button    css:.radius
    Click Element    css:a[href="/logout"]
    Element Should Be Visible   css:.radius
    Page Should Contain     Login Page
    Close Browser