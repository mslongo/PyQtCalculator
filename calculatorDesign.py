# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(10, 90, 71, 71))
        self.button_7.setObjectName("button_7")
        self.numbers = QtWidgets.QButtonGroup(MainWindow)
        self.numbers.setObjectName("numbers")
        self.numbers.addButton(self.button_7)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(90, 90, 71, 71))
        self.button_8.setObjectName("button_8")
        self.numbers.addButton(self.button_8)
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(170, 90, 71, 71))
        self.button_9.setObjectName("button_9")
        self.numbers.addButton(self.button_9)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(90, 170, 71, 71))
        self.button_5.setObjectName("button_5")
        self.numbers.addButton(self.button_5)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(170, 170, 71, 71))
        self.button_6.setObjectName("button_6")
        self.numbers.addButton(self.button_6)
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(10, 250, 71, 71))
        self.button_1.setObjectName("button_1")
        self.numbers.addButton(self.button_1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(90, 250, 71, 71))
        self.button_2.setObjectName("button_2")
        self.numbers.addButton(self.button_2)
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(10, 170, 71, 71))
        self.button_4.setObjectName("button_4")
        self.numbers.addButton(self.button_4)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(170, 250, 71, 71))
        self.button_3.setObjectName("button_3")
        self.numbers.addButton(self.button_3)
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(10, 330, 151, 71))
        self.button_0.setObjectName("button_0")
        self.numbers.addButton(self.button_0)
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(170, 330, 71, 71))
        self.button_clear.setObjectName("button_clear")
        self.numbers.addButton(self.button_clear)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 22))
        self.menubar.setObjectName("menubar")
        self.menuHello = QtWidgets.QMenu(self.menubar)
        self.menuHello.setObjectName("menuHello")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuHello.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_clear.setText(_translate("MainWindow", "C"))
        self.menuHello.setTitle(_translate("MainWindow", "Hello"))