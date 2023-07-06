# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3



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

class Ui_SignUp(object):
################################################################################################
    def insertdata(self):
	un2=self.s_E_id.text()
	eid1=self.s_E_id_2.text()
	pwd2=self.s_E_pass.text()
	un = unicode(un2)
	eid = unicode(eid1)
	pwd = unicode(pwd2)
	connection = sqlite3.connect("authenticate.db")
	connection.execute("INSERT INTO minipuser VALUES(?,?,?)",[un,eid,pwd])
	print("User Added Successfully..!!")
	connection.commit()
	connection.close()
################################################################################################

    def setupUi(self, SignUp):
        SignUp.setObjectName(_fromUtf8("SignUp"))
        SignUp.resize(451, 380)
        self.gridLayout = QtGui.QGridLayout(SignUp)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.s_acc = QtGui.QLabel(SignUp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s_acc.sizePolicy().hasHeightForWidth())
        self.s_acc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.s_acc.setFont(font)
        self.s_acc.setAlignment(QtCore.Qt.AlignCenter)
        self.s_acc.setObjectName(_fromUtf8("s_acc"))
        self.gridLayout.addWidget(self.s_acc, 0, 0, 1, 2)
        self.s_uname = QtGui.QLabel(SignUp)
        self.s_uname.setObjectName(_fromUtf8("s_uname"))
        self.gridLayout.addWidget(self.s_uname, 1, 0, 1, 1)
        self.s_E_id = QtGui.QLineEdit(SignUp)
        self.s_E_id.setText(_fromUtf8(""))
        self.s_E_id.setObjectName(_fromUtf8("s_E_id"))
        self.gridLayout.addWidget(self.s_E_id, 1, 1, 1, 1)
        self.s_id = QtGui.QLabel(SignUp)
        self.s_id.setObjectName(_fromUtf8("s_id"))
        self.gridLayout.addWidget(self.s_id, 2, 0, 1, 1)
        self.s_E_id_2 = QtGui.QLineEdit(SignUp)
        self.s_E_id_2.setText(_fromUtf8(""))
        self.s_E_id_2.setObjectName(_fromUtf8("s_E_id_2"))
        self.gridLayout.addWidget(self.s_E_id_2, 2, 1, 1, 1)
        self.s_pass = QtGui.QLabel(SignUp)
        self.s_pass.setObjectName(_fromUtf8("s_pass"))
        self.gridLayout.addWidget(self.s_pass, 3, 0, 1, 1)
        self.s_E_pass = QtGui.QLineEdit(SignUp)
        self.s_E_pass.setObjectName(_fromUtf8("s_E_pass"))
        self.gridLayout.addWidget(self.s_E_pass, 3, 1, 1, 1)
        self.s_cracc = QtGui.QPushButton(SignUp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s_cracc.sizePolicy().hasHeightForWidth())
        self.s_cracc.setSizePolicy(sizePolicy)
        self.s_cracc.setObjectName(_fromUtf8("s_cracc"))
################################################################################################
	self.s_cracc.clicked.connect(self.insertdata)	################################################################################################

        self.gridLayout.addWidget(self.s_cracc, 4, 1, 1, 1)

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(_translate("SignUp", "Dialog", None))
        self.s_acc.setText(_translate("SignUp", "Sign Up", None))
        self.s_uname.setText(_translate("SignUp", "User Name", None))
        self.s_id.setText(_translate("SignUp", "Email ID", None))
        self.s_pass.setText(_translate("SignUp", "Password", None))
        self.s_cracc.setText(_translate("SignUp", "Create Account", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SignUp = QtGui.QDialog()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())

