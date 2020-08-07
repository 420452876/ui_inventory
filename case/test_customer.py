import unittest

from page.customer_page import CustomerProxy
from utils import UtilsDriver,get_tip_msg,get_case_data
from parameterized import parameterized
from config import BASE_DIR

# 获取json中的数据
filename = BASE_DIR + "/data/add_customer_case.json"
data = get_case_data(filename,"add_customer")

class TestCustomer(unittest.TestCase):
    # 类级前置别方法
    @classmethod
    def setUpClass(cls):
        cls.driver = UtilsDriver.get_driver()
        cls.customer_page = CustomerProxy()

    # 类级别后置方法
    @classmethod
    def tearDownClass(cls):
        UtilsDriver.quit_driver()

    # 方法级别前置
    def setUp(self):
        self.driver.get("http://localhost")

    # 参数化传入
    @parameterized.expand(data)
    def test01_add_customer(self,shippers,model,name,phone,address,remarks,msg):
        self.customer_page.go_add_customer(shippers,model,name,phone,address,remarks)
        self.assertIn(msg,get_tip_msg())