*** Settings ***
Library     func.py


*** Test Cases ***
Calling function from python
    ${value}    func.Add One To Integer ${1}
    SHOULD BE EQUAL     ${value}         ${2}