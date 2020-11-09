*** Settings ***

Library  customer_main.py   WITH NAME  F

Library  customer_main.C2   WITH NAME  C2



*** Test Cases ***

添加客户 API-0152
  [Teardown]  C2.teardown

  C2.teststeps
