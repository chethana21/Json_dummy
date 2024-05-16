*** Settings ***
Library    ${CURDIR}${/}..\\..\\UserFunctions\\RestCountries\\RestCountriesDataDriver.py

 
*** Test Cases ***
Check Compare Common Name Count with JSON
    [Documentation]    Verify if compare_common_name_count_with_json returns True
    ${result}=   compare_common_name_count_with_json   
    Should Be True    ${result}

Check Compare with regions
    [Documentation]    Verify if compare_with_regions
    ${a}=    RestCountriesDataDriver.Compare With Regions    Asia
    Should Be True    ${a}
    ${b}=    RestCountriesDataDriver.Compare With Regions    Oceania
    Should Be True    ${b}

Check Compare with subregions
    [Documentation]    Verify if compare_with_subregions
    ${a}=    RestCountriesDataDriver.Compare With subregions   Central America
    Should Be True    ${a}
    ${b}=    RestCountriesDataDriver.Compare With subregions    Micronesia
    Should Be True    ${b}

Check Compare Unique regions
    [Documentation]    Verify if compare_unique_regions
    ${result}=    RestCountriesDataDriver.Compare Unique Regions   
    Should Be True    ${result}

Check Compare Unique subregions
    [Documentation]    Verify if compare_unique_subregions
    ${result}=    RestCountriesDataDriver.Compare Unique subregions   
    Should Be True    ${result}

Check Compare common name country
    [Documentation]    Verify if compare_common_name_country
    ${a}=    RestCountriesDataDriver.compare_common_name_country   Palestine
    Should Be True    ${a}
    ${b}=    RestCountriesDataDriver.compare_common_name_country   North Macedoni
    Should Be True    ${b}
    ${c}=    RestCountriesDataDriver.compare_common_name_country   Lebanon
    Should Be True    ${c}