# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(635, 165)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 321, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(150, 100, 321, 30))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(490, 100, 93, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 20, 93, 30))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(160, 70, 60, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 70, 60, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(150, 50, 151, 41))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(320, 70, 151, 19))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查找"))
        self.pushButton_1.setText(_translate("Form", "替换"))
        self.pushButton.setText(_translate("Form", "查找下一个"))
        self.radioButton.setText(_translate("Form", "向上"))
        self.radioButton_2.setText(_translate("Form", "向下"))
        self.groupBox.setTitle(_translate("Form", "查找方向"))
        self.label.setText(_translate("Form", "查找："))
        self.label_2.setText(_translate("Form", "替换为："))
        self.checkBox.setText(_translate("Form", "区分大小写"))
