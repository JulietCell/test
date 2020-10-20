from hyrobot.common import *
from selenium import webdriver
import time

#打开浏览器
def open_browser():
    print('打开浏览器1')
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)

    #使用hyrobot全局存储对象 GSTORE
    GSTORE['global_webdriver'] = wd
    return wd

#获取 全局使用的webdriver对象
def get_lobal_webdriver():
    return GSTORE['global_webdriver']

#登录进去
def mgr_login(wd):
    wd.get("http://127.0.0.1/mgr/sign.html")
    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')
    wd.find_element_by_class_name('btn-primary').click()

def clickMenu(wd,menuName):
    #找到所有菜单元素
    menus = wd.find_elements_by_css_selector('.sidebar-menu li a[href] span')
    #根据判断点击对应订单
    if menuName == '客户':
        menus[0].click()
    if menuName == '药品':
        menus[1].click()
    if menuName == '订单':
        menus[2].click()
    if menuName == '其它菜单':
        menus[3].click()

def clear_all_message(wd):
    #find_elements的方法查找元素，就算元素找不到，也不会报错，不会抛出异常，从而不影响后面的执行。
    # 找到所有菜单元素
    menus = wd.find_elements_by_css_selector('.sidebar-menu li a[href] span')
    #必须先清除订单信息，否则有依赖的客户和药品无法删除
    #清除订单信息
    menus[2].click()
    #获取删除按钮元素
    clear_elements = wd.find_elements_by_css_selector('.search-result-item .btn-xs')
    #根据xpath选择
    #clear_elements = wd.find_elements_by_css_selector('//*[@type="button"][2]')
    for clear_element in clear_elements:
        clear_element.click()
        #Confirm框
        wd.switch_to.alert.accept()

    #清除客户信息
    menus[0].click()
    #获取删除按钮元素
    clear_elements = wd.find_elements_by_css_selector('.search-result-item .btn-xs:nth-child(2)')
    #根据xpath选择
    #clear_elements = wd.find_elements_by_css_selector('//*[@type="button"][2]')
    for clear_element in clear_elements:
        clear_element.click()
        #Confirm框
        wd.switch_to.alert.accept()

    #清除药品信息
    menus[1].click()
    #获取删除按钮元素
    clear_elements = wd.find_elements_by_css_selector('.search-result-item .btn-xs:nth-child(2)')
    #根据xpath选择
    #clear_elements = wd.find_elements_by_css_selector('//*[@type="button"][2]')
    for clear_element in clear_elements:
        clear_element.click()
        # Confirm框
        wd.switch_to.alert.accept()


