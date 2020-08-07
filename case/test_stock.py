import unittest,time
from page.stock_page import StockProxy
from utils import UtilsDriver,get_tip_msg,get_case_data
from config import BASE_DIR
from parameterized import parameterized

filename = BASE_DIR + "/data/add_stock_case.json"

class TestStock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动
        cls.driver = UtilsDriver.get_driver()
        cls.stock_page = StockProxy()

    @classmethod
    def tearDownClass(cls):
        UtilsDriver.quit_driver()

    def setUp(self):
        self.driver.get("http://localhost")

    # 新增库存
    @parameterized.expand(get_case_data(filename,"add_stock"))
    def test01_stock_add(self,supplier_name,model,price,number,msg):
        self.stock_page.go_add_stock(supplier_name,model,price,number)
        self.assertIn(msg,get_tip_msg())
        time.sleep(5)

    # 出库
    @parameterized.expand(get_case_data(filename,"out_stock"))
    def test02_out_stock(self,shippers,out_number,out_price,msg):
        self.stock_page.go_out_stock(shippers,out_number,out_price)
        self.assertIn(msg, get_tip_msg())