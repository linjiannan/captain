# coding=utf-8
from key_word.get_data import GetData
from key_word.action_method import ActionMethod
from util.server import Server


class RunMain:
    def run_method(self):
        server = Server()
        server.main()
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_case_lines()
        for i in range(1, lines):
            #操作步骤
            handle_step = data.get_handle_step(i)
            #操作元素
            element_key = data.get_element_key(i)
            # 操作值
            handle_value = data.get_handle_value(i)
            #预期值
            expect_key = data.get_expect_element(i)
            #预期步骤
            expect_step = data.get_expect_handle(i)
            # input()  login_button
            # input  str
            # None
            #getattr，会自动匹配acition_method中的函数
            excute_method = getattr(action_method, handle_step)
            if element_key != None:
                #执行匹配的函数
                excute_method(element_key, handle_value)
            else:
                excute_method(handle_value)
            if expect_step != None:
                expect_result = getattr(action_method, expect_step)
                result = expect_result(expect_key)
                if result:
                    data.write_value(i, "fail")
                else:
                    data.write_value(i, "pass")


if __name__ == '__main__':
    run = RunMain()
    run.run_method()
