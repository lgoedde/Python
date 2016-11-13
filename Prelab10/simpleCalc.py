#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-11-09 16:58:33 -0500 (Mon, 09 Nov 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab10/simpleCalc.py $
#$Revision: 83210 $

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class Calculator(QMainWindow, Ui_MyCalculator):

    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setupUi(self)

        self.buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,
                        self.btn9]
        self.math = [self.btnDiv,self.btnMinus,self.btnPlus,self.btnMul]

        self.output.setText('')
        self.btnClear.clicked.connect(self.clearDisplay)
        self.btnEq.clicked.connect(self.checkEq)
        self.btnDec.clicked.connect(self.displayDec)
        self.checkSep.stateChanged.connect(self.displaySep)

        self.spinDigits.valueChanged.connect(self.digHelper)

        self.op = 0
        self.clearFlag = False

        for button in self.buttons:
            button.clicked.connect(self.displayNum)

        for func in self.math:
            func.clicked.connect(self.checkFuncs)


    def displayNum(self):
        if (self.clearFlag):
            self.clearDisplay()
            self.clearFlag = False

        button = self.sender()
        check = self.output.text().replace(',','')
        check = check.replace('.','')
        if len(check) < 12:
            val = self.output.text() + button.text()
            self.output.setText(val)
        else:
            pass


    def clearDisplay(self):
        self.output.clear()
        self.output.setText('')

    def displayDec(self):
        val = self.output.text().replace(',','')
        if '.' not in val:
            val += '.'
            self.output.setText(val)

    def checkFuncs(self):
        func = self.sender()
        self.prev = float(self.output.text().replace(',',''))
        self.output.clear()
        if func == self.btnDiv:
            self.op = 1

        if func == self.btnMul:
            self.op = 2

        if func == self.btnPlus:
            self.op = 3

        if func == self.btnMinus:
            self.op = 4

    def displaySep(self):
        if self.checkSep.isChecked():
            if self.output.text() != '':
                currVal = float(self.output.text())
                self.displayDigits(currVal)
        else:
            if self.output.text() != '':
                try:
                    currVal = float(self.output.text())
                except:
                    currVal = float(self.output.text().replace(',',''))
                finally:
                    self.displayDigits(currVal)

    def digHelper(self):
        val = self.output.text().replace(',','')
        if val != '':
            val = float(val)
            self.displayDigits(val)

    def displayDigits(self,currVal):
        self.digits = self.spinDigits.value()

        if currVal != '':
            if self.checkSep.isChecked():
                formatStr = '{0:,.{1}f}'.format(currVal,self.digits)
                self.output.setText(formatStr)
            else:
                formatStr = '{0:.{1}f}'.format(currVal,self.digits)
                self.output.setText(formatStr)

    def checkEq(self):
        currVal = float(self.output.text().replace(',',''))
        self.clearFlag = True

        if self.op == 1:
            try:
                final = self.prev / currVal
                self.displayDigits(final)
            except:
                self.output.setText("Error: Cannot divide by zero =)")
        if self.op == 2:
            final = self.prev * currVal
            self.displayDigits(final)
        if self.op == 3:
            final = self.prev + currVal
            self.displayDigits(final)
        if self.op == 4:
            final = self.prev - currVal
            self.displayDigits(final)
        #self.output.setText(str(final))



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Calculator()

    currentForm.show()
    currentApp.exec_()