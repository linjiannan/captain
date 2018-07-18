#coding=utf-8
from util.read_init import ReadIni
from util.logging import logger
class GetBy:
	def __init__(self,driver):
		self.driver = driver
	def get_element(self,key,section='login'):
		read_ini = ReadIni()
		local = read_ini.get_value(key,section)
		print(local)
		if local != None:
            #方式
			by = local.split('>')[0]
            #定位数据
			local_by = local.split('>')[1]
			try:
				if by == 'id':
					if self.driver.find_element_by_id(local_by):
						logger.info("id定位的元素为"+local_by)
						return self.driver.find_element_by_id(local_by)
					else:
						print("id方式查找元素没有找到")
						logger.info("id方式查找元素没有找到")
				elif by == 'className':
					if self.driver.find_element_by_class_name(local_by):
						logger.info('className定位的元素为'+local_by)
						return self.driver.find_element_by_class_name(local_by)
					else:
						print("className方式查找元素没有找到")
						logger.info("className方式查找元素没有找到")
				elif by=='text':
					if self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'% str(local_by)):
						logger.info('text定位的元素为'+local_by)
						return self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'% str(local_by))
					else:
						print("text方式查找元素没有找到")
						logger.info("text方式查找元素没有找到")
				else:
					if self.driver.find_element_by_xpath(local_by):
						logger.info('xpath定位的元素为'+local_by)
						return self.driver.find_element_by_xpath(local_by)
					else:
						print("xpath方式查找元素没有找到")
						logger.info("xpath方式查找元素没有找到")
			except:
				#self.driver.save_screenshot("../jpg/test02.png")
				return None
		else:
			return None
