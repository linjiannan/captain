import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.getBy import GetBy
from base.base_driver import base_driver

class loginPage:
    #在底层传i进去，表示要运行的设备
    def __init__(self,i):
        baseDriver=base_driver()
        print("get_driver 的i： " + str(i))
        self.driver=baseDriver.get_driver(i)
        self.getBy = GetBy(self.driver)
    def get_login_username(self):
        return self.getBy.get_element("username", "login")

    def get_login_password(self):
        return self.getBy.get_element("password", "login")

    def get_loginButton(self):
        return self.getBy.get_element("loginButton", "login")

    def get_fail_toast(self):
        tost_element = ("xpath", "//*[contains(@text,'请配置服务器')]")
        info = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))
        print(info)

    def get_tost_element(self, message):
        '''
        获取tostelement
        '''
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))


