*** Settings ***
Library     RequestsLibrary

*** Variables ***
${BASE_URL}     http://127.0.0.1:5010

*** Keywords ***
Create API Session
    Create Session      Equipment_API        ${BASE_URL}
Get ALL Equipment
    ${response}=        GET on Session       equipment_API       /api/equipment      expected_status=200 
    RETURN      ${response}  
GET Equipment by id
    [Arguments]     ${equipment_id}     ${expected_status}
    ${response}=        GET on Session       equipment_API       /api/equipment/${equipment_id}      expected_status=${expected_status} 
    RETURN      ${response}      