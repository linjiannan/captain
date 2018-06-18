#coding=utf-8
import yaml
class WriteUserCommand:
	#读取yaml文件
	def read_data(self):
		'''
		加载yaml数据
		'''
		with open("../config/userconfig.yaml") as fr:
			data = yaml.load(fr)
		return data
	#从yaml中获取数据，key为设备名，port为要启动的端口号
	def get_value(self,key,port):
		'''
		获取value
		'''
		data = self.read_data()
		value = data[key][port]
		return value

	#往yaml中写入数据，主要是数据拼接好后写入，以便base_driver可以使用
	def write_data(self,i,device,bp,port):
		'''
		写入数据
		'''
		data = self.join_data(i,device,bp,port)
		with open("../config/userconfig.yaml","a") as fr:
			yaml.dump(data,fr)
	#以二层字典的形式写入
	def join_data(self,i,device,bp,port):
		data = {
		"user_info_"+str(i):{
		    "deviceName":device,
		    "bp":bp,
		    "port":port
		}
		}
		return data
	#清楚yaml文件中的数据
	def clear_data(self):
		with open("../config/userconfig.yaml","w") as fr:
			fr.truncate()
		fr.close()
	#获取yaml中数据的行数
	def get_file_lines(self):
		data = self.read_data()
		return len(data)


if __name__ == '__main__':
	write_file = WriteUserCommand()
	print(write_file.get_value('user_info_2','bp'))
