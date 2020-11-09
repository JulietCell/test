*** Settings ***

Library  customer_main.py   WITH NAME  F

Library  customer_main.C1   WITH NAME  C1

Library  customer_main.C3   WITH NAME  C3

Library  customer_main.C4   WITH NAME  C4

Library  customer_main.C5   WITH NAME  C5

Library  customer_main.C6   WITH NAME  C6

Library  customer_main.C7   WITH NAME  C7

Library  customer_main.C8   WITH NAME  C8



*** Test Cases ***

添加客户 API-0151
  [Teardown]  C1.teardown

  C1.teststeps


添加客户 API-0153

  C3.teststeps


修改客户 API-0201

  C4.teststeps


修改客户 API-0202
  [Setup]     C5.setup
  [Teardown]  C5.teardown

  C5.teststeps


修改客户 API-0203
  [Setup]     C6.setup
  [Teardown]  C6.teardown

  C6.teststeps


删除客户 API-0251

  C7.teststeps


删除客户 API-0252
  [Setup]     C8.setup

  C8.teststeps
