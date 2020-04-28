from selenium.webdriver.support.select import Select
from selenium import webdriver
import time


# 以W3C下拉菜单为例
w  =  webdriver.Chrome()
# w.get("https://www.w3school.com.cn/tiy/t.asp?f=html_select")
# w.implicitly_wait(10)
# w.switch_to.frame("iframeResult")



# sel = w.find_element_by_tag_name("select")
# select = Select(sel)
# select.select_by_index(2)
# time.sleep(1)
# select.select_by_value("saab")
# time.sleep(1)
# select.select_by_visible_text("Audi")

# # 以W3C的alert为例
# w.get("https://www.w3school.com.cn/tiy/t.asp?f=hdom_alert")
# w.switch_to.frame("iframeResult")
# w.find_element_by_xpath("//input[@type='button']").click()
# alert =  w.switch_to.alert
# print(alert.text)
# time.sleep(1)
# alert.accept()
# # 拒绝
# # alert.dismiss()

# # 以W3C的confim为例
# # js='window.open("https://www.w3school.com.cn/tiy/t.asp?f=hdom_confirm");'
# # w.execute_script(js)

# w.get("https://www.w3school.com.cn/tiy/t.asp?f=hdom_confirm")
# w.switch_to.frame("iframeResult")
# w.find_element_by_xpath("//input[@type='button']").click()

# alert = w.switch_to.alert
# time.sleep(2)
# alert.dismiss()
# time.sleep(2)
# alert.accept()

# js='window.open("https://www.jianshu.com/p/3aa45532e179");'
# w.execute_script(js)
w.get("https://www.jianshu.com/p/3aa45532e179")
time.sleep(5)
js_scroll1="window.scrollTo(0,100)"
js_scroll2 = "window.scrollTo(0,document.body.scrollHeight)"
w.execute_script(js_scroll1)
time.sleep(5)
w.execute_script(js_scroll2)

time.sleep(5)
w.execute_script("window.scrollTo(0,0)")
time.sleep(2)

w.execute_script("window.open('https://www.baidu.com')")
current_handle = w.current_window_handle
print(current_handle)
w.execute_script("window.open('https://www.cnblogs.com/kuaileya/p/11905363.html')")
print(w.current_window_handle)
print(w.current_url)
print(w.window_handles)

# for a in w.window_handles:
#     if current_handle != a :
#         w.switch_to.window(a)
#         print(a)
#         time.sleep(1)
#     else:
#         break
for a in w.window_handles:
    if current_handle != a :
        print(1)
        w.switch_to_window(a)
        time.sleep(1)
    else:
        break
print("最后的页面的句柄是："+w.current_window_handle)
print(current_handle)


w.switch_to_window(current_handle)


time.sleep(5)
# w.quit()