*** Settings ***
Documentation     Test metody PUT
Library           RequestsLibrary
Library           Collections

*** Test Cases ***
Aktualizacja istniejącego posta (PUT)
    [Documentation]  Test wysyła PUT aby zmienić tytuł posta i sprawdzić odpowiedź
    ${update_data}=     Create Dictionary    Id=1   title=Zaktualizowany tytuł  body=Zmieniona treść    userId=1
    ${response}=    PUT     http://jsonplaceholder.typicode.com/posts/1     json=${update_data}
    ${updated}=     Evaluate    json.loads("""${response.text}""")    json
    ShoulD Be Equal  ${updated}[title]   Zaktualizowany tytuł
    ShoulD Be Equal  ${updated}[body]   Zmieniona treść
    ShoulD Be Equal As Integers  ${updated}[userId]     1
    ShoulD Be Equal As Integers  ${updated}[id]     1