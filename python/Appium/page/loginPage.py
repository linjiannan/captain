import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.conf import conf

class loginPage:
    #在底层传i进去，表示要运行的设备
    def __init__(self,i):
        self.conf=conf(i)
    def get_login_username(self):
        return self.conf.fd_e("username", "login")

    def get_login_password(self):
        return self.conf.fd_e("password", "login")

    def get_loginButton(self):
        return self.conf.fd_e("loginButton", "login")

    def get_fail_toast(self,message):
        self.conf.get_tost_element(message)
    def get_ScreenShot(self,functionName):
        self.conf.get_ScreenShot(functionName)



