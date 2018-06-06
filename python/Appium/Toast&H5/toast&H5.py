# coding=utf-8
import sys

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def get_driver():
    capabilities = {
        "platformName": "Android",
        #获取toast必备
        "automationName":"UiAutomator2",
        "deviceName": "19c1812c",
        "appPackage": "com.yeastar.linkus",
        "appActivity": "com.linkus.activity.WelcomeActivity",
        "noReset": "true",
        "unicodeKeyboard":True,
        "resetKeyboard":False
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(10)
    return driver
# 获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height

# 向左边滑动
def swipe_left():
    # [100,200]
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1, 1000)


# 向右边滑动
def swipe_right():
    # [100,200]
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1, 1000)


# 向上滑动
def swipe_up():
    # [100,200]direction
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    y = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y, 1000)


# 向下滑动
def swipe_down():
    # [100,200]
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


def swipe_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    else:
        swipe_right()


def go_login():
    driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login')
    driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()


def login_by_class():
    element = driver.find_element_by_class_name('android.widget.TextView')
    elements = driver.find_elements_by_class_name('android.widget.TextView')
    elements[4].click()








#切换到H5界面
def get_web_view():
    time.sleep(10)
    webview = driver.contexts
    for viw in webview:
        if 'WEBVIEW_cn.com.open.mooc' in viw:
            driver.switch_to.context(viw)
            break
    driver.find_element_by_link_text('C').click()
    try:
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
    except Exception as e:
        #切换为正常的界面
        driver.switch_to.context(webview[0])
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
        raise e
def get_tost():
    tost_element = ("xpath","//*[contains(@text,'请配置服务器')]")
    info=WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(tost_element))
    print(info)



driver = get_driver()
element=driver.find_element_by_id('login_username_et')
element.send_keys('5000')
login=driver.find_element_by_id("login_btn").click()
get_tost()

#element1=driver.find_elements_by_class_name('android.widget.EditText')
#print(len(element1))
#element1[1].send_keys('wo shi')
#driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText[2]').send_keys("111")
#driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.yeastar.linkus:id/login_linearlayout"]/android.widget.LinearLayout[1]/android.widget.EditText[2]').send_keys("111")
#driver.find_element_by_xpath('//*[contains(@text,"密码")]').send_keys('111')
#driver.find_element_by_android_uiautomator('new UiSelector().text("密码")').send_keys('18513199587')


#swipe_on('right')
# time.sleep(1)
# swipe_on('left')
# time.sleep(1)
# swipe_on('up')
# time.sleep(10)
# login_by_class()
# login_by_xpath()
# get_tost()