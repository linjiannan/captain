# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5中单元格的基本例子

'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QColor
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView,
                             QPushButton)


class Table1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(430, 230);
        conLayout = QHBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        button1 = QPushButton(self)
        button1.setText("你好")
        conLayout.addWidget(self.tableWidget)
        conLayout.addWidget(button1)
        #设置表头的颜色
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView:section{background-color:rgb(85, 85, 0);color: white;};");
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        #self.tableWidget.horizontalHeader().setStyleSheet("background-color: rgb(170, 170, 255)")
        #self.tableWidget.horizontalHeader().setStyleSheet("background-color: rgb(170, 170, 255);")
        newItem = QTableWidgetItem("张三")
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem("男")
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem("160")
        self.tableWidget.setItem(0, 2, newItem)
        self.tableWidget.verticalHeader().setVisible(False)
        self.setLayout(conLayout)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.itemChanged['QTableWidgetItem*'].connect(self.one)
        self.setWindowTitle("这是一个TableWidget")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        qssStyle = '''
             QWidget{
        	     background-color:yellow
        	}'''
        #self.tableWidget.setStyleSheet(qssStyle)
        # 字体颜色（红色）
        #self.tableWidget.item(0, 0).setForeground(QBrush(QColor(255, 0, 0)))

    def one(self):
        # 获取选中的行号
        index = self.tableWidget.currentIndex()
        print("index")
        print(index)
        indexnum = index.row()
        rownum = index.column()
        print(indexnum)
        print(rownum)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    examplea = Table1()
    #设置透明度
    examplea.setWindowOpacity(0.9)
    palette=QPalette()
    palette.setColor(QPalette.Background,Qt.gray)
    examplea.setPalette((palette))

    examplea.show()
    sys.exit(app.exec_())
