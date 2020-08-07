# 分类层封装类
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage,BaseHandle

# 对象库层
class CategoryPage(BasePage):
    # 初始化
    def __init__(self):
        # 获取父类初始化浏览器驱动
        super().__init__()

        # 获取新增分类元素
        self.cate_add = (By.CSS_SELECTOR, ".el-popover__reference span")
        # 获取新增分类输入元素
        self.cate_input = (By.CSS_SELECTOR, ".el-input__inner")
        # 获取新增分类按钮
        self.cate_btn = (By.CSS_SELECTOR, "div[role='tooltip'] .el-button--primary span")

        # 获取新增品牌元素
        self.brand_add = (By.XPATH, "//tbody/tr[6]/td[3]/div/button/span")
        # 获取新增品牌输入元素
        self.brand_input = (By.XPATH, "//div[@class='el-input']/input")
        # 获取新增品牌按钮
        self.brand_btn = (By.CSS_SELECTOR, ".dialog-footer .el-button--primary")

    # 获取新增分类元素对象
    def find_cate_add(self):
        return self.find_element(self.cate_add)
    # 获取新增分类输入元素对象
    def find_cate_input(self):
        return self.find_element(self.cate_input)
    # 获取新增分类按钮元素对象
    def find_cate_btn(self):
        return self.find_element(self.cate_btn)

    # 获取新增品牌元素对象
    def find_brand_add(self):
        return self.find_element(self.brand_add)
    # 获取新增品牌输入对象
    def find_brand_input(self):
        return self.find_element(self.brand_input)
    # 获取新增品牌按钮元素对象
    def find_brand_btn(self):
        return self.find_element(self.brand_btn)

# 操作层
class CategoryHandle(BaseHandle):
    def __init__(self):
        self.category_page = CategoryPage()

    # 点击新增分类操作
    def click_cate_add(self):
        self.category_page.find_cate_add().click()
    # 获取分类输入操作
    def input_cate(self,cate_name):
        self.input_text(self.category_page.find_cate_input(),cate_name)
    # 点击确定按钮
    def click_cate_btn(self):
        self.category_page.find_cate_btn().click()

    # 点击新增品牌操作
    def click_brand_add(self):
        self.category_page.find_brand_add().click()
    # 获取品牌输入操作
    def input_brand(self,brand_name):
        self.input_text(self.category_page.find_brand_input(),brand_name)
    # 点击品牌确认按钮
    def click_brand_btn(self):
        self.category_page.find_brand_btn().click()


# 业务层
class CategoryProxy:
    def __init__(self):
        self.category_handle = CategoryHandle()

    # 执行添加分类操作
    def go_add_cate(self,cate_name):
        # 点击新增分类
        time.sleep(0.3)
        self.category_handle.click_cate_add()
        time.sleep(0.3)
        # 输入分类
        self.category_handle.input_cate(cate_name)
        time.sleep(0.3)
        # 点击确定按钮
        self.category_handle.click_cate_btn()
        time.sleep(0.3)

    # 执行添加品牌操作
    def go_add_bran(self,brand_name):
        # 新增品牌
        self.category_handle.click_brand_add()
        # 输入品牌
        self.category_handle.input_brand(brand_name)
        # 点击确认按钮
        self.category_handle.click_brand_btn()
        # 获取提示文本
