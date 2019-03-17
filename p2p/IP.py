# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IP.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IP(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(366, 176)
        Dialog.setStyleSheet(_fromUtf8("background-color:#68b740;\n"
"font:13px;\n"
"\n"
"\n"
""))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(110, 60, 131, 31))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 60, 31, 21))
        self.label.setStyleSheet(_fromUtf8("font:20px;\n"
"font-weight: bold;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.AddButton = QtGui.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(230, 120, 75, 23))
        self.AddButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
""))
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.AddButton.clicked.connect(self.getText)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "IP:", None))
        self.AddButton.setText(_translate("Dialog", "Add IP", None))

    def getText(self):
        IP = self.textEdit.toPlainText()
        result = self.checkIP(IP)
        if(result == True):
            with open("peers.txt","a+") as f:
                f.write("\n" + IP)
                f.close()
        else:
            print ("Error")

    def checkIP(self,IP):
        values = IP.split('.')
        if (len(values) == 4):
            try:
                socket.inet_aton(IP)
                self.showPropmpt("Valid")
                return True
            except socket.error:
                self.showPropmpt("Invalid")
                return False
        else:
            self.showPropmpt("Invalid")
            return False


    def showPropmpt(self,type):
        message = QtGui.QMessageBox()
        if(type == "Valid"):
            message.setIcon(QtGui.QMessageBox.Information)
            message.setWindowTitle("IP Added")
            message.setText("IP has been added successfully.")
        else:
            message.setIcon(QtGui.QMessageBox.Critical)
            message.setWindowTitle("Invalid IP")
            message.setText("Please enter a valid IP.")
        message.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        message.exec_()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_IP()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

