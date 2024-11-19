*** Settings ***
Library    grocery_store_api_automation.py

*** Test Cases ***
Get Auth Token Test
    ${response} =    Get Auth Token
    #Should Be Equal As Strings    ${response.status_code}    200
    Log To Console    Response: ${response}

Create Booking Test
    ${response} =    Create Booking
    Log To Console    Response: ${response}