# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'donors.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
import matplotlib.pyplot as plt
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

class Ui_Donors(object):
#######################################################################################################################
    def indata3(self):
	n4=self.don_e_name.text()
	amt2=self.don_e_amt.text()
	mob3=self.don_e_mobno.text()
	paym2=self.don_e_paym.text()
	adds2=self.don_e_state.text()
	n = unicode(n4)
	amt = unicode(amt2)
	mob = unicode(mob3)
	paym = unicode(paym2)
	adds = unicode(adds2)
	connection = sqlite3.connect("authenticate.db")
	connection.execute("INSERT INTO donors_entry VALUES(?,?,?,?,?)",[n,amt,mob,paym,adds])
	print("Donor Details Added Successfully..!!")
	connection.commit()
	connection.close()
#######################################################################################################################
    def graphdata1(self):
#	connection = sqlite3.connect("authenticate.db")
	c.execute('SELECT mob_no, amount FROM donors_entry')
	mbn = []
	amount = []
	for row in c.fetchall():
		print(row[0])
		print(row[1])
#		x = [1,2,3,4,5,6,7,8,9]
#		y = [10,20,30,4,05,0,7,8,100]
		mbn.append(row[0])
		amount.append(row[1])
	plt.plot(mbn, amount)
	plt.show()		
	c.close()
	conn.close()
#######################################################################################################################

    def setupUi(self, Donors):
        Donors.setObjectName(_fromUtf8("Donors"))
        Donors.resize(861, 417)
        self.gridLayout_2 = QtGui.QGridLayout(Donors)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(Donors)
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
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.paymethod = QtGui.QLabel(Donors)
        self.paymethod.setObjectName(_fromUtf8("paymethod"))
        self.gridLayout.addWidget(self.paymethod, 3, 0, 1, 1)
        self.name = QtGui.QLabel(Donors)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.don_e_name = QtGui.QLineEdit(Donors)
        self.don_e_name.setObjectName(_fromUtf8("don_e_name"))
        self.gridLayout.addWidget(self.don_e_name, 0, 2, 1, 1)
        self.state = QtGui.QLabel(Donors)
        self.state.setObjectName(_fromUtf8("state"))
        self.gridLayout.addWidget(self.state, 4, 0, 1, 1)
        self.amount = QtGui.QLabel(Donors)
        self.amount.setObjectName(_fromUtf8("amount"))
        self.gridLayout.addWidget(self.amount, 1, 0, 1, 1)
        self.mobno = QtGui.QLabel(Donors)
        self.mobno.setObjectName(_fromUtf8("mobno"))
        self.gridLayout.addWidget(self.mobno, 2, 0, 1, 1)
        self.don_e_amt = QtGui.QLineEdit(Donors)
        self.don_e_amt.setObjectName(_fromUtf8("don_e_amt"))
        self.gridLayout.addWidget(self.don_e_amt, 1, 2, 1, 1)
        self.don_e_paym = QtGui.QLineEdit(Donors)
        self.don_e_paym.setObjectName(_fromUtf8("don_e_paym"))
        self.gridLayout.addWidget(self.don_e_paym, 3, 2, 1, 1)
        self.don_e_mobno = QtGui.QLineEdit(Donors)
        self.don_e_mobno.setObjectName(_fromUtf8("don_e_mobno"))
        self.gridLayout.addWidget(self.don_e_mobno, 2, 2, 1, 1)
        self.don_e_state = QtGui.QLineEdit(Donors)
        self.don_e_state.setObjectName(_fromUtf8("don_e_state"))
        self.gridLayout.addWidget(self.don_e_state, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.don_add = QtGui.QPushButton(Donors)
        self.don_add.setObjectName(_fromUtf8("don_add"))
#######################################################################################################################
	self.don_add.clicked.connect(self.indata3)
#######################################################################################################################
        self.gridLayout_2.addWidget(self.don_add, 2, 0, 1, 1)
        self.don_graph_text = QtGui.QLabel(Donors)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.don_graph_text.sizePolicy().hasHeightForWidth())
        self.don_graph_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.don_graph_text.setFont(font)
        self.don_graph_text.setObjectName(_fromUtf8("don_graph_text"))
        self.gridLayout_2.addWidget(self.don_graph_text, 3, 0, 1, 2)
        self.don_graph = QtGui.QPushButton(Donors)
        self.don_graph.setObjectName(_fromUtf8("don_graph"))
#######################################################################################################################
	self.don_graph.clicked.connect(self.graphdata1)
#######################################################################################################################
        self.gridLayout_2.addWidget(self.don_graph, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Donors)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi(Donors)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Donors.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Donors.reject)
        QtCore.QMetaObject.connectSlotsByName(Donors)

    def retranslateUi(self, Donors):
        Donors.setWindowTitle(_translate("Donors", "Dialog", None))
        self.label.setText(_translate("Donors", "Donors", None))
        self.paymethod.setText(_translate("Donors", "Pay Method", None))
        self.name.setText(_translate("Donors", "Name", None))
        self.state.setText(_translate("Donors", "State", None))
        self.amount.setText(_translate("Donors", "Amount", None))
        self.mobno.setText(_translate("Donors", "ID Number", None))
        self.don_add.setText(_translate("Donors", "Submit", None))
        self.don_graph_text.setText(_translate("Donors", "Funds Donated :", None))
        self.don_graph.setText(_translate("Donors", "Click here to know details.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Donors = QtGui.QDialog()
    ui = Ui_Donors()
    ui.setupUi(Donors)
    Donors.show()
    sys.exit(app.exec_())

