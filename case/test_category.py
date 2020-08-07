import unittest

from page.category_page import CategoryProxy
from utils import UtilsDriver,get_tip_msg,get_case_data
from parameterized import parameterized
from config import BASE_DIR

filename = BASE_DIR + "/data/add_category_case.json"

class TestCategory(unittest.TestCase):
    # 类级别前置操作
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = UtilsDriver.get_driver()
        cls.category_page = CategoryProxy()
    # 类级别后置操作
    @classmethod
    def tearDownClass(cls):
        UtilsDriver.quit_driver()
    # 方法级别前置操作
    def setUp(self):
        self.driver.get("http://localhost")


    # 新增分类
    @parameterized.expand(get_case_data(filename,"add_category"))
    def test01_add_cate(self,cate_name,brand_name,msg):
        # 添加分类
        self.category_page.go_add_cate(cate_name)
        self.assertIn(msg,get_tip_msg())
        # 添加品牌
        self.category_page.go_add_bran(brand_name)
        self.assertIn(msg,get_tip_msg())

