#coding=utf-8
from util.dos_cmd import DosCmd
class Port:
    #检测端口是否被使用
	def port_is_used(self,port_num):
		'''
		判断端口是否被占用
		'''
		flag = None
		self.dos = DosCmd()
		command = 'netstat -ano | findstr '+str(port_num)
		result = self.dos.excute_cmd_result(command)
		if len(result)>0:
			flag = True
		else:
			flag = False
		return flag
    #根据检测到的设备的数量生成可用的端口
	def create_port_list(self,start_port,device_list):
		'''start_port 4701
		生成可用端口
		@parameter start_port
		@parameter device_list
		'''
		port_list = []
		if device_list != None:
			#如果当前可使用的端口数没有等于设备的数量，就一直创建
			while len(port_list) != len(device_list):
				#如果当前的端口没有被使用就把端口添加到port_list中
				if self.port_is_used(start_port) != True:
					port_list.append(start_port)
				start_port = start_port +1
			return port_list
		else:
			print("生成可用端口失败")
			return None




if __name__ == '__main__':
	port = Port()
	li = [1,2,3,4,5]
	print(port.create_port_list(4722,li))