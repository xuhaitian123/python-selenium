import selenium
from selenium import webdriver


w = webdriver.Chrome()
w.get("http://www.baidu.com")
print(w.get_cookies())