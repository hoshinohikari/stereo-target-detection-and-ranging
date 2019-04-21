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
        Form.resize(474, 201)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(50, 40, 79, 26))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 18))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toolButton = QtWidgets.QToolButton(self.tab_2)
        self.toolButton.setGeometry(QtCore.QRect(420, 20, 21, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_2.setGeometry(QtCore.QRect(420, 70, 21, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 201, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 191, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 110, 421, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 391, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 391, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab_2, "")

        process = os.popen('ls /dev | grep video')
        output = process.read()
        outlist = output.split("\n")
        if (outlist[-1] == ''):
            outlist.pop(-1)
        self.comboBox.addItems(outlist)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(Form.slot1)
        self.comboBox.activated['QString'].connect(Form.slot2)
        self.toolButton.clicked.connect(Form.slot3)
        self.toolButton_2.clicked.connect(Form.slot4)
        self.pushButton_2.clicked.connect(Form.slot5)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Please choose a camera"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Camera Mode"))
        self.toolButton.setText(_translate("Form", "..."))
        self.toolButton_2.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "OutputFile"))
        self.label_3.setText(_translate("Form", "InputFile"))
        self.pushButton_2.setText(_translate("Form", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "InputFile Mode"))

