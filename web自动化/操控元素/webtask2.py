from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('https://y.qq.com/n/yqq/toplist/27.html#stat=y_new.toplist.menu.27')
wd.find_element_by_class_name('popup__icon_close').click()  #关闭弹出的让你下载客户端的窗口
songlist_list = wd.find_element_by_class_name('songlist__list')
lis = songlist_list.find_elements_by_tag_name('li')
message = {}
for li in lis:
    #查找歌曲的各属性信息
    songlist_rank_temp = li.find_element_by_class_name('songlist__rank').find_element_by_tag_name('i')
    songlist_rank = songlist_rank_temp.get_attribute('class')
    js_song = li.find_element_by_class_name('js_song').text
    singer_name = li.find_element_by_class_name('singer_name').text
    message[js_song] = [js_song,singer_name,songlist_rank]
print("排名上升的歌曲和演唱者信息如下")
print("------------------------\n\n")
for k,v in message.items():
    if v[2] == 'icon_rank_up':
        print('  :  '.join(v[:2]))
