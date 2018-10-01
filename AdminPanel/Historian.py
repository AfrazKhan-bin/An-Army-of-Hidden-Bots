# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Historian.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import ntpath

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
        Dialog.resize(709, 342)
        Dialog.setStyleSheet(_fromUtf8("font-size:30px;"))
        self.scrollArea_2 = QtGui.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(360, 30, 321, 291))
        self.scrollArea_2.setStyleSheet(_fromUtf8("Background-Color: rgb(61, 60, 60);\n"
"border: 5px solid rgb(97, 98, 85);\n"
"border-radius: 15px;"))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 311, 281))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setStyleSheet(_fromUtf8("font-size:15px;"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("arial"))
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color : Brown;\n"
"font-family: arial;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 280, 181, 51))
        self.pushButton.clicked.connect(self.selectFile)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-Color:gray;\n"
"border: 2px solid black;\n"
"color: white"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 171, 171))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(_fromUtf8("Background-Color: rgb(247, 255, 166);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 240, 171, 31))
        self.label_3.setStyleSheet(_fromUtf8("font-Size:30px;\n"
"color: black;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(480, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("Font-Size:15px;\n"
"color:rgb(106, 35, 12)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Historian", None))
        self.label.setText(_translate("Dialog", "Admin Panel", None))
        self.pushButton.setText(_translate("Dialog", "Open a User", None))
        self.label_3.setText(_translate("Dialog", "Name", None))
        self.label_4.setText(_translate("Dialog", "History of User", None))
    
    def selectFile(self):
        image = QtGui.QFileDialog.getOpenFileName(None,'OpenFile','C:\\Users\\Hassan\\Pictures\\Screenshots',"Image file(*.png *.jpg)")
        image = str(image)     

        #directory name of image
        dirName = os.path.dirname(image) 
        #just image name with excluding directory path
        imageName = ntpath.basename(image)

        #image name without extension
        personName =  os.path.splitext(imageName)[0]
        
        if image:
                self.label_3.setText(personName)
                self.label_2.setPixmap(QtGui.QPixmap(image).
                                        scaled(self.label_2.width(),
                                                self.label_2.height()))
        
                textFileName = dirName + "\\" + personName + ".txt"
                with open(textFileName,'r') as f:
                        content = f.read()
                        f.close()

                self.label_5.setText(str(content))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

