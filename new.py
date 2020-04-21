import selenium 
import time
from selenium import webdriver
wb =  webdriver.Chrome()
wb.get("http://www.baidu.com")
# js='window.open("https://www.sogou.com");'
# wb.execute_script(js)
wb.implicitly_wait(10)
btn1 = wb.find_element_by_id("kw")
btn1.send_keys("by_id")
time.sleep(2)
btn1.clear()

# btn2 =  wb.find_elements_by_tag_name("input")
# print(len(btn2))
# time.sleep(2)
# btn2.clear()

#通过classname方式定位元素
btn3 = wb.find_element_by_class_name("s_ipt")
btn3.send_keys("by_class_name")
time.sleep(2)
btn3.clear()

# 通过属性名来定位元素
btn4 = wb.find_element_by_name("wd")
btn4.send_keys("selenium")
time.sleep(2)
 

# 通过id来定位元素
b5 = wb.find_element_by_id("su")
b5.click()
time.sleep(3)

# 通过链接文本来定位，全匹配
b6 = wb.find_element_by_link_text("知道")
print(b6)
# b6.click()


# 通过链接文本来定位，模糊匹配
wb.find_element_by_partial_link_text("知").click()

# 通过xpath来匹配元素  可以是属性名，id，类名等等
b7 = wb.find_element_by_xpath("//input[@name='word']")
b7.clear()
b7.send_keys("selenium")
wb.find_element_by_xpath("//button[@type='submit']").click()

# 通过css元素选择来定位元素
wb.find_element_by_css_selector("#ask-btn-new").click()
wb.find_element_by_css_selector("#title-area").send_keys("通过id获取元素")
wb.find_element_by_css_selector("textarea[placeholder='一句话完整的描述你的问题']").send_keys("通过属性定位")
wb.find_element_by_css_selector("div #content-area").send_keys("层级选择器定位")



# 浏览器方法
# 1. maximize_window()                最大化 --> 模拟浏览器最大化按钮
# 2. set_window_size(100,100)            浏览器大小 --> 设置浏览器宽、高(像素点)
# 3. set_window_position(300,200)     浏览器位置 --> 设置浏览器位置
# 4. back()                             后退 --> 模拟浏览器后退按钮
# 5. forward()                         前进 --> 模拟浏览器前进按钮
# 6. refresh()                         刷新 --> 模拟浏览器F5刷新
# 7. close()                            关闭 --> 模拟浏览器关闭按钮(关闭单个窗口)
# 8. quit()   

# 其他常用方法
# 1. size                 返回元素大小
# 2. text                 获取元素的文本
# 3. title                 获取页面title
# 4. current_url            获取当前页面URL
# 5. get_attribute()         获取属性值
# 6. is_display()            判断元素是否可见
# 7. is_enabled()            判断元素是否可用


print(wb.find_element_by_css_selector("[class='qd-ct qd-title']").size)
print(wb.find_element_by_css_selector(".qd-ct.qd-title").size)
# wb.find_element_by_css_selector("[class='qd-content'] div textarea").send_keys("1111111111111")
print(wb.find_element_by_css_selector("[class='qd-content'] div textarea").size)
print("-------------------------")
print(wb.find_element_by_id("content-area").text)  #获取不到文本内容，用下面的方式
print(wb.find_element_by_id("content-area").get_attribute("value"))
print(wb.find_element_by_css_selector("[class='qd-content'] div textarea").get_attribute("value"))


time.sleep(5)





















time.sleep(3)
handles  = wb.window_handles
print(handles)
print("当前窗口的title是" + wb.title)

time.sleep(3)
wb.close()

# wb.get_screenshot_as_file("E:\自己学习文件夹\web_driver_image\test.png")

