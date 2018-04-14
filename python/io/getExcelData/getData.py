# coding=utf-8
#数据 {"login":"usernaem"}
import json
fp=open("F:\json\date.txt")
datab=json.load(fp)
print datab['login']