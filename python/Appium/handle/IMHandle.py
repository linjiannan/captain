from page.IM import IM


class IMHandle:
    def __init__(self,i):
        self.im=IM(i)
    def click_IM(self):
        self.im.get_IM().click()
    def click_IM1(self):
        self.im.get_IM1().click()
    def long_click_IM_text(self):
        self.im.get_IM_text()
    def click_IM_copy(self):
        self.im.get_IM_copy().click()
    def switch_to_alert(self):
        self.im.switch_to_alert()