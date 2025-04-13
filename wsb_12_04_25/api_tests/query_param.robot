*** Settings ***
Documentation     Test metody GET z parametrami
Library           RequestsLibrary

*** Test Cases ***
Filtracja komentarzy po postID
    [Documentation]     Sprawdza czy GET zwraca tylko komentarze powiązane z postem o id 1
    ${params}=    Create Dictionary    postId=1     # Wysyłamy zapytanie GET z parametrem
    ${response}=    GET    http://jsonplaceholder.typicode.com/comments    params=${params}
    Should Be Equal As Integers     ${response.status_code}     200     # Sprawdzamy status odpowiedzi
    ${comments}=    To JSON    ${response.content}      # Zamieniamy odpowiedź JSON na listę Pythonową
    ${count}=    Get Length    ${comments}      # Sprawdzamy długość odpowiedzi
    Log    ${count}     #logujemy długość listy
    Should Be Equal As Integers    ${count}    5        #sprawdzamy długość listy komentarzy
    FOR    ${comment}    IN    @{comments}
        Should Be Equal As Integers    ${comment}[postId]    1
    END
