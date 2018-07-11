import inspect

import sys

sys.path.append("G:/git/captain/python/Appium")
from handle.loginHandle import  loginHandle
class loginBusiness:
    def __init__(self,i):
        self.loginBusiness=loginHandle(i)
        print("loginBusiness 的i： "+str(i) )
    def loginPass(self):
        self.loginBusiness.inputUsername("5000")
        self.loginBusiness.inputPassword("Yeastar123")
        self.loginBusiness.get_ScreenShot(inspect.stack()[1][3])
    def loginError(self):
        self.loginBusiness.inputUsername("5001")
        self.loginBusiness.inputPassword("Yeastar12")
        self.loginBusiness.clickLoginButton()
        flag=self.loginBusiness.get_fail_toast("请配置服务器")
        if flag:
            return True
        else:
            return False

