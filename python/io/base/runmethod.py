#coding=utf-8
import requests
import json
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data=data,headers=header)
		else:
			res = requests.post(url=url,data=data)
		return res

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.get(url=url,data=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'Post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return res
		# return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
		#你好啊

if __name__ == '__main__':
	run=RunMethod()
	geta='get'
	date='熊猫'.encode("utf-8")
	dat={
		'Host': 'www.imooc.com',
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Referer': 'https://www.imooc.com/course/list',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Cookie': 'imooc_uuid=0bab9679-7943-4c0b-96a4-746112b8aae4; imooc_isnew_ct=1514819868; UM_distinctid=1627cc1d5c74bd-0ebff6bccbe634-5d4e211f-e1000-1627cc1d5c867e; CNZZDATA1261110065=370696219-1522506356-https%253A%252F%252Fwww.baidu.com%252F%7C1524393581; imooc_isnew=2; last_login_username=1186535553%40qq.com; PHPSESSID=r6jeh78h6qp74oo65q0ilsnak1; loginstate=1; apsid=ZkNDViMmE1MjMzZTAzMmU4NzIxOTA5N2ZhMzcxODMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTYwMzc4NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADExNmEyYTgzMGUxMDVhOTViMWNiN2RlYjA4NDEyNDU0py5XW6cuV1s%3DOW; Hm_lvt_fb538fdd5bd62072b6a984ddbc658a16=1532355032,1532439699,1532443382,1532443439; Hm_lpvt_fb538fdd5bd62072b6a984ddbc658a16=1532443439; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1532009844,1532355032,1532439699,1532443439; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1532443439; cvde=5b572c8f14dda-48; IMCDNS=1',
		'Accept-Encoding': 'gzip, deflate'
	}
	result=run.run_main(method=geta,url='https://www.imooc.com/course/list',data=dat)
	print(type(geta))
	print(type(date))
	print(result.text)
	print(result)


