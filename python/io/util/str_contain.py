# coding=utf-8



class str_contain:
    def is_contain(self,str_one,str_two):
        flag=None
        #把unicode类型转换为字符串类型
        # if isinstance(str_one,unicode):
        #     str_one=str_one.encode('unicode-escape').decode('string_escape')
        # #判断字符串1是否包含在字符串2里面
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag


