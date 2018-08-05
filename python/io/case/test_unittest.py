# coding:utf-8
import unittest
import json
import HTMLTestRunner
from base.runmethod import RunMethod

class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMethod()

    def test_03(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001
        }
        # self.run.run_main = mock.Mock(return_value=data)
        res = self.run.run_main('Post',url,data)

        print(res)
        #self.assertEqual(res['errorCode'], 1001, "测试失败")
        print("这是第一个case")
        print(a)

    # @unittest.skip('test_02')
    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'
        }
        global a
        a=666
        res = self.run.run_main('Post',url, data)
        print(type(res))
        print(res.text)
        #转化为json格式
        print("######3")
        print(res.status_code)

        res=res.json()
        print(type(res))
        print(res['errorCode'])
        #self.assertEqual(res['errorCode'], 1007, "测试失败")
        print("这是第二个case")





if __name__ == '__main__':
    unittest.main()