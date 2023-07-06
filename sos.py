# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sos.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from victims import Ui_Victims
from volunteers import Ui_Volunteers
from fundraiser import Ui_FundRaiser
from donors import Ui_Donors
from ngo import Ui_NGOs

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

class Ui_SOS(object):
###########################################################################################################
    def victimCheck(self):
	print("Victim button clicked")
	self.victimsWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_Victims()		
	self.ui.setupUi(self.victimsWindow)
	self.victimsWindow.show()
    def volCheck(self):
	print("Volunteer button clicked")
	self.volunteersWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_Volunteers()		
	self.ui.setupUi(self.volunteersWindow)
	self.volunteersWindow.show()
    def donCheck(self):
	print("Donor button clicked")
	self.donorsWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_Donors()		
	self.ui.setupUi(self.donorsWindow)
	self.donorsWindow.show()
    def ngoCheck(self):
	print("NGOs button clicked")
	self.ngoWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_NGOs()		
	self.ui.setupUi(self.ngoWindow)
	self.ngoWindow.show()
    def funCheck(self):
	print("FundRaiser button clicked")
	self.fundraiserWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_FundRaiser()		
	self.ui.setupUi(self.fundraiserWindow)
	self.fundraiserWindow.show()
###########################################################################################################	
    def setupUi(self, SOS):
        SOS.setObjectName(_fromUtf8("SOS"))
        SOS.resize(692, 267)
        self.gridLayout = QtGui.QGridLayout(SOS)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mw_pain = QtGui.QLabel(SOS)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mw_pain.sizePolicy().hasHeightForWidth())
        self.mw_pain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mw_pain.setFont(font)
        self.mw_pain.setAlignment(QtCore.Qt.AlignCenter)
        self.mw_pain.setObjectName(_fromUtf8("mw_pain"))
	self.gridLayout.addWidget(self.mw_pain, 2, 1, 1, 3)
        self.mw_vic = QtGui.QPushButton(SOS)
        self.mw_vic.setObjectName(_fromUtf8("mw_vic"))
        #######################################################################################################
	self.mw_vic.clicked.connect(self.victimCheck)
	#######################################################################################################
        self.gridLayout.addWidget(self.mw_vic, 1, 0, 1, 1)
        self.mw_vol = QtGui.QPushButton(SOS)
        self.mw_vol.setObjectName(_fromUtf8("mw_vol"))
        #######################################################################################################
	self.mw_vol.clicked.connect(self.volCheck)
	#######################################################################################################
	self.gridLayout.addWidget(self.mw_vol, 1, 1, 1, 1)
        self.mw_don = QtGui.QPushButton(SOS)
        self.mw_don.setObjectName(_fromUtf8("mw_don"))
	#######################################################################################################
	self.mw_don.clicked.connect(self.donCheck)
	#######################################################################################################
        self.gridLayout.addWidget(self.mw_don, 1, 3, 1, 1)
        self.mw_ngo = QtGui.QPushButton(SOS)
        self.mw_ngo.setObjectName(_fromUtf8("mw_ngo"))
	#######################################################################################################
	self.mw_ngo.clicked.connect(self.ngoCheck)
	#######################################################################################################
        self.gridLayout.addWidget(self.mw_ngo, 1, 4, 1, 1)
        self.mw_sos = QtGui.QLabel(SOS)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mw_sos.sizePolicy().hasHeightForWidth())
        self.mw_sos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(30)
        self.mw_sos.setFont(font)
        self.mw_sos.setAlignment(QtCore.Qt.AlignCenter)
        self.mw_sos.setObjectName(_fromUtf8("mw_sos"))
        self.gridLayout.addWidget(self.mw_sos, 0, 1, 1, 3)
        self.mw_fun = QtGui.QPushButton(SOS)
        self.mw_fun.setObjectName(_fromUtf8("mw_fun"))
	#######################################################################################################
	self.mw_fun.clicked.connect(self.funCheck)
	#######################################################################################################
        self.gridLayout.addWidget(self.mw_fun, 1, 2, 1, 1)

        self.retranslateUi(SOS)
        QtCore.QMetaObject.connectSlotsByName(SOS)

    def retranslateUi(self, SOS):
        SOS.setWindowTitle(_translate("SOS", "Dialog", None))
        self.mw_pain.setText(_translate("SOS", "We know the Importance of your loved ones..!!", None))
        self.mw_vic.setText(_translate("SOS", "Victim", None))
        self.mw_vol.setText(_translate("SOS", "Volunteers", None))
        self.mw_don.setText(_translate("SOS", "Donor", None))
        self.mw_ngo.setText(_translate("SOS", "NGOs", None))
        self.mw_sos.setText(_translate("SOS", "SOS", None))
        self.mw_fun.setText(_translate("SOS", "FundRaiser", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SOS = QtGui.QDialog()
    ui = Ui_SOS()
    ui.setupUi(SOS)
    SOS.show()
    sys.exit(app.exec_())

