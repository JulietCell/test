from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('http://www.51job.com')

#点击高级搜索
wd.find_element_by_css_selector('a.more').click()
wd.find_element_by_css_selector('.d_lt #kwdselectid').send_keys('python')
wd.find_element_by_css_selector('.d_lt p em.dicon').click()

import time
time.sleep(2)

#关键字
#清空当前已经选择的城市，并选择杭州
# wd.find_element_by_css_selector('.ipt #kwdselectid').send_keys('python')
select_places = wd.find_elements_by_css_selector('#work_position_click_multiple span span')
for select_place in select_places:
    select_place.click()
wd.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_080200').click()
wd.find_element_by_css_selector('#work_position_click_bottom_save').click()

time.sleep(2)
#职能类型
wd.find_element_by_css_selector('.b_key').click()   #下拉菜单缩回
wd.find_element_by_css_selector('span[class="ic i_add"]').click()
wd.find_element_by_css_selector('#funtype_click_center_left_each_0100').click()
wd.find_element_by_css_selector('#funtype_click_center_right_list_category_0100_0100').click()
wd.find_element_by_css_selector('.funtype_click_center_right_list_sub_category span:nth-child(2)').click()
wd.find_element_by_css_selector('#funtype_click_bottom_save').click()

#6个可选项
values = wd.find_elements_by_css_selector('span[class="ic i_arrow"]')
values[0].click()
time.sleep(2)
wd.find_element_by_css_selector('[data-value="10"]').click()
values[1].click()
time.sleep(2)
wd.find_element_by_css_selector('[title="1-3年"]').click()
wd.find_element_by_css_selector('.btnbox > span').click()

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