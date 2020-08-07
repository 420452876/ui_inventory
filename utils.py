from selenium import webdriver
import json
# 定义工具类
from selenium.webdriver.common.by import By


class UtilsDriver :
    _driver = None
    # 定义方法创建浏览器驱动对象
    @classmethod
    def get_driver(cls):
        if cls._driver is None :
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None :
            cls.get_driver().quit()
            cls._driver = None

# 获取操作提示框信息
def get_tip_msg():
    msg = UtilsDriver.get_driver().find_element(By.CSS_SELECTOR, ".el-notification__content p").text
    return msg

# 获取json中的数据
def get_case_data(filename,params):
    # 打开json文件
    with open(filename, encoding='utf-8') as f :
        # 获取json文件里面的数据
        data = json.load(f)
        # 定义空列表
        case_list = []
        # params 参数是json数据文件的第一个键名，需要什么样的数据传什么样的键名
        case_list.append(tuple(data[params].values()))
        return case_list

