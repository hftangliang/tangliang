#coding:utf-8
import unittest
from testcase.test_baidu import MyTest
from testcase.test_baidu2 import MyTest2
from testcase.test_baidu3 import MyTest3
from testcase.test_baidu4 import MyTest4
#import test_project.testcase.test_youdao
from HTMLTestRunner import HTMLTestRunner

# 
# test_dir='./'
# discover=unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(MyTest("test_baidu"))
    suite.addTest(MyTest2("test_baidu"))
    suite.addTest(MyTest3("test_baidu"))
    suite.addTest(MyTest4("test_baidu"))
    #suite.addTest(test_project.testcase.test_youdao.MyTest("test_youdao"))
    fp=open('D:\\eclipse\\eclipse-workspace\\unittestdemo4\\test_project\\report\\result.html','wb')
    runner=HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
    #runner=unittest.TextTestRunner()
    runner.run(suite)
    fp.close
