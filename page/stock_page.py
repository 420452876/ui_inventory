# 库存列表封装
from selenium.webdriver.common.by import By
import time
from base.base_page import BasePage,BaseHandle

# 对象库层
class StockPage(BasePage):
    def __init__(self):
        # 获取父类浏览器驱动
        super().__init__()

        # 获取库存列表元素
        self.stock_list = (By.XPATH, "//ul[@class='el-menu el-menu--inline']/li[2]/span")
        # 获取新增库存元素
        self.stock_add = (By.CSS_SELECTOR, ".el-col-2 button")
        # 获取供应商元素
        self.supplier_input = (By.XPATH, "//form[@class='el-form']/div[1]/div/div/input")
        # 获取时间元素
        self.stock_date = (By.CSS_SELECTOR, ".el-date-editor--date")
        self.stock_time = (By.XPATH, "//table[@class='el-date-table']/tbody/tr[4]/td")
        # 获取品类元素
        self.cate_element = (By.CSS_SELECTOR, ".el-cascader .el-input__inner")
        self.cate_id = (By.XPATH, "//ul[@class='el-scrollbar__view el-cascader-menu__list']/li[4]/span")
        self.cate_son_id = (By.XPATH, "//div[@class='el-cascader-panel']/div[2]/div/ul/li/span")
        # 获取模型元素
        self.stock_model = (By.XPATH, "//form[@class='el-form']/div[4]/div/div/input")
        # 获取进货价格元素
        self.stock_price = (By.XPATH, "//input[@oninput=\"value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')\"]")
        # 获取新增库存数量元素
        self.stock_number = (By.XPATH, "//input[@aria-label='描述文字']")
        # 获取确认按钮
        self.stock_btn = (By.XPATH, "//div[@class='el-dialog__footer']/span/button[@class='el-button el-button--primary']")

        # 获取出库元素
        self.stock_out = (By.CSS_SELECTOR, ".el-button--warning")
        # 获取出货人元素
        self.stock_out_people= (By.XPATH, "//div[@aria-label='出库']/div[2]/form/div[6]/div/div/input")
        # 获取出货时间元素
        self.stock_out_date = (By.XPATH, "//form[@class='el-form']/div[7]/div/div[@class='el-date-editor el-input el-input--prefix el-input--suffix el-date-editor--date']")
        self.stock_out_time = (By.XPATH, "//div[@class='el-picker-panel__content']/table[1]/tbody/tr[6]/td[3]/div/span")
        # 获取出库数量元素
        self.stock_out_number = (By.XPATH, "//form[@class='el-form']/div[8]/div/div/div/input")
        # 获取出库价格
        self.stock_out_price = (By.XPATH, "//input[@oninput=\"value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')\"]")
        # 获取出库确认按钮元素
        self.stock_out_btn = (By.XPATH, "//div[@aria-label='出库']/div[3]/span/button[2]/span")




    # 获取库存列表元素对象
    def find_stock_list(self):
        return self.find_element(self.stock_list)
    # 获取新增库存元素对象
    def find_stock_add(self):
        return self.find_element(self.stock_add)
    # 获取供应商元素对象
    def find_supplier_input(self):
        return self.find_element(self.supplier_input)
    # 获取时间元素对象
    def find_stock_date(self):
        return self.find_element(self.stock_date)
    def find_stock_time(self):
        return self.find_element(self.stock_time)
    # 获取品类元素对象
    def find_cate_element(self):
        return self.find_element(self.cate_element)
    def find_cate_id(self):
        return self.find_element(self.cate_id)
    def find_cate_sonid(self):
        return self.find_element(self.cate_son_id)
    # 获取模型元素对象
    def find_stock_model(self):
        return self.find_element(self.stock_model)
    # 获取价格元素对象
    def find_stock_price(self):
        return self.find_element(self.stock_price)
    # 获取新增库存数量元素对象
    def find_stock_number(self):
        return self.find_element(self.stock_number)
    # 获取确认按钮元素对象
    def find_stock_btn(self):
        return self.find_element(self.stock_btn)

    # 获取出库元素对象
    def find_stock_out(self):
        return self.find_element(self.stock_out)
    # 获取出货人元素对象
    def find_stock_out_people(self):
        return self.find_element(self.stock_out_people)
    # 获取出货时间元素对象
    def find_stock_out_date(self):
        return self.find_element(self.stock_out_date)
    def find_stock_out_time(self):
        return self.find_element(self.stock_out_time)
    # 获取出货数量元素对象
    def find_stock_out_number(self):
        return self.find_element(self.stock_out_number)
    # 获取出货价格元素对象
    def find_stock_out_price(self):
        return self.find_element(self.stock_out_price)
    # 获取出库确认按钮元素对象
    def find_stock_out_btn(self):
        return self.find_element(self.stock_out_btn)


class StockHandle(BaseHandle):
    def __init__(self):
        self.stock_page = StockPage()

    # 点击库存列表操作
    def click_stock_list(self):
        self.stock_page.find_stock_list().click()
    # 点击新增库存操作
    def click_stock_add(self):
        self.stock_page.find_stock_add().click()
    # 获取供应商输入操作
    def input_supplier(self,sup_name):
        self.input_text(self.stock_page.find_supplier_input(),sup_name)
    # 选择时间点击操作
    def click_stock_date(self):
        self.stock_page.find_stock_date().click()
    def click_stock_time(self):
        self.stock_page.find_stock_time().click()
    # 选择分类点击操作
    def click_cate_element(self):
        self.stock_page.find_cate_element().click()
    def click_cate_id(self):
        self.stock_page.find_cate_id().click()
    def click_cate_sonid(self):
        self.stock_page.find_cate_sonid().click()
    # 获取型号输入操作
    def input_stock_model(self,model):
        self.input_text(self.stock_page.find_stock_model(),model)
    # 获取价格输入操作
    def input_stock_price(self,price):
        self.input_text(self.stock_page.find_stock_price(),price)
    # 获取数量输入操作
    def input_stock_number(self,number):
        self.input_text(self.stock_page.find_stock_number(),number)
    # 点击确认按钮操作
    def click_stock_btn(self):
        self.stock_page.find_stock_btn().click()

    # 点击出库操作
    def click_stock_out(self):
        self.stock_page.find_stock_out().click()
    # 获取出货人输入操作
    def input_stock_out_people(self,shippers):
        self.input_text(self.stock_page.find_stock_out_people(),shippers)
    # 点击出库时间操作
    def click_stock_out_date(self):
        self.stock_page.find_stock_out_date().click()
    def click_stock_out_time(self):
        self.stock_page.find_stock_out_time().click()
    # 获取出库数量输入操作
    def input_stock_out_number(self,out_number):
        self.input_text(self.stock_page.find_stock_out_number(),out_number)
    # 获取出库价格输入操作
    def input_stock_out_price(self,out_price):
        self.input_text(self.stock_page.find_stock_out_price(),out_price)
    # 点击出库确认按钮操作
    def click_stock_out_btn(self):
        self.stock_page.find_stock_out_btn().click()



class StockProxy:
    def __init__(self):
        self.stock_handle = StockHandle()

    # 执行添加库存
    def go_add_stock(self,supplier_name,model,price,number):
        time.sleep(0.3)
        # 点击库存列表
        self.stock_handle.click_stock_list()
        # 点击新增库存
        time.sleep(0.3)
        self.stock_handle.click_stock_add()
        # 输入供应商
        time.sleep(0.3)
        self.stock_handle.input_supplier(supplier_name)
        # 点击选择时间
        time.sleep(0.3)
        self.stock_handle.click_stock_date()
        time.sleep(0.3)
        self.stock_handle.click_stock_time()
        # 选择分类
        time.sleep(0.3)
        self.stock_handle.click_cate_element()
        time.sleep(0.3)
        self.stock_handle.click_cate_id()
        time.sleep(0.3)
        self.stock_handle.click_cate_sonid()
        # 输入型号
        time.sleep(0.3)
        self.stock_handle.input_stock_model(model)
        # 输入价格
        time.sleep(0.3)
        self.stock_handle.input_stock_price(price)
        # 输入数量
        time.sleep(0.3)
        self.stock_handle.input_stock_number(number)
        # 点击确认
        time.sleep(0.3)
        self.stock_handle.click_stock_btn()
        time.sleep(0.3)

    # 执行出库
    def go_out_stock(self,shippers,out_number,out_price):
        # 点击库存列表
        time.sleep(0.2)
        self.stock_handle.click_stock_list()
        # 点击出库
        time.sleep(0.2)
        self.stock_handle.click_stock_out()
        # 输入出货人
        time.sleep(0.2)
        self.stock_handle.input_stock_out_people(shippers)
        # 选择出货时间
        time.sleep(0.2)
        self.stock_handle.click_stock_out_date()
        time.sleep(0.2)
        self.stock_handle.click_stock_out_time()
        # 输入数量
        time.sleep(0.2)
        self.stock_handle.input_stock_out_number(out_number)
        # 输入价格
        time.sleep(0.2)
        self.stock_handle.input_stock_out_price(out_price)
        # 点击确认
        time.sleep(0.2)
        self.stock_handle.click_stock_out_btn()
        # 返回提示框内容
        time.sleep(0.2)
