import inspect
import os

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import base_driver
from util.getBy import GetBy
class conf:
    def __init__(self,i):
        baseDriver=base_driver()
        self.driver=baseDriver.get_driver(i)
        self.getBy = GetBy(self.driver)
    #对getBy和Base_driver进行二次封装
    def fd_e(self,key,section):
        return self.getBy.get_element(key,section)
        #封装截图
    def get_ScreenShot(self,functionName):
        #文件夹的路径为当前工程路径下
        path = "../ScreenShot"
        #判断文件夹是否存在，不存在就创建文件夹
        if(not(os.path.exists(path))):
            os.mkdir(path)
        self.driver.get_screenshot_as_file('../ScreenShot/%s.png'%(functionName))
    # #封装获取方法名
    # def get_current_function_name(self):
    #     return inspect.stack()[1][3]
    # #封装获取函数加方法名
    # def function_one(self,ClassName,FunctionName):
    #     print("%s.%s" % (self.__class__.__name__, self.get_current_function_name()))
    #     return ("%s.%s" % (ClassName, FunctionName))

    #封装获取toast
    def get_tost_element(self, message):
        '''
        获取tostelement
        '''
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))