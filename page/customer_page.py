# 顾客信息层封装
from selenium.webdriver.common.by import By
import time
from base.base_page import BasePage,BaseHandle
# 对象库层
class CustomerPage(BasePage):
    def __init__(self):
        # 获取父类浏览器驱动对象
        super().__init__()

        # 获取顾客信息元素列表
        self.list_customer = (By.XPATH, "//li[@default-active='this.$route.path']/ul/li[3]/span")
        # 获取新增顾客元素
        self.add_customer = (By.XPATH, "//div[@class='el-row is-justify-space-around el-row--flex']/div[2]/button[1]")
        # 获取出货人元素
        self.shippers_customer = (By.XPATH, "//div[@class='el-dialog__body']/form/div/div/div/input")
        # 获取模型元素
        self.model_customer = (By.XPATH, "//div[@class='el-dialog__body']/form/div[2]/div/div/input")
        # 获取顾客姓名元素
        self.name_customer = (By.XPATH, "//div[@class='el-dialog__body']/form/div[3]/div/div/input")
        # 获取联系电话元素
        self.phone_customer = (By.XPATH, "//div[@class='el-dialog__body']/form/div[4]/div/div/input")
        # 获取收货地址元素
        self.address_customer = (By.XPATH, "//div[@class='el-dialog__body']/form/div[5]/div/div/input")
        # 获取出单时间元素
        self.issuer_date = (By.XPATH, "//div[@class='el-dialog__body']/form/div[6]/div/div/input")
        self.issuer_time = (By.XPATH, "//div[@class='el-picker-panel__content']")
        # 获取送货时间元素
        self.delivery_date = (By.XPATH, "//div[@class='el-dialog__body']/form/div[7]/div/div/input")
        self.delivery_time = (By.XPATH, "//div[@x-placement='top-start']/div/div/div[2]/table/tbody/tr[5]/td[5]")
        # 获取备注元素
        self.remarks_customer = (By.XPATH, "//div[@class='el-dialog__body']/form/div[8]/div/div/textarea")
        # 获取确认按钮元素
        self.btn_customer = (By.XPATH, "//div[@aria-label='客户信息']/div[3]/span/button[2]")

    # 获取顾客信息列表元素对象
    def find_list_customer(self):
        return self.find_element(self.list_customer)
    # 获取新增顾客元素对象
    def find_add_customer(self):
        return self.find_element(self.add_customer)
    # 获取出货人元素对象
    def find_shippers_customer(self):
        return self.find_element(self.shippers_customer)
    # 获取模型元素对象
    def find_model_customer(self):
        return self.find_element(self.model_customer)
    # 获取顾客姓名元素对象
    def find_name_customer(self):
        return self.find_element(self.name_customer)
    # 获取联系电话元素对象
    def find_phone_customer(self):
        return self.find_element(self.phone_customer)
    # 获取收货地址元素对象
    def find_address_customer(self):
        return self.find_element(self.address_customer)
    # 获取出单时间元素对象
    def find_issuer_date(self):
        return self.find_element(self.issuer_date)
    def find_issuer_time(self):
        return self.find_element(self.issuer_time)
    # 获取送货时间元素对象
    def find_delivery_date(self):
        return self.find_element(self.delivery_date)
    def find_delivery_time(self):
        return self.find_element(self.delivery_time)
    # 获取备注元素对象
    def find_remarks_customer(self):
        return self.find_element(self.remarks_customer)
    # 获取确认按钮元素对象
    def find_btn_customer(self):
        return self.find_element(self.btn_customer)


# 操作层
class CustomerHandle(BaseHandle):
    def __init__(self):
        self.customer_page = CustomerPage()

    # 点击顾客列表操作
    def click_list_customer(self):
        self.customer_page.find_list_customer().click()
    # 点击新增顾客操作
    def click_add_customer(self):
        self.customer_page.find_add_customer().click()
    # 出货人输入操作
    def input_shippers_customer(self,shippers):
        self.input_text(self.customer_page.find_shippers_customer(),shippers)
    # 型号输入操作
    def input_model_customer(self, model):
        self.input_text(self.customer_page.find_model_customer(),model)
    # 顾客姓名输入操作
    def input_name_customer(self, name):
        self.input_text(self.customer_page.find_name_customer(),name)
    # 联系电话输入操作
    def input_phone_customer(self, phone):
        self.input_text(self.customer_page.find_phone_customer(),phone)
    # 收货地址输入操作
    def input_address_customer(self,address):
        self.input_text(self.customer_page.find_address_customer(),address)
    # 点击出单时间操作
    def click_issuer_data(self):
        self.customer_page.find_issuer_date().click()
    def click_issuer_time(self):
        self.customer_page.find_issuer_time().click()
    # 点击送货时间
    def click_delivery_date(self):
        self.customer_page.find_delivery_date().click()
    def click_delivery_time(self):
        self.customer_page.find_delivery_time().click()
    # 备注输入操作
    def input_remarks_customer(self,remarks):
        self.input_text(self.customer_page.find_remarks_customer(),remarks)
    # 点击确认按钮操作
    def click_btn_customer(self):
        self.customer_page.find_btn_customer().click()


# 业务层
class CustomerProxy:
    def __init__(self):
        self.customer_handle = CustomerHandle()

    # 执行新增顾客
    def go_add_customer(self,shippers,model,name,phone,address,remarks):

        # 点击顾客列表
        time.sleep(0.2)
        self.customer_handle.click_list_customer()
        # 点击新增顾客
        time.sleep(0.2)
        self.customer_handle.click_add_customer()
        # 输入出货人
        time.sleep(0.2)
        self.customer_handle.input_shippers_customer(shippers)
        # 输入型号
        time.sleep(0.2)
        self.customer_handle.input_model_customer(model)
        # 输入顾客姓名
        time.sleep(0.2)
        self.customer_handle.input_name_customer(name)
        # 输入联系电话
        time.sleep(0.2)
        self.customer_handle.input_phone_customer(phone)
        # 输入收货地址
        time.sleep(0.2)
        self.customer_handle.input_address_customer(address)
        # 点击出单时间
        time.sleep(0.2)
        self.customer_handle.click_issuer_data()
        time.sleep(0.2)
        self.customer_handle.click_issuer_time()
        # 点击送货时间
        time.sleep(0.2)
        self.customer_handle.click_delivery_date()
        time.sleep(0.2)
        self.customer_handle.click_delivery_time()
        # 输入备注
        time.sleep(0.2)
        self.customer_handle.input_remarks_customer(remarks)
        # 点击确认
        time.sleep(0.2)
        self.customer_handle.click_btn_customer()
        time.sleep(0.2)
