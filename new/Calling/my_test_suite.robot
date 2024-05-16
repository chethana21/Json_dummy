*** Settings ***
Library    ../MAIN/MyLibrary.py    # Import the Python library by specifying the path

*** Test Cases ***
Increment Value and Get It
    [Documentation]    Test incrementing and getting a value
    [Tags]    example
    MyLibrary.Increment Value
    ${value}    MyLibrary.Get Value
    Should Be Equal As Integers    ${value}    1


*** Keywords ***
MyLibrary.Increment Value
    [Documentation]    Increment the value
    Set Global Variable    ${value}    0  # Initialize the variable to 0
    ${new_value}    Evaluate    ${value} + 1
    Set Global Variable    ${value}    ${new_value}  # Update the value

MyLibrary.Get Value
    [Documentation]    Get the value
    [Return]    ${value}



