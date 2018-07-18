from util.conf import conf
from util.logging import logger


class IM:
    def __init__(self,i):
        self.conf=conf(i)
    def get_IM_icon(self):
        logger.info("00000000")
        logger.info(self.conf.driver.current_activity)
        return self.conf.fd_e("IM_icon","IM")
    def get_IM_group(self):
        # ele=self.conf.fd_e("IM_group", "IM")
        # logger.info(ele.get_attribute("text"))
        return self.conf.fd_e("IM_group","IM")
    def get_IM_text_longPress(self):
        ele=self.conf.fd_e("IM_text","IM")
        logger.info("@@@@@")
        logger.info(ele.get_attribute("text"))
        logger.info(ele.text)
        self.conf.long_press_aciton(ele)
    def get_IM_copy(self):
        return self.conf.fd_e("IM_copy","IM")
    def switch_to_alert(self):
        self.conf.swith_to_alert()
