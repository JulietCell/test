from lib.webui import *
import time
from hyrobot.common import *

class C1:
    name = '管理员操作 UI-0101'
    def teststeps(self):
        wd = get_lobal_webdriver()
        STEP(1,'获取左侧菜单信息')
        ul = wd.find_element_by_class_name('sidebar-menu')
        spans = ul.find_elements_by_tag_name('span')
        title = []
        for span in spans:
            title.append(span.text)

        STEP(2,'检查左侧菜单是否正确')
        CHECK_POINT('左侧菜单',title[:3] == ['客户','药品','订单'])

class C2:
    name = '管理员操作 UI-0102'
    def teststeps(self):
        wd = get_lobal_webdriver()
        STEP(1,'点击添加客户，输入客户名为 南京第二中医院 的客户')
        time.sleep(2)   #等待前端数据稳定
        wd.find_element_by_css_selector('.add-one-area>.btn').click()
        custom_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        custom_messages[0].send_keys('南京第二中医院')
        custom_messages[1].send_keys('88888888')
        custom_messages[2].send_keys('江苏省-南京市-秦淮区-汉中路-500')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()
        clicks[1].click()
        time.sleep(2)
        elements = wd.find_elements_by_css_selector('.container-fluid .search-result-item span:nth-child(2)')
        message = []
        for element in elements:
            message.append(element.text)

        STEP(2,'检查是否正确')
        CHECK_POINT('检查客户信息',message[:3] == ['南京第二中医院','88888888','江苏省-南京市-秦淮区-汉中路-500'])


