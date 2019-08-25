# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idiom_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 401)
        self.lblIdiom = QtWidgets.QLabel(Form)
        self.lblIdiom.setGeometry(QtCore.QRect(40, 50, 151, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIdiom.sizePolicy().hasHeightForWidth())
        self.lblIdiom.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblIdiom.setFont(font)
        self.lblIdiom.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lblIdiom.setObjectName("lblIdiom")
        self.lblName1 = QtWidgets.QLabel(Form)
        self.lblName1.setGeometry(QtCore.QRect(40, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblName1.setFont(font)
        self.lblName1.setObjectName("lblName1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 170, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lblName2 = QtWidgets.QLabel(Form)
        self.lblName2.setGeometry(QtCore.QRect(270, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblName2.setFont(font)
        self.lblName2.setObjectName("lblName2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(260, 40, 261, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(60, 310, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "成语接龙"))
        self.lblIdiom.setText(_translate("Form", "成语"))
        self.lblName1.setText(_translate("Form", "接龙："))
        self.lineEdit.setText(_translate("Form", "成语"))
        self.lblName2.setText(_translate("Form", "答题记录："))
        self.pushButton.setText(_translate("Form", "回答"))
        self.cancelButton.setText(_translate("Form", "放弃"))

