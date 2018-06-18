from appium import webdriver
from util.write_user_command import WriteUserCommand

class base_driver:
    def get_driver(self,i):
        print("get_driver的i ："+str(i))
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        print("devices: "+devices)
        print("port: "+port)
        capabilities = {
            "platformName": "Android",
            # 获取toast必备
            #"automationName": "UiAutomator2",
            "deviceName": str(devices),
            "appPackage": "com.yeastar.linkus",
            "appActivity": "com.linkus.activity.WelcomeActivity",
            "noReset": "true",
            "unicodeKeyboard": True,
            "resetKeyboard": False
        }
        url="http://127.0.0.1:" +port+"/wd/hub"
        print("URl: " + url)
        driver = webdriver.Remote(url, capabilities)
        print("我已经启动了")

        print("setupclass")
        return driver

if __name__=='__main__':
    print("+++++++")
    one=base_driver()
    one.get_driver(1)