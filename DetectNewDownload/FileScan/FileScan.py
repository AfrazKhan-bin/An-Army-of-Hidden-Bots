# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtTest
import os,time
# from PyQt4 import QFileDialog, QMessageBox 
# from PyQt4 import QtTest
from PyQt4.QtCore import * 
from PyQt4.QtGui import *

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
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(414, 351)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/logo.png);"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.openFileDialog)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 160, 341, 41))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 120, 111, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 411, 351))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 247, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 280, 101, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2.raise_()
        self.pushButton.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Select File", None))
        self.label.setText(_translate("Dialog", "Path to be followed:", None))
        self.pushButton_2.setText(_translate("Dialog", "Start Scanning", None))

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pathToMonitor = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.textEdit.setText(pathToMonitor)
        self.monitorDirectory(pathToMonitor)

    def monitorDirectory(self,path):
        before = []     #Initial representation of directory
        after = []      #
        for dirpath,dirnames,folder in os.walk(path):
            for eachFile in folder:
                before.append(eachFile)

        while 1:
            added = ""
            removed = ""
            QtTest.QTest.qWait(5000)
            for dirpath,dirnames,folder in os.walk(path):
                for eachFile in folder:
                    after.append(eachFile)

            # print(after)

            for f in after:
                if not f in before:
                    # print (f)
                    added =  added + f + ","

            for f in before:
                if not f in after:
                    # print(f)
                    removed = removed + f + ","

            if added:
                addMessageBox = QMessageBox()
                addMessageBox.setIcon(QMessageBox.Information)
                addMessageBox.setText("Added: " + ", ".join (added))
                addMessageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                addMessageBox.exec_()

                print ("Added: " + "," .join (added))

            if removed:
                removeMessageBox = QMessageBox()
                removeMessageBox.setIcon(QMessageBox.Information)
                removeMessageBox.setText("Removed: " + ", ".join (removed))
                removeMessageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                removeMessageBox.exec_()
                print ("Removed: " + ", ".join (removed))

            before = after
            after = []

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

