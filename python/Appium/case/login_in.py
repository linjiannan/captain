import sys

sys.path.append("G:/git/captain/python/Appium")
import unittest
import HTMLTestRunner
import threading
import multiprocessing
from util.server import Server
import time
from appium import webdriver
from business.loginBusiness import loginBusiness
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame
class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpclass---->", parames)
        cls.login_business = loginBusiness(parames)

    def setUp(self):
        print("this is setup\n")

    def test_01(self):
        self.login_business.loginPass()
    def test_02(self):
        self.login_business.loginError()
        self.assertTrue(True)

    def tearDown(self):
        time.sleep(1)

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
    HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)


def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    print("++++")
    appium_init()
    # get_suite(0)
    threads = []
    for i in range(get_count()):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()

    # time.sleep(1)
# time.sleep(80)