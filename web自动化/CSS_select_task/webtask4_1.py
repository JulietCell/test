from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)

#访问网页
wd.get('http://quote.eastmoney.com/stock_list.html')

#循环10次，获取10页
for i in range(10):
    stockmessage = {}
    stocknames = wd.find_elements_by_css_selector('#table_wrapper-table .odd td:nth-child(3) , #table_wrapper-table .even td:nth-child(3) ')
    stocknums = wd.find_elements_by_css_selector('#table_wrapper-table .odd td:nth-child(2) , #table_wrapper-table .even td:nth-child(2) ')
    for j,stocknum in enumerate(stocknums):
        stockmessage[stocknum.text] = stocknames[j].text
    with open("stock.txt","a",encoding="utf-8") as f:   #追加形式打开
        content = f"\n第{i+1}页的信息\n\n"
        for k,v in stockmessage.items():
            content += f'{k} : {v}\n'
        f.write(content)
    wd.find_element_by_css_selector('.next').click()
    import time
    time.sleep(1)
wd.quit()







