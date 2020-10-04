from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
wd = webdriver.Chrome()
wd.implicitly_wait(10)

#访问网页
wd.maximize_window()
wd.get('https://kyfw.12306.cn/otn/leftTicket/init')

#出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’
fromStation = wd.find_element_by_css_selector('#fromStationText')
fromStation.click()
fromStation.send_keys('南京南\n')
toStation = wd.find_element_by_css_selector('#toStationText')
toStation.click()
toStation.send_keys('杭州东\n')

#发车时间 选 06:00--12:00
select = Select(wd.find_element_by_css_selector('#cc_start_time'))
select.select_by_visible_text('00:00--06:00')

#发车日期选当前时间的下一天
wd.find_element_by_xpath('//*[@id="date_range"]/ul/li[2]').click()

#二等座还有票的车次
xpath = '//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
elements = wd.find_elements_by_xpath(xpath)
for element in elements:
    print(element.text)
