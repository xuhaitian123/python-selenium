import unittest
from selenium import webdriver
import time


class TestUnittest(unittest.TestCase):
    def setUp(self):
        self.wb =  webdriver.Chrome()
        self.wb.get("http://www.baidu.com")
        self.wb.implicitly_wait(10)
        self.wb.maximize_window()
        print("setUp")
    def testClick(self):
        self.wb.find_element_by_id("kw").send_keys("1111111111111111111")
        print("测试case")
        time.sleep(3)
    def tearDown(self):
        time.sleep(3)
        self.wb.quit()
        print("end")
if __name__ == "__main__":
    unittest.main()
