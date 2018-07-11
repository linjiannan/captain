#import HTMLTestRunnerCN
import HTMLTestRunnerCN as Hs
import inspect
import sys
sys.path.append("G:/git/captain/python/Appium")
import unittest
import threading
import multiprocessing
from util.server import Server
import time
from business.IMBusiness import IMBusiness
from appium import webdriver
from business.loginBusiness import loginBusiness
from util.write_user_command import WriteUserCommand
from util.conf import conf

class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame
class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpclass---->", parames)
        #cls.login_business = loginBusiness(parames)
        cls.IMBusiness=IMBusiness(parames)

    def setUp(self):
        print("this is setup\n")

    def test_01(self):
        #self.login_business.loginPass()
        #self.login_business.loginPage.conf.driver.get_screenshot_as_file('%s%s'%(png_file,img_name))
        self.IMBusiness.InIM()
    def test_02(self):
        # self.login_business.loginError()
        # self.assertTrue(True)
        pass

    def tearDown(self):
        time.sleep(1)
        self.IMBusiness.IMHandle.im.conf.driver.quit()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
    # cls.driver.quit()


def appium_init():
    server = Server()
    server.main()


def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", parame=i))
    suite.addTest(CaseTest("test_02", parame=i))
    # unittest.TextTestRunner().run(suite)
    html_file = "G:/git/captain/python/Appium/report/report" + str(i) + ".html"
    fp = open(html_file, "wb")
    #runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：',tester=u"captain")
    runner=Hs.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
    runner.run(suite)


def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    print("+++++")
    appium_init()
    threads = []
    time.sleep(3)
    for i in range(get_count()):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()

    # time.sleep(1)
# time.sleep(80)