*** Settings ***
Library    ${CURDIR}${/}..\\..\\UserFunctions\\UserDetails\\UserDetailsDataDriver.py

*** Test Cases ***
Check Compare User Count with json
    [Documentation]    Verify if compare_user_count_with_json
    ${a}=     UserDetailsDataDriver.compare_user_count_with_json
    Should Be True    ${a}

Check Compare User data with id
    [Documentation]    Verify if compare_user_data_with_id
    ${a}=     UserDetailsDataDriver.compare_user_data_with_id    4
    Should Be True    ${a}

    ${b}=     UserDetailsDataDriver.compare_user_data_with_id    12
    Should Be True    ${b}

Check Compare User data with email
    [Documentation]    Verify if compare_user_data_with_email
    ${a}=     UserDetailsDataDriver.compare_user_data_with_email    charles.morris@reqres.in
    Should Be True    ${a}

    ${b}=     UserDetailsDataDriver.compare_user_data_with_email    george.edwards@reqres.in
    Should Be True    ${b}

Check Compare Create User data
    [Documentation]    Verify if compare_create_user_data
    ${a}=    UserDetailsDataDriver.Compare Create User Data    Chinnu    H/W Engineer
    Should Be True    ${a}

Check Compare Update User data
    [Documentation]    Verify if compare_update_user_data
    ${a}=    UserDetailsDataDriver.Compare Update User Data    4    Chowdry    Software Engineer
    Should Be True    ${a} 

Check Compare Delete User data
    [Documentation]    Verify if compare_delete_user_data
    ${a}=    UserDetailsDataDriver.Compare delete User Data    4    
    Should Be True    ${a} 