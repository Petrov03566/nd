# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_Defective.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class  Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 349)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_name_pr = QtWidgets.QLineEdit(Form)
        self.lineEdit_name_pr.setGeometry(QtCore.QRect(10, 50, 300, 30))
        self.lineEdit_name_pr.setObjectName("lineEdit_name_pr")
        self.lineEdit_break = QtWidgets.QLineEdit(Form)
        self.lineEdit_break.setGeometry(QtCore.QRect(20, 130, 300, 30))
        self.lineEdit_break.setObjectName("lineEdit_break")
        self.lineEdit_flaw = QtWidgets.QLineEdit(Form)
        self.lineEdit_flaw.setGeometry(QtCore.QRect(10, 200, 310, 30))
        self.lineEdit_flaw.setObjectName("lineEdit_flaw")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_add_pr = QtWidgets.QPushButton(Form)
        self.pushButton_add_pr.setGeometry(QtCore.QRect(10, 260, 100, 40))
        self.pushButton_add_pr.setObjectName("pushButton_add_pr")
        self.pushButton_cansel_pr = QtWidgets.QPushButton(Form)
        self.pushButton_cansel_pr.setGeometry(QtCore.QRect(190, 260, 110, 40))
        self.pushButton_cansel_pr.setObjectName("pushButton_cansel_pr")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление данных неисправном "))
        self.label_2.setText(_translate("Form", "имя принтера"))
        self.label_3.setText(_translate("Form", "поломка"))
        self.label_4.setText(_translate("Form", "недостаток"))
        self.pushButton_add_pr.setText(_translate("Form", "добавить "))
        self.pushButton_cansel_pr.setText(_translate("Form", "отмена"))
