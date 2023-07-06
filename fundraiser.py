# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fundraiser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')

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

conn = sqlite3.connect("authenticate.db")
c = conn.cursor()


class Ui_FundRaiser(object):
#    conn = sqlite3.connect("authenticate.db")
#    c = conn.cursor()
#######################################################################################################################
    def indata1(self):
	n2=self.fund_e_name.text()
	id1=self.fund_e_id.text()
	ar1=self.fund_e_area.text()
	paym1=self.fund_e_paym.text()
	fund1=self.fund_e_amt.text()
	adds1=self.fund_e_state.text()
	n = unicode(n2)
	ids = unicode(id1)
	ar = unicode(ar1)
	paym = unicode(paym1)
	fund = unicode(fund1)
	adds = unicode(adds1)
	connection = sqlite3.connect("authenticate.db")
	connection.execute("INSERT INTO fund_entry VALUES(?,?,?,?,?,?)",[n,ids,ar,paym,fund,adds])
	print("FundRaiser Details Added Successfully..!!")
	connection.commit()
	connection.close()
#######################################################################################################################
    def graphdata(self):
#	connection = sqlite3.connect("authenticate.db")
	c.execute('SELECT id, amount FROM fund_entry')
	idz = []
	amount = []
	for row in c.fetchall():
		print(row[0])
		print(row[1])
#		x = [1,2,3,4,5,6,7,8,9]
#		y = [10,20,30,4,05,0,7,8,100]
		idz.append(row[0])
		amount.append(row[1])
	plt.plot(idz, amount)
	plt.show()		
	c.close()
	conn.close()
#######################################################################################################################
    def setupUi(self, FundRaiser):
        FundRaiser.setObjectName(_fromUtf8("FundRaiser"))
        FundRaiser.resize(881, 487)
        self.gridLayout_2 = QtGui.QGridLayout(FundRaiser)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(FundRaiser)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.paym = QtGui.QLabel(FundRaiser)
        self.paym.setObjectName(_fromUtf8("paym"))
        self.gridLayout.addWidget(self.paym, 3, 0, 1, 1)
        self.name = QtGui.QLabel(FundRaiser)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.fund_e_name = QtGui.QLineEdit(FundRaiser)
        self.fund_e_name.setObjectName(_fromUtf8("fund_e_name"))
        self.gridLayout.addWidget(self.fund_e_name, 0, 2, 1, 1)
        self.state = QtGui.QLabel(FundRaiser)
        self.state.setObjectName(_fromUtf8("state"))
        self.gridLayout.addWidget(self.state, 5, 0, 1, 1)
        self.id = QtGui.QLabel(FundRaiser)
        self.id.setObjectName(_fromUtf8("id"))
        self.gridLayout.addWidget(self.id, 1, 0, 1, 1)
        self.areacovered = QtGui.QLabel(FundRaiser)
        self.areacovered.setObjectName(_fromUtf8("areacovered"))
        self.gridLayout.addWidget(self.areacovered, 2, 0, 1, 1)
        self.fund_e_id = QtGui.QLineEdit(FundRaiser)
        self.fund_e_id.setObjectName(_fromUtf8("fund_e_id"))
        self.gridLayout.addWidget(self.fund_e_id, 1, 2, 1, 1)
        self.fund_e_paym = QtGui.QLineEdit(FundRaiser)
        self.fund_e_paym.setObjectName(_fromUtf8("fund_e_paym"))
        self.gridLayout.addWidget(self.fund_e_paym, 3, 2, 1, 1)
        self.fund_e_area = QtGui.QLineEdit(FundRaiser)
        self.fund_e_area.setObjectName(_fromUtf8("fund_e_area"))
        self.gridLayout.addWidget(self.fund_e_area, 2, 2, 1, 1)
        self.fund_e_state = QtGui.QLineEdit(FundRaiser)
        self.fund_e_state.setObjectName(_fromUtf8("fund_e_state"))
        self.gridLayout.addWidget(self.fund_e_state, 5, 2, 1, 1)
        self.label_2 = QtGui.QLabel(FundRaiser)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.fund_e_amt = QtGui.QLineEdit(FundRaiser)
        self.fund_e_amt.setObjectName(_fromUtf8("fund_e_amt"))
        self.gridLayout.addWidget(self.fund_e_amt, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.fund_add = QtGui.QPushButton(FundRaiser)
        self.fund_add.setObjectName(_fromUtf8("fund_add"))
#####################################################################################################################
	self.fund_add.clicked.connect(self.indata1)
#####################################################################################################################
        self.gridLayout_2.addWidget(self.fund_add, 2, 0, 1, 1)
        self.fund_graph_text = QtGui.QLabel(FundRaiser)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fund_graph_text.sizePolicy().hasHeightForWidth())
        self.fund_graph_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.fund_graph_text.setFont(font)
        self.fund_graph_text.setObjectName(_fromUtf8("fund_graph_text"))
        self.gridLayout_2.addWidget(self.fund_graph_text, 3, 0, 1, 2)
        self.fund_graph = QtGui.QPushButton(FundRaiser)
        self.fund_graph.setObjectName(_fromUtf8("fund_graph"))
#####################################################################################################################
	self.fund_graph.clicked.connect(self.graphdata)
#####################################################################################################################
        self.gridLayout_2.addWidget(self.fund_graph, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(FundRaiser)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi(FundRaiser)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FundRaiser.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FundRaiser.reject)
        QtCore.QMetaObject.connectSlotsByName(FundRaiser)

    def retranslateUi(self, FundRaiser):
        FundRaiser.setWindowTitle(_translate("FundRaiser", "Dialog", None))
        self.label.setText(_translate("FundRaiser", "Fund Raiser", None))
        self.paym.setText(_translate("FundRaiser", "Pay Method", None))
        self.name.setText(_translate("FundRaiser", "Name of organization", None))
        self.state.setText(_translate("FundRaiser", "State", None))
        self.id.setText(_translate("FundRaiser", "Organization ID", None))
        self.areacovered.setText(_translate("FundRaiser", "Area Covered", None))
        self.label_2.setText(_translate("FundRaiser", "Amount Raised", None))
        self.fund_add.setText(_translate("FundRaiser", "Submit", None))
        self.fund_graph_text.setText(_translate("FundRaiser", "Funds raised :", None))
        self.fund_graph.setText(_translate("FundRaiser", "Click here for analysis", None))
#############
#c.close()
#conn.close()
#############


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FundRaiser = QtGui.QDialog()
    ui = Ui_FundRaiser()
    ui.setupUi(FundRaiser)
    FundRaiser.show()
    sys.exit(app.exec_())

