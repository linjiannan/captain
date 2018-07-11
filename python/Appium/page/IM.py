from util.conf import conf
from util.logging import logger


class IM:
    def __init__(self,i):
        self.conf=conf(i)
    def get_IM(self):
        return self.conf.fd_e("IM","IM")
    def get_IM1(self):
        return self.conf.fd_e("IM-1","IM")
    def get_IM_text(self):
        ele=self.conf.fd_e("IM_text","IM")
        logger.info("@@@@@")
        logger.info(ele.get_attribute("text"))
        logger.info(ele.text)
        self.conf.long_press_aciton(ele)

    def get_IM_copy(self):
        return self.conf.fd_e("IM_copy","IM")
    def switch_to_alert(self):
        self.conf.swith_to_alert()
