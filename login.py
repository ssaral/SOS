# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from sos import Ui_SOS 
from signup import Ui_SignUp
from reset import Ui_res_password

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

    def loginCheck(self):
	un1=self.l_E_id.text()
	pwd1=self.l_E_pass.text()
	un = unicode(un1)
	pwd = unicode(pwd1)
	connection = sqlite3.connect("authenticate.db")
	result=connection.execute("SELECT * FROM minipuser where USERNAME=? and PASSWORD=?",[un,pwd])
	if( len(result.fetchall())>0):
		print("User Found.")
		print("Successfully Logged-In.")
		self.sosWindow=QtGui.QDialog() #object of new window
		self.ui= Ui_SOS()		
		self.ui.setupUi(self.sosWindow)
		self.sosWindow.show()
	else:
		print("User Not Found.")
		print("ID or Password Maybe Wrong. ")
#	self.showMessageBox('Warning','Invalid Username or Password' )
#######################################################################################################################
    def signinCheck(self):
	print("Sign-in button clicked")
	self.signupWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_SignUp()		
	self.ui.setupUi(self.signupWindow)
	self.signupWindow.show()
#######################################################################################################################
    def pass_reset(self):
	print("Password Option Initiated")
	self.resetWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_res_password()		
	self.ui.setupUi(self.resetWindow)
	self.resetWindow.show()
#######################################################################################################################
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(494, 401)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.l_sign_up = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_sign_up.sizePolicy().hasHeightForWidth())
        self.l_sign_up.setSizePolicy(sizePolicy)
        self.l_sign_up.setObjectName(_fromUtf8("l_sign_up"))
#######################################################################################################################
        self.l_sign_up.clicked.connect(self.signinCheck)
#######################################################################################################################
        self.gridLayout_3.addWidget(self.l_sign_up, 3, 1, 1, 1)
        self.l_e_id = QtGui.QLabel(Dialog)
        self.l_e_id.setObjectName(_fromUtf8("l_e_id"))
        self.gridLayout_3.addWidget(self.l_e_id, 1, 0, 1, 1)
        self.l_E_id = QtGui.QLineEdit(Dialog)
        self.l_E_id.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_E_id.sizePolicy().hasHeightForWidth())
        self.l_E_id.setSizePolicy(sizePolicy)
        self.l_E_id.setText(_fromUtf8(""))
        self.l_E_id.setObjectName(_fromUtf8("l_E_id"))
        self.gridLayout_3.addWidget(self.l_E_id, 1, 1, 1, 1)
        self.l_E_pass = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_E_pass.sizePolicy().hasHeightForWidth())
        self.l_E_pass.setSizePolicy(sizePolicy)
        self.l_E_pass.setText(_fromUtf8(""))
        self.l_E_pass.setObjectName(_fromUtf8("l_E_pass"))
	self.l_E_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout_3.addWidget(self.l_E_pass, 2, 1, 1, 1)
        self.l_log_in = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_log_in.sizePolicy().hasHeightForWidth())
        self.l_log_in.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(31)
        font.setBold(False)
        font.setWeight(50)
        self.l_log_in.setFont(font)
        self.l_log_in.setTextFormat(QtCore.Qt.AutoText)
        self.l_log_in.setAlignment(QtCore.Qt.AlignCenter)
        self.l_log_in.setObjectName(_fromUtf8("l_log_in"))
        self.gridLayout_3.addWidget(self.l_log_in, 0, 0, 1, 2)
        self.l_pass = QtGui.QLabel(Dialog)
        self.l_pass.setObjectName(_fromUtf8("l_pass"))
        self.gridLayout_3.addWidget(self.l_pass, 2, 0, 1, 1)
        self.l_login = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_login.sizePolicy().hasHeightForWidth())
        self.l_login.setSizePolicy(sizePolicy)
        self.l_login.setObjectName(_fromUtf8("l_login"))
#######################################################################################################################
        self.l_login.clicked.connect(self.loginCheck)
#######################################################################################################################
        self.gridLayout_3.addWidget(self.l_login, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#######################################################################################################################
        self.pushButton.clicked.connect(self.pass_reset)
#######################################################################################################################
        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.l_sign_up.setText(_translate("Dialog", "SignUp", None))
        self.l_e_id.setText(_translate("Dialog", "User ID", None))
        self.l_log_in.setText(_translate("Dialog", "          Login", None))
        self.l_pass.setText(_translate("Dialog", "Password", None))
        self.l_login.setText(_translate("Dialog", "Login", None))
        self.pushButton.setText(_translate("Dialog", "Click if you Forgot Your Password.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

