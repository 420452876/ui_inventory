from utils import UtilsDriver

# 定义对象库基类层
class BasePage:
    def __init__(self):
        # 获取浏览器驱动
        self.driver = UtilsDriver.get_driver()

    # 定义获取元素基类的方法
    def find_element(self,location):
        return self.driver.find_element(location[0],location[1])

# 定义操作基类层
class BaseHandle:
    # 定义对象的输入操作
    def input_text(self,element,text):
        # 清除操作
        element.clear()
        element.send_keys(text)

# 定义业务基类层
class BaseProxy:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    # 切换窗口
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])