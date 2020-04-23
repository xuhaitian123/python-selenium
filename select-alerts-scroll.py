from selenium.webdriver.support.select import Select
from selenium import webdriver
import time


# 以W3C下拉菜单为例
w  =  webdriver.Chrome()
w.get("https://www.w3school.com.cn/tiy/t.asp?f=html_select")
w.implicitly_wait(10)
w.switch_to_frame("iframeResult")
sel = w.find_element_by_tag_name("select")
select = Select(sel)
select.select_by_index(2)
time.sleep(1)
select.select_by_value("saab")
time.sleep(1)
select.select_by_visible_text("Audi")

# 以W3C的alert为例
w.get("https://www.w3school.com.cn/tiy/t.asp?f=hdom_alert")
w.switch_to_frame("iframeResult")
w.find_element_by_xpath("//input[@type='button']").click()
alert =  w.switch_to_alert()
print(alert.text)
time.sleep(1)
alert.accept()
# 拒绝
# alert.dismiss()

# 以W3C的confim为例
# js='window.open("https://www.w3school.com.cn/tiy/t.asp?f=hdom_confirm");'
# w.execute_script(js)

w.get("https://www.w3school.com.cn/tiy/t.asp?f=hdom_confirm")
w.switch_to_frame("iframeResult")
w.find_element_by_xpath("//input[@type='button']").click()

alert = w.switch_to_alert()
time.sleep(2)
alert.dismiss()
time.sleep(2)
alert.accept()









time.sleep(5)
w.quit()