from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('http://www.51job.com')

inputmessage = wd.find_element_by_css_selector('.ipt #kwdselectid')
inputmessage.clear()
inputmessage.send_keys('python')
wd.find_element_by_css_selector('#work_position_click').click()

#前端加载
import time
time.sleep(2)

wd.find_element_by_css_selector('.tin > .ttag > em').click()
wd.find_element_by_css_selector('#work_position_click_center_left_each_220200').click()
wd.find_element_by_css_selector('#work_position_click_center_right_list_category_220200_080200').click()
wd.find_element_by_css_selector('#work_position_click_bottom_save').click()
wd.find_element_by_css_selector('''[onclick="kwdGoSearch($('#kwdselectid').val());"]''').click()

#获取所有职位
joblist = wd.find_elements_by_css_selector('.j_joblist div[class="e"]')
jobdict = {}

#遍历每个职位，对每个职位的元素进行处理
for i,job in enumerate(joblist):
    jobname = job.find_element_by_css_selector('.jname').text
    companyname = job.find_element_by_css_selector('.cname').text

    #裁剪信息
    places = job.find_element_by_css_selector('.info > .d').text
    place = places.split('|')[0].strip()

    salary = job.find_element_by_css_selector('.info > .sal').text
    time = job.find_element_by_css_selector('.time').text
    time = time.replace('发布','')
    jobdict[i+1] = [jobname,companyname,place,salary,time]

for k,v in jobdict.items():
    print(' | '.join(v))

wd.quit()
