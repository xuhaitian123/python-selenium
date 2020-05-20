from appium import webdriver
import os
# 导入time
import time
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android' #平台名称
desired_caps['platformVersion'] = '10'  #平台版本
desired_caps['deviceName'] = 'cc79006d' #设备号
# app信息
desired_caps['appPackage'] = 'com.android.settings' #应用的包名
desired_caps['appActivity'] = '.Settings' #代表启动的activity
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #声明driver对象,让手机完成脚本操作

# driver.press_keycode(26)
driver.find_element_by_name("我的设备").click()
# driver.find_element_by_id("com.baidu.yuedu:id/tab_search").click()
print(driver.current_context)
driver.press_keycode(3)


# time.sleep(5)
# 关闭app driver对象不会关闭
# driver.close_app()
#关闭驱动对象
# driver.quit()