import time

import sys

sys.path.append("G:/git/captain/python/Appium")
from handle.IMHandle import IMHandle


class IMBusiness:
    def __init__(self,i):
        self.IMHandle=IMHandle(i)
    def InIM(self):
        time.sleep(2)
        self.IMHandle.click_IM_icon()
        time.sleep(2)
        self.IMHandle.click_group()
        time.sleep(2)
        self.IMHandle.longPress_IM_text()
        time.sleep(2)
        #self.IMHandle.switch_to_alert()
        #time.sleep(1)
        self.IMHandle.click_IM_copy()
