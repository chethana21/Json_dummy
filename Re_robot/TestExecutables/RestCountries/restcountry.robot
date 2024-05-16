# *** Settings ***
# Library    Process

# *** Test Cases ***
# Verify Common Name Count with JSON
#     [Documentation]    Test the RestCountriesDataDriver class
#     [Tags]    regression
#     ${api_url}     Set Variable     https://restcountries.com/v3.1
#     ${json_file_path}    Set Variable    restcountry.json
#     ${output}    Run Process     python     ${CURDIR}RestCountriesDataDriver.py    ${api_url}    ${json_file_path}    --loglevel    NONE
#     Should be Equal    ${output}    True
    # ${data_driver}    Create RestCountriesDataDriver    ${api_url}    ${json_file_path}
    # ${result}    Call Method    ${data_driver}    compare_common_name_count_with_json
    # Should Be True    ${result}
# Compare Common Name Count with JSON
#     [Arguments]    ${data_driver}
#     ${output} =    Call Method    ${data_driver}    compare_common_name_count_with_json
#     [Return]    ${output}
# *** Keywords ***
# Create Rest Countries Data Driver
#     [Arguments]    ${api_url}    ${json_file_path}
#     ${output}    Run Keyword And Return    Main    ${api_url}    ${json_file_path}
#     [Return]    ${output}
 
# Main
#     [Arguments]    ${api_url}    ${json_file_path}
#     ${output}        Run Process     python     RestCountriesDataDriver.py    ${api_url}    ${json_file_path}    --loglevel    NONE
#     [Return]    ${output}




# *** Settings ***
# Library    OperatingSystem
# Library    Collections
# Library    RequestsLibrary
# Library    JSONLibrary
 
# *** Test Cases ***
# Verify Common Name Count with JSON
#     ${api_url}     Set Variable     https://restcountries.com/v3.1
#     ${json_file_path}    Set Variable    restcountry.json
#     ${data_driver}    Create RestCountriesDataDriver    ${api_url}    ${json_file_path}
#     ${result}    Compare Common Name Count with JSON    ${data_driver}
#     Should Be True    ${result}
 
# *** Keywords ***
# Create RestCountriesDataDriver
#     [Arguments]    ${api_url}    ${json_file_path}
#     ${data_driver} =    RestCountriesDataDriver    ${api_url}    ${json_file_path}
#     [Return]    ${data_driver}
 
# Compare Common Name Count with JSON
#     [Arguments]    ${data_driver}
#     ${output} =    Call Method    ${data_driver}    compare_common_name_count_with_json
#     [Return]    ${output}



# *** Settings ***
# Library    ${CURDIR}/RestCountriesDataDriver.py 
  
# ...  # Replace URL and path
 
# *** Keywords ***
# Create RestCountriesDataDriver
#     [Arguments]    ${https://restcountries.com/v3.1}    ${restcountry.json}
    

# *** Test Cases ***
# Test RestCountriesDataDriver Functionality
#     [Documentation]    Test the functionality of RestCountriesDataDriver class
#     [Tags]    RestCountriesDataDriver
#     ${driver}    Create RestCountriesDataDriver    https://restcountries.com/v3.1    restcountry.json 

#     ${result}    ${status_code}    RestCountriesDataDriver.compare_common_name_count_with_json
#     Should Be Equal As Integers    ${status_code}    200
#     Should Be True    ${result}
 
# *** Keywords ***
# Create RestCountriesDataDriver
#     [Arguments]    ${api_url}    ${json_file_path}
#     ${driver} =    RestCountriesDataDriver    ${api_url}    ${json_file_path}
#     [Return]    ${driver}

# *** Settings ***
# Library    RestCountriesDataDriver
 
# *** Variables ***
# ${api_url}     https://restcountries.com/v3.1  # Replace with your actual API URL
 
# *** Test Cases ***
# Check Compare Common Name Count with JSON
#     [Documentation]    Verify if compare_common_name_count_with_json returns True
#     ${result}=    Compare Common Name Count with JSON Result    ${api_url}
#     Should Be True    ${result}
#     Log    The result is: ${result}
 
# *** Keywords ***
# Compare Common Name Count with JSON Result
#     [Arguments]    ${api_url}
#     #${restcountries_data}=    Create RestCountriesDataDriver    ${api_url}
#     ${result}=    RestCountriesDataDriver.compare_common_name_count_with_json
#     [Return]    ${result}\


*** Settings ***
Library    ${CURDIR}${/}..\\..\\UserFunctions\\RestCountries\\RestCountriesDataDriver.py

 
*** Test Cases ***
Check Compare Common Name Count with JSON
    [Documentation]    Verify if compare_common_name_count_with_json returns True
    ${result}=    RestCountriesDataDriver.compare_common_name_count_with_json   
    Should Be True    ${result}
  #  [Teardown]    ${result}
 
# *** Keywords ***
# Compare Common Name Count with JSON Result
#    # [Arguments]    ${api_url}
#     #${restcountries_data}=    Create RestCountriesDataDriver    ${api_url}
#     ${result}=    RestCountriesDataDriver.compare_common_name_count_with_json
#     [Return]    ${result}

 #C:/Users/Administrator/OneDrive - Wipro/Fujitsu/Re_robot/UserFunctions/RestCountries/RestCountriesDataDriver.py    https://restcountries.com/v3.1    C:/Users/Administrator/OneDrive - Wipro/Fujitsu/Re_robot/TestExecutables/RestCountries/restcountry.json 
...   # https://restcountries.com/v3.1    ../TestExecutables/RestCountries/restcountry.json   
# ...    ../UserFunctions/Restcountries/RestcountriesDataDriven.py    https://restcountries.com/v3.1    TestExecutables/RestCountries/restcountry.json
# "C:/Users/Administrator/OneDrive - Wipro/Fujitsu/Re_robot/UserFunctions/RestCountries/RestCountriesDataDriver.py"
#${EXECDIR}${/}..\\Resource\\MyProfile.txt
#Variables    ../TestExecutables/YourJsonFile.json
# *** Variables ***
# ${api_url}     https://restcountries.com/v3.1  # Replace with your actual API URL