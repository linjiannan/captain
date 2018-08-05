#coding:utf-8
import sys
#解决编码问题
from imp import reload

#reload(sys)
#sys.setdefaultencoding('utf-8')
#要把当前的工程目录添加到系统中去，不然会报错
from data.dependent_data import DependdentData

sys.path.append("G:\git\captain\python\io")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.str_contain import str_contain
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
        self.str_contain=str_contain()

    #程序执行的
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        print(rows_count)
        #遍历执行case，去掉0行，从1行开始
        for i in range(1,rows_count):
            #判断是否执行
            is_run = self.data.get_is_run(i)
            print(is_run)
            #执行
            if is_run:
                #获取常规的数据
                url = str(self.data.get_request_url(i))
                print(url)
                method = str(self.data.get_request_method(i))
                Json_filename=self.data.get_request_data(i)
                request_data = self.data.get_data_for_json(i,Json_filename)
                print("-----------------------=====")
                print(request_data)
                except_value = str(int(self.data.get_expect_data(i)))
                depend_case = self.data.is_depend(i)
                #获取预期的结果
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    print("---------------------->")
                    # 获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    print(depend_response_data)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    print(depend_key)
                    print(type(depend_key))
                    print("@@@@@@@@@@@@@@@")
                    request_data[depend_key] = depend_response_data
                    print(request_data)
                print("$$$$$$")
                print(request_data)
                res = self.run_method.run_main(method, url, request_data)
                if self.str_contain.is_contain(except_value,res.text):
                    print("测试通过")
                    self.data.write_result(i,'passa')
                    print(res.text)
                else:
                    print("测试失败")
                    print(except_value)
                    print(res.text)
                    self.data.write_result(i, 'faila')

if __name__ == '__main__':
    run = RunTest()
    result=run.go_on_run()

