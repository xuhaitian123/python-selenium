import selenium
from  selenium import webdriver
import time
import os

w = webdriver.Chrome()
w.get("http://www.baidu.com")
w.implicitly_wait(10)
w.maximize_window()
ipt = w.find_element_by_id("kw")
ipt.send_keys("1111")
time.sleep(1)
# 路径可以使用以下两种方法
# filename =  "D:\\testclass.png"
filename  =  "D:/rom_package/4-30/test.png"
try:
    picture=w.get_screenshot_as_file(filename)  
    print(picture)
    if picture == True:        
            print (picture,":截图成功！图片保存路径为：",filename)    
    else:
       print(picture,":截图失败！")
except Exception as e:
   print(e)
   w.quit()
print (os.getcwd())#获得当前工作目录
print (os.path.abspath('.'))#获得当前工作目录
print (os.path.abspath('..'))#获得当前工作目录的父目录
print (os.path.abspath(os.curdir))#获得当前工作目录

