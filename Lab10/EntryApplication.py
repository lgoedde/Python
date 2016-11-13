import sys
import re
from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)
        self.edits = [self.txtFirstName, self.txtLastName, self.txtAddress, self.txtCity, self.txtState, self.txtZip, self.txtEmail]
        self.btnClear.clicked.connect(self.clearScreen)

        for field in self.edits:
            field.textChanged.connect(self.enableBtn)

        self.btnSave.clicked.connect(self.getData)
        self.btnLoad.clicked.connect(self.loadData)

    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """
        with open(filePath, 'r') as f:
            data = f.readlines()

        del data[0:2]
        del data[len(data)-1]
        itemlist = []
        for item in data:
            item = item.split('>')[1].split('<')[0]
            itemlist.append(item)

        self.txtFirstName.setText(itemlist[0])
        self.txtLastName.setText(itemlist[1])
        self.txtAddress.setText(itemlist[2])
        self.txtCity.setText(itemlist[3])
        self.txtState.setText(itemlist[4])
        self.txtZip.setText(itemlist[5])
        self.txtEmail.setText(itemlist[6])

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)

    def clearScreen(self):
        for field in self.edits:
            field.setText('')
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)
        self.lblError.setText('')

    def enableBtn(self):
        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

    def getData(self):
        self.clearError = True
        if self.txtFirstName.text() == '':
            self.lblError.setText('Error: Please enter a first name')
            self.clearError = False
        else:
            self.fname = self.txtFirstName.text()

        if self.txtLastName.text() == '':
            self.lblError.setText('Error: Please enter a last name')

            self.clearError = False
        else:
            self.lname = self.txtLastName.text()

        if self.txtAddress.text() == '':
            self.lblError.setText('Error: Please enter an address')

            self.clearError = False
        else:
            self.address = self.txtAddress.text()

        if self.txtCity.text() == '':
            self.lblError.setText('Error: Please enter a city')
            self.clearError = False
        else:
            self.city = self.txtCity.text()

        if self.txtState.text() == '':
            self.lblError.setText('Error: Please enter a state')

            self.clearError = False
        elif self.txtState.text() not in self.states:
            self.lblError.setText('Error: State is not valid!')
            self.clearError = False
        else:
            self.state = self.txtState.text()

        testz = re.compile(r'[0-9]{5}')
        checkz = re.match(testz,self.txtZip.text())
        if self.txtZip.text() == '':
            self.lblError.setText('Error: Please enter a Zip code')

            self.clearError = False
        elif not checkz:
            self.lblError.setText('Error: Zip code is not valid!')

            self.clearError = False
        else:
            self.zip = self.txtZip.text()


        teste = re.compile(r'\w+@\w+\.\w+')
        checke = re.match(teste,self.txtEmail.text())
        if self.txtEmail.text() == '':
            self.lblError.setText('Error: Please enter an email address')

            self.clearError = False
        elif not checke:
            self.lblError.setText('Error: Email is not valid!')
            self.clearError = False
        else:
            self.email = self.txtEmail.text()

        if self.clearError:
            self.lblError.setText('')
            with open('target.xml', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n<user>\n\t<FirstName>{}</FirstName>\n\t<LastName>{}</LastName>'
                        '\n\t<Address>{}</Address>\n\t<City>{}</City>\n\t<State>{}</State>\n\t<ZIP>{}</ZIP>\n\t<Email>{}'
                        '</Email>\n</user>\n'.format(self.fname,self.lname,self.address,self.city,self.state,self.zip,self.email))


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()
