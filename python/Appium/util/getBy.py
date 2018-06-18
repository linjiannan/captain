#coding=utf-8
from util.read_init import ReadIni
class GetBy:
	def __init__(self,driver):
		self.driver = driver
	def get_element(self,key,section):
		read_ini = ReadIni()
		local = read_ini.get_value(key,section)
		if local != None:
            #方式
			by = local.split('>')[0]
            #定位数据
			local_by = local.split('>')[1]
			try:
				if by == 'id':
					return self.driver.find_element_by_id(local_by)
				elif by == 'className':
					return self.driver.find_element_by_class_name(local_by)
				else:
					return self.driver.find_element_by_xpath(local_by)
			except:
				#self.driver.save_screenshot("../jpg/test02.png")
				return None
		else:
			return None