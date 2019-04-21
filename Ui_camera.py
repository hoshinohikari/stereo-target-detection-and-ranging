# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hoshino/program/Qt/test/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 367)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 30, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 30, 79, 26))
        self.comboBox.setObjectName("comboBox")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 100, 421, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 191, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 57, 18))
        self.label_2.setObjectName("label_2")

        process = os.popen('ls /dev | grep video')
        output = process.read()
        outlist = output.split("\n")
        if (outlist[-1] == ''):
            outlist.pop(-1)
        self.comboBox.addItems(outlist)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.slot1)
        self.comboBox.activated['QString'].connect(Form.slot2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.label.setText(_translate("Form", "Please choose a camera"))
        self.label_2.setText(_translate("Form", "Log"))
