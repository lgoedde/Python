# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Sun Nov  8 14:11:55 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MyCalculator(object):
    def setupUi(self, MyCalculator):
        MyCalculator.setObjectName("MyCalculator")
        MyCalculator.resize(622, 388)
        self.centralwidget = QtGui.QWidget(MyCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.btn7 = QtGui.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(20, 100, 92, 27))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtGui.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(130, 100, 92, 27))
        self.btn8.setObjectName("btn8")
        self.btn9 = QtGui.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(240, 100, 92, 27))
        self.btn9.setObjectName("btn9")
        self.btnDiv = QtGui.QPushButton(self.centralwidget)
        self.btnDiv.setGeometry(QtCore.QRect(350, 100, 92, 27))
        self.btnDiv.setObjectName("btnDiv")
        self.btn5 = QtGui.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(130, 140, 92, 27))
        self.btn5.setObjectName("btn5")
        self.btnMul = QtGui.QPushButton(self.centralwidget)
        self.btnMul.setGeometry(QtCore.QRect(350, 140, 92, 27))
        self.btnMul.setObjectName("btnMul")
        self.btn6 = QtGui.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(240, 140, 92, 27))
        self.btn6.setObjectName("btn6")
        self.btn4 = QtGui.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(20, 140, 92, 27))
        self.btn4.setObjectName("btn4")
        self.btn2 = QtGui.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(130, 180, 92, 27))
        self.btn2.setObjectName("btn2")
        self.btnMinus = QtGui.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(350, 180, 92, 27))
        self.btnMinus.setObjectName("btnMinus")
        self.btn3 = QtGui.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(240, 180, 92, 27))
        self.btn3.setObjectName("btn3")
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(20, 180, 92, 27))
        self.btn1.setObjectName("btn1")
        self.btn0 = QtGui.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(20, 220, 201, 27))
        self.btn0.setObjectName("btn0")
        self.btnDec = QtGui.QPushButton(self.centralwidget)
        self.btnDec.setGeometry(QtCore.QRect(240, 220, 92, 27))
        self.btnDec.setObjectName("btnDec")
        self.btnPlus = QtGui.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(350, 220, 92, 27))
        self.btnPlus.setObjectName("btnPlus")
        self.checkSep = QtGui.QCheckBox(self.centralwidget)
        self.checkSep.setGeometry(QtCore.QRect(380, 290, 221, 22))
        self.checkSep.setObjectName("checkSep")
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(490, 100, 92, 71))
        self.btnClear.setObjectName("btnClear")
        self.btnEq = QtGui.QPushButton(self.centralwidget)
        self.btnEq.setGeometry(QtCore.QRect(490, 180, 92, 71))
        self.btnEq.setObjectName("btnEq")
        self.spinDigits = QtGui.QSpinBox(self.centralwidget)
        self.spinDigits.setGeometry(QtCore.QRect(40, 280, 55, 27))
        self.spinDigits.setMaximum(5)
        self.spinDigits.setObjectName("spinDigits")
        self.output = QtGui.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 10, 571, 71))
        self.output.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")
        MyCalculator.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MyCalculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 25))
        self.menubar.setObjectName("menubar")
        MyCalculator.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MyCalculator)
        self.statusbar.setObjectName("statusbar")
        MyCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(MyCalculator)
        QtCore.QMetaObject.connectSlotsByName(MyCalculator)

    def retranslateUi(self, MyCalculator):
        MyCalculator.setWindowTitle(QtGui.QApplication.translate("MyCalculator", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn7.setText(QtGui.QApplication.translate("MyCalculator", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.btn8.setText(QtGui.QApplication.translate("MyCalculator", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.btn9.setText(QtGui.QApplication.translate("MyCalculator", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDiv.setText(QtGui.QApplication.translate("MyCalculator", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.btn5.setText(QtGui.QApplication.translate("MyCalculator", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMul.setText(QtGui.QApplication.translate("MyCalculator", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.btn6.setText(QtGui.QApplication.translate("MyCalculator", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.btn4.setText(QtGui.QApplication.translate("MyCalculator", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.btn2.setText(QtGui.QApplication.translate("MyCalculator", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMinus.setText(QtGui.QApplication.translate("MyCalculator", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btn3.setText(QtGui.QApplication.translate("MyCalculator", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.btn1.setText(QtGui.QApplication.translate("MyCalculator", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btn0.setText(QtGui.QApplication.translate("MyCalculator", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDec.setText(QtGui.QApplication.translate("MyCalculator", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlus.setText(QtGui.QApplication.translate("MyCalculator", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSep.setText(QtGui.QApplication.translate("MyCalculator", "Display Thousands\' Separator", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("MyCalculator", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEq.setText(QtGui.QApplication.translate("MyCalculator", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.output.setText(QtGui.QApplication.translate("MyCalculator", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
