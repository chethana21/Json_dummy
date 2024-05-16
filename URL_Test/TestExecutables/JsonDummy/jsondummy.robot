*** Settings ***
Library    ${CURDIR}${/}..\\..\\UserFunctions\\JsonDummy\\JsondummyDataDriver.py

 
*** Test Cases ***
Check Category By Product Details
    [Documentation]    Verify if Category By Product Details returns True
    ${result}=   Compare Category By Product Details  
    Should Be True    ${result}
Check Compare Category name for product details by user
    [Documentation]    Verify if Category name for product details by user returns True
    ${result}=   Compare Categoryname For Product Details By Product   laptops  
    Should Be True    ${result}

Check Compare data by keywords
    [Documentation]    Verify if Compare data by keywords returns True
    ${result}=   Compare Data By Keywords    Apple 
    Should Be True    ${result}


Check compare created Product data
    [Documentation]    Verify if compare created product data returns True
    ${result}=    Compare Create Product Data       BMW Pencil
    Should Be True    ${result}

Check Compare Updated Product data
    [Documentation]    Verify if compare updated product data returns True
    ${result}=    Compare Update User Data       1    iPhone Galaxy +1
    Should Be True    ${result}

Check Compare Delete Product Data
    [Documentation]    Verify if compare delete product data returns True
    ${result}=    Compare Delete Product Data       1    
    Should Be True    ${result}