from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
forecastBox = wd.find_element_by_class_name('forecastBox')
dls = forecastBox.find_elements_by_tag_name('dl')
cityweather = {}
for dl in dls:
    cityname = dl.find_element_by_tag_name('a').text
    weather = dl.find_element_by_tag_name('span').text
    cityweather[cityname] = weather

result_min = min(cityweather.values())
cities = []
for index,temperature in enumerate(cityweather.values()):
    if temperature == result_min:
        cities.append(list(cityweather.keys())[index])
print(f"气温最低为{result_min}，城市有{','.join(cities)}")
