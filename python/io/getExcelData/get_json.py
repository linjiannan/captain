# coding=utf-8
#数据 {"login":{"usernaem":"linjiannan","password":"captain"},"loginout":{"loginoutButton":"1111"}}
import json
# fp=open("F:\json\data.json")
# datab=json.load(fp)
# print datab['login']
class get_json:
    def __init__(self,file_path="F:\json\data.json"):
        self.file_path=file_path
        self.data=self.read_data()
    #读取json文件
    def read_data(self):
        with open(self.file_path) as fd:
            data = json.load(fd)
            return data
    #获取json文件内容
    def content(self,value):
        content=self.data[value]
        return content
if __name__ == '__main__':
    getjson=get_json()
    login=getjson.content("login")
    print login
