#coding:utf-8
import sys
#解决编码问题
reload(sys)
sys.setdefaultencoding('utf-8')
#要把当前的工程目录添加到系统中去，不然会报错
sys.path.append("G:\git\captain\python\io")
from base.runmethod import RunMethod
from data.get_data import GetData
# from util.common_util import CommonUtil
# from data.dependent_data import DependdentData
# from util.send_email import SendEmail
# from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
class RunTest:
    def __init__(self):
        #定义对象
        #get、post对象
        self.run_method = RunMethod()
        #获取数据对象
        self.data = GetData()
        # self.com_util = CommonUtil()
        # self.send_mai = SendEmail()

    #程序执行的
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        #10  0,1,2,3；执行的case数值
        rows_count = self.data.get_case_lines()
        print rows_count
        #遍历执行case，去掉0行，从1行开始
        for i in range(1,rows_count):
            #判断是否执行
            is_run = self.data.get_is_run(i)
            print is_run
            #执行
            if is_run:
                #获取常规的数据
                url = str(self.data.get_request_url(i))
                print 'url'+url
                print type(url)
                method = str(self.data.get_request_method(i))
                print method
                print type(method)
                request_data = self.data.get_request_data(i)
                print request_data
                print type(request_data)
                res = self.run_method.run_main(method,url,request_data)
                return res

if __name__ == '__main__':
    run = RunTest()
    result=run.go_on_run()
    print result.status_code
    print result.text
