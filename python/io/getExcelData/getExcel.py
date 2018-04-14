# coding=utf-8
import xlrd
# data=xlrd.open_workbook(r'F:\exceltest.xlsx')
# table=data.sheets()[0]
# print table.nrows
# print table.cell_value(0,0)
# print table.cell_value(1,1)
class  getExcel:
    def __init__(self,filepatha=None,sheetsnum=0):
        if filepatha:
            self.filepatha=filepatha
            self.sheetsnum=sheetsnum
        else:
            self.filepatha = 'F:\exceltest.xlsx'
            self.sheetsnum = sheetsnum
        self.data = self.getdata()
    #获取excel内容
    def getdata(self):
        data=xlrd.open_workbook(self.filepatha)
        table=data.sheets()[self.sheetsnum]
        return table
    #获取行数
    def excel_lines(self):
        return self.data.nrows
    #获取某个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
if __name__ == '__main__':
    one=getExcel()
    print one.excel_lines()
    print one.get_cell_value(1,1)


