# coding=utf-8
import requests

class io_method:
    #封装get请求
    def send_get(self, url, data):
        res = requests.get(url=url, data=data,verify=False)
        return res
    #封装post请求
    def send_post(self, url, data):
        res = requests.post(url=url, data=data,verify=False)
        return res

    def io_method(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = 'https://www.sogou.com/web?query=%E7%86%8A%E7%8C%AB&ie=utf8&_ast=1523078016&_asf=null&w=01029901&p=40040100&dp=1&cid=&cid=&s_from=result_up'
    data={}
    run = io_method()
    result=run.io_method(url, 'GET', data)
    print result.status_code
    print result.text

# print run.run_main(url,'GET',data)
