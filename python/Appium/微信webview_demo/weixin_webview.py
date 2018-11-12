from appium import webdriver

import time

capabilities = {
    "platformName": "Android",
    # 获取toast必备
    # "automationName": "UiAutomator2",
    "deviceName": "19c1812c",
    "appPackage": "com.tencent.mm",
    "appActivity": "ui.LauncherUI",
    "noReset": "true",
    "unicodeKeyboard": True,
    "resetKeyboard": False,
    "chromeOptions":{"androidProcess":"com.tencent.mm:tools",'args': ['--no-sandbox']},
    'recreateChromeDriverSessions': True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
time.sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("订阅号")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("华尔街英语")').click()
driver.find_element_by_id("com.tencent.mm:id/yw").click()
contexts=driver.contexts
print(contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
time.sleep(8)
print("111111")
print(driver.current_context)
all_handles = driver.window_handles
print(len(all_handles))
for handle in all_handles:
    try:
        driver.switch_to_window(handle)
        driver.find_element_by_xpath('//*[@id="voice_title_MjM5NzY1MDMwMF8yNjU4NTY2OTQ1_0"]').click()
        print('定位成功')
        break
    except Exception as e:
        print("失败")
'''
相关的帖子：https://testerhome.com/topics/12003
https://www.cnblogs.com/dapped/p/7891833.html   查看手机chromedriver版本号
https://www.jianshu.com/p/b96755bf4916
http://www.cnblogs.com/peachh/p/9740172.html


'''

