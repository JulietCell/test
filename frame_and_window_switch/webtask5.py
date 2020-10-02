from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(5)
import time
import traceback
import csv

#打开网页进行选择
wd.maximize_window()
wd.get('http://www.51job.com')
wd.find_element_by_css_selector('.ipt #kwdselectid').send_keys('python')
wd.find_element_by_css_selector('#work_position_input').click()
time.sleep(2)
wd.find_element_by_css_selector('.tin span em').click()
wd.find_element_by_css_selector('#work_position_click_center_right_list_000000 table tbody tr:nth-child(1) .js_more:nth-child(2) em').click()
wd.find_element_by_css_selector('#work_position_click_bottom_save').click()
wd.find_element_by_css_selector('.bar button[onclick]')
wd.find_element_by_css_selector('.ush button ').click()

#进入到搜索内容，对所搜索的内容进行操作
#循环10次，取前2页数据
wd.find_element_by_css_selector('.tleft span:nth-child(3)').click() #点击最新发布
title = ['岗位名称','薪资','岗位要求与介绍','职位信息描述']
message =[]
for i in range(2):
    time.sleep(2)
    jobs = wd.find_elements_by_css_selector('.j_joblist .e')
    main_window = wd.current_window_handle
    for job in jobs:
        #获取职位名称
        job_name = job.find_element_by_css_selector('.t span[title]').text
        job_sal = job.find_element_by_css_selector('.sal').text
        job_experence = job.find_element_by_css_selector('.info .d').text
        job.click()
        # 确认新窗口访问
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
            if '前程无忧' in handle.title():
                break
        #职位描述信息可能有两种元素的情况
        stat = False
        try:
            job_describe = wd.find_element_by_css_selector('.tBorderTop_box').text
        except:
            print(traceback.format_exc())
            stat = True
        #如果上面的元素找不到，则用下面的方法查找
        if stat:
            job_describe = wd.find_element_by_css_selector('.jcon').text
        #信息集写入
        message.append([job_name,job_sal,job_experence,job_describe])

        #关闭当前窗口，并且切换句柄
        wd.close()
        wd.switch_to.window(main_window)

    #点击下一页
    wd.find_element_by_css_selector('.next a').click()
wd.quit()

#csv格式保存
with open('message.csv','w') as f :
    writer = csv.writer(f)
    writer.writerow(title)
    writer.writerows(message)


#文件格式保存
# with open('message.txt','w',encoding='utf-8') as f :
#     f.write('|n\t'.join(title)+'\n')
#     for mes in message:
#         f.write('|\t'.join(mes)+'\n')



