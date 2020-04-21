from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# title_is：判断当前页面的title是否等于预期
# title_contains：判断当前页面的title是否包含预期字符串
# presence_of_element_located：判断某个元素是否被加到了dom树里，并不代表该元素一定可见
# visibility_of_element_located：判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
# visibility_of：跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
# presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
# text_to_be_present_in_element：判断某个元素中的text是否 包含 了预期的字符串
# text_to_be_present_in_element_value：判断某个元素中的value属性是否包含了预期的字符串
# frame_to_be_available_and_switch_to_it：判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
# invisibility_of_element_located：判断某个元素中是否不存在于dom树或不可见
# element_to_be_clickable - it is Displayed and Enabled：判断某个元素中是否可见并且是enable的，这样的话才叫clickable
# staleness_of：等某个元素从dom树中移除，注意，这个方法也是返回True或False
# element_to_be_selected：判断某个元素是否被选中了,一般用在下拉列表
# element_located_to_be_selected
# element_selection_state_to_be：判断某个元素的选中状态是否符合预期
# element_located_selection_state_to_be：跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
# alert_is_present：判断页面上是否存在alert



wb = webdriver.Chrome()
# wb = webdriver.PhantomJS()
wb.get("http://www.baidu.com")
ipt = WebDriverWait(wb, 5,1).until(EC.presence_of_element_located((By.ID, 'kw')))
ipt.send_keys("selenium")

# wb.implicitly_wait(10)#设置隐式等待最长时间10s
