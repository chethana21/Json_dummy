# function.py
# try:
#     from robot.libraries.BuiltIn import BuiltIn
#     from robot.libraries.BuiltIn import _Misc
#     import robot.api.logger as logger
#     from robot.api.deco import keyword
#     ROBOT = False
# except Exception:
#     ROBOT = False   

# @keyword("CUSTOM KEYWORD TO ADD")
# def add_one_to_integer(n: int) -> int:
#     BuiltIn().log_to_console(f"input: {n}, output: {n+1}")
#     return n + 1
# *** Settings ***
# Library     func.py


# *** Test Cases ***
# Calling function from python
#     ${value}    CUSTOM KEYWORD TO ADD    ${1}
#     SHOULD BE EQUAL     ${value}         ${2}
def add_one_to_integer(n: int) -> int:
  return n + 1