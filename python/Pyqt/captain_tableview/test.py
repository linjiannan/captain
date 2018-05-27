# -*- coding: utf-8 -*-
import sqlite3

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class myDialog(QDialog):
    """docstring for myDialog"""
    def __init__(self, arg=None):
        super(myDialog, self).__init__(arg)
        self.setWindowTitle("first window")
        self.setWindowFlags(Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.resize(500,300)
        # 数据表
        self.tableView = None
        # 总数页文本
        self.totalPageLabel = None
        # 当前页文本
        self.currentPageLabel = None
        # 转到页输入框
        self.switchPageLineEdit = None
        # 前一页按钮
        self.prevButton = None
        # 后一页按钮
        self.nextButton = None
        # 转到页按钮
        self.switchPageButton = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecrodCount = 0
        # 每页显示记录数
        self.PageRecordCount = 5
        self.db = None
        self.Ui()
        self.setTable()
    #把数据插入表中
    def insert_Table(self,limitIndex=0):
        #从数据库取值和列数
        values=self.recordQuery(limitIndex)
        print("currentPage")
        print(self.currentPage)
        print("totalPage")
        print(self.totalPage)
        print("******")
        #count=getSqlite.getRowCount()
        if self.currentPage<self.totalPage:
            print("currentPage")
            print(self.currentPage)
            print("currentPage")
            print(self.totalPage)
            print("^^^^^^^^^")
            num=self.PageRecordCount
            self.model=QStandardItemModel(num,3)
        else:
            num=self.totalRecrodCount-(self.totalPage-1)*self.PageRecordCount
            print("+++++")
            print(num)
            self.model = QStandardItemModel(num, 3)
        self.model.setHorizontalHeaderLabels(['ID','Name','Sex'])
        #把数据全部插入到表格中
        for row in range(num):
            for column in range(3):
                item = QStandardItem("%s"% str(values[row][column]))
                self.model.setItem(row, column, item)

        #下面代码让表格100填满窗口
        #self.tableView.horizontalHeader().setStretchLastSection(True)
        #self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.model)

    def Ui(self):
        # 操作布局，水平布局
        layout2 = QHBoxLayout()
        self.Button_add = QPushButton("增加一行")
        self.Button_del = QPushButton("删除一行")
        # 点击按钮的时候弹出另外一个对话框

        layout2.addWidget(self.Button_add)
        layout2.addWidget(self.Button_del)

        operatorLayout = QHBoxLayout()
        self.prevButton = QPushButton("前一页")
        self.nextButton = QPushButton("后一页")
        self.switchPageButton = QPushButton("Go")
        # 设置输入框
        self.switchPageLineEdit = QLineEdit()
        self.switchPageLineEdit.setFixedWidth(40)

        switchPage = QLabel("转到第")
        page = QLabel("页")
        operatorLayout.addWidget(self.prevButton)
        operatorLayout.addWidget(self.nextButton)
        operatorLayout.addWidget(switchPage)
        operatorLayout.addWidget(self.switchPageLineEdit)
        operatorLayout.addWidget(page)
        operatorLayout.addWidget(self.switchPageButton)
        operatorLayout.addWidget(QSplitter())

        # 水平布局
        statusLayout = QHBoxLayout()
        # 总页数
        self.totalPageLabel = QLabel()
        self.totalPageLabel.setFixedWidth(70)
        # 当前页
        self.currentPageLabel = QLabel()
        self.currentPageLabel.setFixedWidth(70)
        # 数据条数
        self.totalRecordLabel = QLabel()
        self.totalRecordLabel.setFixedWidth(70)

        statusLayout.addWidget(self.totalPageLabel)
        statusLayout.addWidget(self.currentPageLabel)
        statusLayout.addWidget(QSplitter())
        statusLayout.addWidget(self.totalRecordLabel)

        # 设置表格属性
        self.tableView = QTableView()
        #
        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 创建界面，垂直布局
        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(layout2)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tableView)
        mainLayout.addLayout(statusLayout)
        self.setLayout(mainLayout)
        # 信号槽连接
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)
        self.Button_add.clicked.connect(self.otherDialog)
        self.Button_del.clicked.connect(self.delrow)
    def delrow(self):
        #获取选中的行号
        index = self.tableView.currentIndex()
        print("index")
        print(index)
        indexnum=index.row()
        #没有选中就是-1
        if indexnum !=-1:
            print("index %d"%indexnum)
            #获取选中的行号的数据
            result=getSqlite.record((self.currentPage-1)*5+indexnum,1)
            print("获取选中的数据")
            print(type(result[0][0]))
            print(result[0][0])
            print(result[0][1])
            print(result[0][2])
            for a in result:
                print(a)
            print("index.row()")
            print(index.row())
            #self.model.removeRow(index.row())
            print("@%@#$%^#$%")
            getSqlite.del_record(result)
            myWindow.setTable()
    def setTable(self):
        # 设置当前页
        self.currentPage = 1;
        # 得到总记录数
        self.totalRecrodCount = self.getTotalRecordCount()
        print("+++")
        print(self.totalRecrodCount)
        # 得到总页数
        self.totalPage = self.getPageCount()
        # 刷新状态
        self.updateStatus()
        # 设置总页数文本
        self.setTotalPageLabel()
        # 设置总记录数
        self.setTotalRecordLabel()

        # 记录查询
        self.insert_Table()
    # 另外一个界面显示
    def otherDialog(self):
        self.one = InputdialogDemo()
        self.one.show()

    # 得到记录数
    def getTotalRecordCount(self):
        rowCount =getSqlite.getRowCount()
        print('记录数rowCount=' + str(rowCount))
        return rowCount

    # 得到页数
    def getPageCount(self):
        # 如果刚好能被整除的话，计算的结果就是总的页数
        if self.totalRecrodCount % self.PageRecordCount == 0:
            print("总页数")
            print(self.totalRecrodCount // self.PageRecordCount)
            return (self.totalRecrodCount // self.PageRecordCount)
        else:
            print("总页数")
            print(self.totalRecrodCount // self.PageRecordCount + 1)
            return (self.totalRecrodCount // self.PageRecordCount + 1)

    # 记录查询
    def recordQuery(self, limitIndexnum):
        if self.currentPage<self.totalPage:
            num=self.PageRecordCount
            print("num")
            print(num)
        else:
            num=self.totalRecrodCount-(self.totalPage-1)*self.PageRecordCount
            print("num")
            print(num)
        record=getSqlite.record(limitIndexnum,num)
        print("@@@@@@")
        return record

    # 刷新状态
    def updateStatus(self):
        # 设置按钮是否可用
        if self.currentPage == 1:
            self.prevButton.setEnabled(False)
            self.nextButton.setEnabled(True)
        elif self.currentPage >= self.totalPage:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(True)
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.currentPageLabel.setText(szCurrentText)

    # 设置总数页文本
    def setTotalPageLabel(self):
        print("设置总页数")
        szPageCountText = ("总共%d页" % self.totalPage)
        self.totalPageLabel.setText(szPageCountText)
        print("+++")
        print(szPageCountText)

    # 设置总记录数
    def setTotalRecordLabel(self):
        print("设置总记录数")
        szTotalRecordText = ("共%d条" % self.totalRecrodCount)
        print('*** setTotalRecordLabel szTotalRecordText=' + szTotalRecordText)
        self.totalRecordLabel.setText(szTotalRecordText)
        print("+++")
        print(szTotalRecordText)

    # 前一页按钮按下
    def onPrevButtonClick(self):
        print('*** onPrevButtonClick ');
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.currentPage -= 1
        self.insert_Table(limitIndex)
        self.updateStatus()

        # 后一页按钮按下

    def onNextButtonClick(self):
        print('*** onNextButtonClick ');
        # 跳过limitIndex条
        limitIndex = self.currentPage * self.PageRecordCount
        self.currentPage += 1
        self.insert_Table(limitIndex)
        self.updateStatus()

        # 转到页按钮按下

    def onSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.switchPageLineEdit.text()
        print(type(szText))
        print(szText)
        # 数字正则表达式
        print("+++++")
        import re
        pattern = re.compile(r'^[0-9]*$')
        match = pattern.match(szText)
        print(match)
        print("-----")
        # 判断是否为数字
        if not match:
            QMessageBox.information(self, "提示", "请输入数字")
            return

        # 是否为空
        if szText == '':
            QMessageBox.information(self, "提示", "请输入跳转页面")
            return

        # 得到页数
        pageIndex = int(szText)
        # 判断是否有指定页
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.PageRecordCount

        # 记录查询
        self.recordQuery(limitIndex);
        # 设置当前页
        self.currentPage = pageIndex
        # 刷新状态
        self.updateStatus();
class getSqlite():
    def __init__(self):
        self.conn = sqlite3.connect('F:\\sql\\test.db')
        self.c = self.conn.cursor()
        print("Opened database successfully")
    #获取所有的数据
    def getValue(self):
        cursor = self.c.execute("select * from info ")
        cursor = cursor.fetchall()
        for i in cursor:
            print(i)
        return cursor
    #获取总的条数
    def getRowCount(self):
        results=self.c.execute("select count(*) from info")
        count=results.fetchall()
        count=count[0][0]
        print(type(count))
        print("count的数为")
        print(count)
        return count
    def record(self,limitIndex,PageRecordCount):
        results = ("select * from info limit %d,%d" % (limitIndex, PageRecordCount))
        record=self.c.execute(results)
        record = record.fetchall()
        print("$$$$")
        return record
    def del_record(self,row_values):
        results="delete from info where id='{id}' and name='{name}' and sex='{sex}'".format(id=row_values[0][0],name=row_values[0][1],sex=row_values[0][2])
        record = self.c.execute(results)
        self.conn.commit()
class InputdialogDemo(QWidget):
    def __init__(self):
        #super(InputdialogDemo,self).__init__(parent)
        super(InputdialogDemo,self).__init__()
        label1=QLabel()
        label2=QLabel()
        label3=QLabel()
        label4 = QLabel()
        self.line1=QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.btn1=QPushButton("OK")
        self.btn1.clicked.connect(self.getText)
        self.btn1.clicked.connect(self.close)
        label1.setText("ID")
        label2.setText("Name")
        label3.setText("Sex")
        label4.setText(" ")
        layout=QFormLayout()
        layout.addRow(label1,self.line1)
        layout.addRow(label2, self.line2)
        layout.addRow(label3, self.line3)
        layout.addRow(label4, self.btn1)
        self.setLayout(layout)
    def  getText(self):
        self.one=self.line1.text()
        self.two=self.line2.text()
        self.three=self.line3.text()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 设置要连接的数据库名称
        self.db.setDatabaseName('F:\\sql\\test.db')
        if not self.db.open():
            return False
        # 打开数据库
        self.db.open()
        # 声明查询模型
        query = QSqlQuery()
        print(type(self.one))
        #print(int(self.one));下面这3个语句导致了崩溃
        #print(int(self.two))
        #print(int(self.three))
        #https://blog.csdn.net/qq_26033611/article/details/79224565
        #query.exec("insert into info values(" +self.one + "," + self.two + "," + self.three + ")")
        query.exec("insert into info values({one},{two},{three})".format(one=self.one,two=self.two,three=self.three))
        self.db.close()
        print(self.one)
        print(self.two)
        print(self.three)
        myWindow.setTable()

if __name__ == '__main__':
    getSqlite = getSqlite()
    app = QApplication(sys.argv)
    myWindow = myDialog()
    myWindow.show()
    sys.exit(app.exec_())


