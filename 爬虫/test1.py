import selenium
from selenium import webdriver
wb =  webdriver.Chrome()
wb.get("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%B1%BD%E8%BD%A6")

img = wb.find_elements_by_tag_name("img")


for imgSrc in img:
    print(imgSrc.get_attribute('src'))
print(len(img))