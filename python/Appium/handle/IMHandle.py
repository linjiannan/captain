from page.IM import IM


class IMHandle:
    def __init__(self,i):
        self.im=IM(i)
    def click_IM_icon(self):
        self.im.get_IM_icon().click()
    def click_group(self):
        self.im.get_IM_group().click()
    def longPress_IM_text(self):
        self.im.get_IM_text_longPress()
    def click_IM_copy(self):
        self.im.get_IM_copy().click()
    def switch_to_alert(self):
        self.im.switch_to_alert()