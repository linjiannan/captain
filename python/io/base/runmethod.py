#coding:utf-8
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

if __name__ == '__main__':
	run=RunMethod()
	geta='get'
	date='熊猫'
	result=run.run_main(method=geta,url='https://www.sogou.com',data=date)
	print type(geta)
	print type(date)
	print result.text
	print result


