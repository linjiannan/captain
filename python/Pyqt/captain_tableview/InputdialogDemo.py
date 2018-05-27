import sys
from msilib import Dialog

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QApplication, QDialog
from PyQt5.uic.properties import QtWidgets

import captain_tableview
from captain_tableview.test import myDialog, myWindow
from lineEdit.DataGrid import DataGrid


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




# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myWindow = InputdialogDemo()
#     myWindow.show()
#     sys.exit(app.exec_())
