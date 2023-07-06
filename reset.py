# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reset.ui'
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

class Ui_res_password(object):
##############################################################################################
    def resetpass(self):
	un2=self.uesr_entry.text()
	eid1=self.email_entry.text()
	un = unicode(un2)
	eid = unicode(eid1)
	connection = sqlite3.connect("authenticate.db")
	connection.execute("DELETE FROM minipuser WHERE USERNAME=(?)",[un])
	print("PASSWORD reset is successfull..!!")
	connection.commit()
	connection.close()
################################################################################################
    def setupUi(self, res_password):
        res_password.setObjectName(_fromUtf8("res_password"))
        res_password.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(res_password)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(res_password)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(res_password)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.reset_pass = QtGui.QPushButton(res_password)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_pass.sizePolicy().hasHeightForWidth())
        self.reset_pass.setSizePolicy(sizePolicy)
        self.reset_pass.setObjectName(_fromUtf8("reset_pass"))
##############################################################################################
        self.reset_pass.clicked.connect(self.resetpass)        ##############################################################################################
        self.gridLayout.addWidget(self.reset_pass, 2, 0, 1, 1)
        self.email_entry = QtGui.QLineEdit(res_password)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_entry.sizePolicy().hasHeightForWidth())
        self.email_entry.setSizePolicy(sizePolicy)
        self.email_entry.setObjectName(_fromUtf8("email_entry"))
        self.gridLayout.addWidget(self.email_entry, 1, 1, 1, 1)
        self.uesr_entry = QtGui.QLineEdit(res_password)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uesr_entry.sizePolicy().hasHeightForWidth())
        self.uesr_entry.setSizePolicy(sizePolicy)
        self.uesr_entry.setObjectName(_fromUtf8("uesr_entry"))
        self.gridLayout.addWidget(self.uesr_entry, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(res_password)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(res_password)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)

        self.retranslateUi(res_password)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), res_password.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), res_password.reject)
        QtCore.QMetaObject.connectSlotsByName(res_password)

    def retranslateUi(self, res_password):
        res_password.setWindowTitle(_translate("res_password", "Dialog", None))
        self.label.setText(_translate("res_password", "Reset Your Password", None))
        self.reset_pass.setText(_translate("res_password", "Reset Password", None))
        self.label_3.setText(_translate("res_password", "UserName", None))
        self.label_2.setText(_translate("res_password", "EmailID", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    res_password = QtGui.QDialog()
    ui = Ui_res_password()
    ui.setupUi(res_password)
    res_password.show()
    sys.exit(app.exec_())

