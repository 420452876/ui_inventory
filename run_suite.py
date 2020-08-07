import unittest,time
from HTMLTestRunner_PY3 import HTMLTestRunner

from case.test_customer import TestCustomer
from config import BASE_DIR
from case.test_category import TestCategory
from case.test_stock import TestStock

suite = unittest.TestSuite()
# 组装测试用例
suite.addTest(unittest.makeSuite(TestCategory))
suite.addTest(unittest.makeSuite(TestStock))
suite.addTest(unittest.makeSuite(TestCustomer))
# 生成测试报告
filename = BASE_DIR + "/report/test_invent.html"
with open(filename, 'wb') as f :
    runner = HTMLTestRunner(stream=f, title='ui自动化',description="进销存管理系统1.1版本，测试报告生成")
    runner.run(suite)
