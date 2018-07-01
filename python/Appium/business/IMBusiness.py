import time

from handle.IMHandle import IMHandle


class IMBusiness:
    def __init__(self,i):
        self.IMHandle=IMHandle(i)
    def InIM(self):
        self.IMHandle.click_IM()
        time.sleep(2)
        self.IMHandle.click_IM1()
        time.sleep(2)
        self.IMHandle.long_click_IM_text()
        time.sleep(2)
        #self.IMHandle.switch_to_alert()
        #time.sleep(1)
        self.IMHandle.click_IM_copy()
