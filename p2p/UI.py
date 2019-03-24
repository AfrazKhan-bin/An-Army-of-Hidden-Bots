# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from IP import Ui_IP
import sig_tool as tool
from queue import Queue
import threading,time

intThreads = 2
arrJobs = [1, 2]
queue = Queue()

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

class Ui_Dialog(object):

    # def __init__(self):
    #     self.label = QtGui.QLabel(self.frame)
    #     self.logo_image = QtGui.QWidget(self.frame)
    #     self.pushButton_2 = QtGui.QPushButton(self.frame)
    #     self.pushButton = QtGui.QPushButton(self.frame)
    #     self.label_3 = QtGui.QLabel(self.frame)
    #     self.scrollArea_2 = QtGui.QScrollArea(self.frame)
    #     self.status = QtGui.QFrame(self.frame)
    #     self.scrollArea = QtGui.QScrollArea(self.frame)
    #     self.label_2 = QtGui.QLabel(self.frame)
    #     self.label = QtGui.QLabel(self.frame)


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(607, 350)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 611, 351))
        self.frame.setStyleSheet(_fromUtf8("background-color:#68b740;\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.listOfNodes = QtGui.QTextEdit()
        self.lisOfTransactions = QtGui.QTextEdit(self.frame)
        self.label = QtGui.QLabel(self.frame)
        self.logo_image = QtGui.QWidget(self.frame)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.label_3 = QtGui.QLabel(self.frame)
        self.scrollArea_2 = QtGui.QScrollArea(self.frame)
        self.status = QtGui.QFrame(self.frame)
        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 20, 361, 41))
        self.label.setStyleSheet(_fromUtf8("Font-size:25px;\n"
"Font-family:verdana;\n"
"Font-weight:900;\n"
"color:white;\n"
"padding: 5px;\n"
"border: 1px solid white;\n"
"border-radius:5px; \n"
"\n"
"\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2.setGeometry(QtCore.QRect(420, 80, 151, 41))
        self.label_2.setStyleSheet(_fromUtf8("Font-size:20px;\n"
"Font-family:verdana;\n"
"Font-weight:900;\n"
"color:white;\n"
"color:#e6fc6f;\n"
"text-decoration:underline;\n"
"\n"
"\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea.setGeometry(QtCore.QRect(410, 120, 181, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 219))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.getListOfTransactions()
        self.scrollArea.setWidget(self.lisOfTransactions)
        self.status.setGeometry(QtCore.QRect(10, 310, 391, 31))
        self.status.setStyleSheet(_fromUtf8("background-color:#e6f28e;\n"
"opacity:70%;"))
        self.status.setFrameShape(QtGui.QFrame.StyledPanel)
        self.status.setFrameShadow(QtGui.QFrame.Raised)
        self.status.setObjectName(_fromUtf8("status"))
        self.scrollArea_2.setGeometry(QtCore.QRect(220, 120, 181, 181))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 179, 179))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.getListOfNodes()
        self.scrollArea_2.setWidget(self.listOfNodes)
        self.label_3.setGeometry(QtCore.QRect(250, 85, 121, 31))
        self.label_3.setStyleSheet(_fromUtf8("Font-size:20px;\n"
"Font-family:verdana;\n"
"Font-weight:900;\n"
"color:white;\n"
"color:#e6fc6f;\n"
"text-decoration:underline;\n"
"\n"
"\n"
""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 171, 51))
        self.pushButton.setStyleSheet(_fromUtf8("Font-size:14px;\n"
"font-family:verdana;\n"
"color:white;\n"
"font-weight:bold;\n"
"border: 1px solid white;\n"
"background-color:#7fcc4d\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.SelectNewFile)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 230, 171, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("Font-size:14px;\n"
"font-family:verdana;\n"
"color:white;\n"
"font-weight:bold;\n"
"border: 1px solid white;\n"
"background-color:#7fcc4d\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.showIPWindow)
        self.logo_image.setGeometry(QtCore.QRect(40, 10, 141, 131))
        self.logo_image.setStyleSheet(_fromUtf8(""))
        self.logo_image.setObjectName(_fromUtf8("logo_image"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "ARMY of HIDDEN BOTs", None))
        self.label_2.setText(_translate("Dialog", "Transactions", None))
        self.label_3.setText(_translate("Dialog", "All Nodes", None))
        self.pushButton.setText(_translate("Dialog", "Update Antivirus", None))
        self.pushButton_2.setText(_translate("Dialog", "Add New Node", None))

    def showIPWindow(self):
        self.secondwindow=QtGui.QDialog()
        self.ui=Ui_IP()
        self.ui.setupUi(self.secondwindow)
        self.secondwindow.show()
        print ("Back here")
        self.getListOfNodes()

    def SelectNewFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(None,'OpenFile')
        if filename:
            hashedString = tool.hash_file(filename)
            result = tool.checkSignature(hashedString)
            if(result == False):
                with open("signatures.txt","a+") as f:
                    f.write("\n" + hashedString)
                    f.close()
            self.showPrompt()

    def showPrompt(self):
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Information)
        message.setWindowTitle("Success")
        message.setText("Signature has been added successfully.")
        message.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        message.exec_()
        self.getListOfTransactions()

    def getListOfNodes(self):
        with open("peers.txt",'r') as f:
            listOfIPs = f.readlines()
            # print (listOfIPs)
            f.close()

        self.listOfNodes.setPlainText("")
        for each in listOfIPs:
            self.listOfNodes.setPlainText(self.listOfNodes.toPlainText() + each)

    def getListOfTransactions(self):
        with open("Transactions.txt") as f:
            allTransactions = f.readlines()
            f.close()

        self.lisOfTransactions.setPlainText("")
        for each in allTransactions:
            self.lisOfTransactions.append(each)
  
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())