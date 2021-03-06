#coding:utf-8
from selenium import webdriver

import unittest
import time

from HTMLTestRunner import HTMLTestRunner
class MyTest2(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
    def test_baidu(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title=driver.title
        self.assertEqual(title,"unittest_百度搜索")
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    
    testunit=unittest.TestSuite()
    testunit.addTest(MyTest2("test_baidu"))
    fp=open('D:\\eclipse\\eclipse-workspace\\unittestdemo4\\test_project\\report\\result.html','wb')
    runner=HTMLTestRunner(stream=fp,title='搜索功能测试',description='用例执行情况')
    runner.run(testunit)
    fp.close()
    