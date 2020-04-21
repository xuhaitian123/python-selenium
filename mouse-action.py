from selenium.webdriver.common.action_chains import ActionChains
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 鼠标事件
# 1. context_click()            右击 --> 此方法模拟鼠标右键点击效果
# 2. double_click()            双击 --> 此方法模拟双标双击效果
# 3. drag_and_drop()            拖动 --> 此方法模拟双标拖动效果
# 4. move_to_element()        悬停 --> 此方法模拟鼠标悬停效果
# 5. perform()                执行 --> 此方法用来执行以上所有鼠标方法

wb =  webdriver.Chrome()
wb.get("http://www.baidu.com")
wb.implicitly_wait(5)
wb.find_element_by_id("kw").send_keys("selenium")
sub = wb.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
ActionChains(wb).context_click(sub).perform()
sub1 = wb.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
ActionChains(wb).double_click(sub1).perform()

# 键盘事件
# 1. send_keys(Keys.BACK_SPACE)删除键（BackSpace） 
# 2. send_keys(Keys.SPACE)空格键(Space) 
# 3. send_keys(Keys.TAB)制表键(Tab) 
# 4. send_keys(Keys.ESCAPE)回退键（Esc） 
# 5. send_keys(Keys.ENTER)回车键（Enter） 
# 6. send_keys(Keys.CONTROL,'a') 全选（Ctrl+A） 
# 7. send_keys(Keys.CONTROL,'c')复制（Ctrl+C）

wb.find_element_by_id("su").send_keys(Keys.ENTER)
wb.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
wb.find_element_by_id("kw").send_keys(Keys.CONTROL,"c")
