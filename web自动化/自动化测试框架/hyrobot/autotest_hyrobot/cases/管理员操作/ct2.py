from lib.webui import *
import time
from hyrobot.common import *

class C3():
    name = '管理员操作 UI-0103'
    def teststeps(self):
        wd = get_lobal_webdriver()

        STEP(1,'添加 南京中医院 的客户')
        # 添加客户
        wd.find_element_by_css_selector('.add-one-area>.btn').click()
        custom_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        custom_messages[0].send_keys('南京中医院')
        custom_messages[1].send_keys('88888888')
        custom_messages[2].send_keys('江苏省-南京市-秦淮区-汉中路-500')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()   #点击创建
        clicks[1].click()   #点击取消，收起窗口
        time.sleep(1)

        STEP(2,'获取第一项结果中的信息')
        elements = wd.find_elements_by_css_selector('.container-fluid .search-result-item span:nth-child(2)')
        message = []
        for element in elements:
            message.append(element.text)

        STEP(3,'检查第一次添加客户后，信息是否正确')
        CHECK_POINT('检查客户信息',message[:3] == ['南京中医院','88888888','江苏省-南京市-秦淮区-汉中路-500'])

        STEP(4,'修改客户名称为 南京省中医院')
        wd.find_element_by_css_selector('.search-result-item .btn-xs').click()
        a = wd.find_element_by_css_selector('[style="margin-top: 1em;"]>.form-control')
        a.clear()
        a.send_keys('南京省中医院')
        wd.find_element_by_css_selector('.search-result-item .btn-xs').click()

        STEP(5, '获取修改信息后第一项结果中的信息')
        time.sleep(2)   #必加
        elements = wd.find_elements_by_css_selector('.container-fluid .search-result-item span:nth-child(2)')
        message = []
        for element in elements:
            message.append(element.text)

        STEP(5,'检查修改后的信息是否正确')
        CHECK_POINT('检查客户信息',message[:3] == ['南京省中医院','88888888','江苏省-南京市-秦淮区-汉中路-500'])

class C4():
    name = '管理员操作 UI-0105'

    def teststeps(self):
        wd = get_lobal_webdriver()

        STEP(1,'添加药品')
        wd.find_element_by_css_selector('a[href="#/medicines"] span').click()
        wd.find_element_by_css_selector('.add-one-area>.btn').click()
        medicines_messages = wd.find_elements_by_css_selector('.col-lg-8 .form-control')
        medicines_messages[0].send_keys('阿莫西林胶囊')
        medicines_messages[1].send_keys('123456')
        medicines_messages[2].send_keys('一种青霉素类抗生素')
        clicks = wd.find_elements_by_css_selector('.col-lg-12 .btn-xs')
        clicks[0].click()  # 点击创建
        clicks[1].click()  # 点击取消，收起窗口
        time.sleep(1)

        STEP(2,'获取第一个药品中的元素')
        elements = wd.find_elements_by_css_selector('.container-fluid .search-result-item span:nth-child(2)')
        message = []
        for element in elements:
            message.append(element.text)

        STEP(3,'检查药品信息是否正确')
        CHECK_POINT('检查药品信息',message[:3] == ['阿莫西林胶囊','123456','一种青霉素类抗生素'])

class C5():
    name = '管理员操作 UI-0106'
    tags = ['hh']
    def teststeps(self):
        wd = get_lobal_webdriver()

        STEP(1,' 点击页脚处 链接 白月黑羽教学使用，点击访问官网')
        # 点击页脚处 链接 白月黑羽教学使用，点击访问官网
        main_windos = wd.current_window_handle
        wd.find_element_by_css_selector('.pull-right [target="_blank"]').click()

        STEP(2,'获取 页眉导航菜单中所有教程类目')
        # 确认用新窗口访问
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
            if 'Python' in wd.title:
                break
        wd.maximize_window()
        time.sleep(2)
        items = wd.find_elements_by_css_selector('.main-menu-item .nav-item span')
        class_name = []
        for item in items:
            class_name.append(item.text)

        STEP(3,'检查导航菜单名是否正确')
        CHECK_POINT('检查导航菜单中所有教程类目',
                    class_name == ['Python基础', 'Python进阶', '图形界面', 'Web开发', '自动化测试', '性能测试', '常见问题', '其它'])

        STEP(4,'回到 白月SMS系统网页，点击退出登录')
        # 回到原来的窗口
        wd.close()
        wd.switch_to.window(main_windos)
        wd.find_element_by_css_selector('.dropdown-toggle .hidden-xs').click()
        wd.find_element_by_css_selector('.pull-right .btn-default').click()
        time.sleep(2)   #必加

        STEP(5,'检查是否回到了登录界面')
        url = wd.current_url
        INFO(print(url))
        CHECK_POINT('检查是否退出',url == 'http://127.0.0.1/mgr/sign.html')

        STEP(6,'重新登录')
        mgr_login(wd)







