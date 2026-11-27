*** Settings ***
Resource        C:/PythonProject/Robot_API_Project/Resources/equipment_Keyword.resource
Suite Setup     Create API Session

*** Test Cases ***
TC1_GETAll
    Log To Console    Test1 Started

    ${response}=    GET All Equipment
    ${data}=        Set Variable    ${response.json()}

    Should Be Equal As Integers    ${response.status_code}    200
    Length Should Be    ${data}    2
TC1_GETBYID
    Log To Console    Test2 Started

    ${response}=    GET Equipment by id     101     200
    ${data}=        Set Variable    ${response.json()}

    Should Be Equal As Integers    ${response.status_code}    200  

    Should Be Equal As Integers     ${data}[id]     101