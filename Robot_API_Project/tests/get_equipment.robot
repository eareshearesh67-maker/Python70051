*** Settings ***
Library     RequestsLibrary

*** Variables ***
${BASE_URL}     http://127.0.0.1:5010

*** Keywords ***
Create API Session
    Create Session      Equipment_API        ${BASE_URL}

*** Test Cases ***
TC001_Test Get ALL Equipment
    Create API Session
    ${response}=        GET On Session     Equipment_API       /api/equipment
    Should Be Equal As Integers        ${response.status_code}     200
    Log To Console     ${response.json()}
TC002_Test Get ALL Equipment
    Create API Session
    ${response}=        GET On Session     Equipment_API       /api/equipment/101
    Should Be Equal As Integers        ${response.status_code}     200
    ${data}=        set Variable        ${response.json()}
    Should Be Equal As Integers     ${data}[id]     101
    Should Be Equal As Strings     ${data}[name]   Flight control unit
    Should Be Equal As Strings     ${data}[type]   FCU 
    Should Be Equal As Strings     ${data}[status]   Operational                                         
    Log To Console     ${response.json()} 
