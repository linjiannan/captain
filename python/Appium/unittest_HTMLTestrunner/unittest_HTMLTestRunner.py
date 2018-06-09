import HTMLTestRunner
import HTMLTestRunnerCN
import unittest


class Test(unittest.TestCase):
    @classmethod
    # 只运行一次
    def setUpClass(cls):
        print("setupclass")

    def setUp(self):
        print("setup")

    # @unittest.skip("test") #可跳过case
    def test_01(self):
        print("test_01")
        self.assertEqual(1, 2, "1不等于2")

    def test_02(self):
        print("test_02")

    def tearDown(self):
        print("tearDowm")

    @classmethod
    # 只运行一次
    def tearDownClass(cls):
        print("tearDownClass")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test("test_01"))
    suite.addTest(Test("test_02"))
    # unittest.TextTextRunner().run(suite)
    # 设置报告的路径
    html = "G:/git/captain/python/Appium/report/report.html"
    fp = open(html, 'wb')  # file不能用就用open
    HTMLTestRunnerCN.HTMLTestRunner(stream=fp).run(suite)