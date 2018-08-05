#coding:utf-8
import json
class OperetionJson:

	def __init__(self,file_path=None):
		if file_path  == None:
			self.file_path = '..\data_json\data.json'
		else:
			self.file_path = '..\data_json\%s'%file_path
		self.data = self.read_data()

	#读取json文件，读取zi
	def read_data(self):
		with open(self.file_path) as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self,id):
		print(type(self.data))
		return self.data[id]

	#写json
	def write_data(self,data):
		with open('..\data_json\data.json','w') as fp:
			fp.write(json.dumps(data))



if __name__ == '__main__':
	get_json = OperetionJson()
	print(get_json.get_data('value'))
