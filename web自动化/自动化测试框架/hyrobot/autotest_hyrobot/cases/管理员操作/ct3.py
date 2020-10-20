from lib.webui import *
import time
from hyrobot.common import *

class C6():
    name = '管理员操作 UI-0107'
    tags = ['xx']

    def teststeps(self):
        wd = get_lobal_webdriver()

        STEP(1,'在系统中添加3种药品')
        clickMenu(wd,'药品')
        wd.find_element_by_css_selector('.add-one-area>.btn').click()
        #创建第一个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('青霉素盒装1')
        medicines_messages[1].send_keys('YP-32342341')
        medicines_messages[2].send_keys('青霉素注射液，每支15ml，20支装')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        # 创建第二个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('青霉素盒装2')
        medicines_messages[1].send_keys('YP-32342342')
        medicines_messages[2].send_keys('青霉素注射液，每支15ml，30支装')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        # 创建第二个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('青霉素盒装3')
        medicines_messages[1].send_keys('YP-32342343')
        medicines_messages[2].send_keys('青霉素注射液，每支15ml，40支装')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        clicks[1].click()  # 点击取消，收起窗口
        time.sleep(2)

        STEP(2, '获取药品中的信息')
        elements = wd.find_elements_by_css_selector('.container-fluid .search-result-item span:nth-child(2)')
        message = []
        for element in elements:
            message.append(element.text)

        STEP(3, '检查药品信息是否正确')
        INFO(message[:9])
        CHECK_POINT('检查药品信息', message[:9] == ['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装'
                                              ,'青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'
                                              ,'青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'])

class C7():
    name = '管理员操作 UI-0108'
    tags = ['cc']

    # 初始化清除，前置条件，系统中没有订单、客户和药品，如果有，点击删除按钮删除掉。
    def setup(self):
        wd =get_lobal_webdriver()
        clear_all_message(wd)

    def teststeps(self):
        wd = get_lobal_webdriver()

        #在系统中添加3种药品
        STEP(1, '在系统中添加3种药品')
        clickMenu(wd, '药品')
        wd.find_element_by_css_selector('.add-one-area>.btn').click()
        # 创建第一个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('青霉素盒装1')
        medicines_messages[1].send_keys('YP-32342341')
        medicines_messages[2].send_keys('青霉素注射液，每支15ml，20支装')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        # 创建第二个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('青霉素盒装2')
        medicines_messages[1].send_keys('YP-32342342')
        medicines_messages[2].send_keys('青霉素注射液，每支15ml，30支装')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        # 创建第二个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('青霉素盒装3')
        medicines_messages[1].send_keys('YP-32342343')
        medicines_messages[2].send_keys('青霉素注射液，每支15ml，40支装')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        clicks[1].click()  # 点击取消，收起窗口
        time.sleep(2)

        #系统中添加3个客户
        STEP(2,'系统中添加3个客户')
        clickMenu(wd,'客户')
        wd.find_element_by_css_selector('.add-one-area>.btn').click()
        # 创建第一个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('南京中医院1')
        medicines_messages[1].send_keys('2551867851')
        medicines_messages[2].send_keys('江苏省-南京市-秦淮区-汉中路-501')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        # 创建第二个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('南京中医院2')
        medicines_messages[1].send_keys('2551867852')
        medicines_messages[2].send_keys('江苏省-南京市-秦淮区-汉中路-502')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        # 创建第二个
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('南京中医院3')
        medicines_messages[1].send_keys('2551867853')
        medicines_messages[2].send_keys('江苏省-南京市-秦淮区-汉中路-504')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建

        clicks[1].click()  # 点击取消，收起窗口
        time.sleep(2)

        STEP(3,'进入订单管理界面，添加一个订单')
        clickMenu(wd,'订单')
        wd.find_element_by_css_selector('.add-one-area>.btn').click()
        wd.find_element_by_css_selector('.form-control:nth-of-type(1)').send_keys('订单1')
        select_elements = wd.find_elements_by_css_selector('.add-one-area select')

        from selenium.webdriver.support.ui import Select
        Select(select_elements[0]).select_by_visible_text('南京中医院2')
        Select(select_elements[1]).select_by_visible_text('青霉素盒装1')
        wd.find_element_by_css_selector('.add-one-area [type="number"]').send_keys('100')

        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建
        clicks[1].click()  # 点击取消，收起窗口
        time.sleep(2)

        STEP(4,'获取添加的订单信息')
        elements = wd.find_elements_by_css_selector('.search-result-item-field span:nth-child(2),.search-result-item-field p')
        order_message = []
        for element in elements:
            order_message.append(element.text)

        STEP(5,'检查订单信息是否正确')
        INFO(order_message)
        CHECK_POINT('检查订单信息',order_message == ['订单1',order_message[1],'南京中医院2','青霉素盒装1 * 100'])



