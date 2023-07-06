# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ngo_search.ui'
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

class Ui_NGOsearch(object):
#####################################################################################################################
    def loadData5(self):
	connection = sqlite3.connect("authenticate.db")
	query = "SELECT * FROM ngo_entry"
	result = connection.execute(query)
	self.tableWidget.setRowCount(0)
	
	for row_number, row_data in enumerate(result):
		self.tableWidget.insertRow(row_number)		
		for column_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))

	connection.close()
####################################################################################################################
    def searchData5(self):
	ngo1 = self.comboBox.currentText()
	ngo = unicode(ngo1)
	connection = sqlite3.connect("authenticate.db")
	result = connection.execute("SELECT * FROM ngo_entry WHERE hsp = (?)",[ngo])
#	query = ("SELECT * FROM vol_entry WHERE id = (?)",[vic])	
#	result = connection.execute(query)
	self.tableWidget.setRowCount(0)
	
	for row_number, row_data in enumerate(result):
		self.tableWidget.insertRow(row_number)		
		for column_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))

	connection.close()
####################################################################################################################

    def setupUi(self, NGOsearch):
        NGOsearch.setObjectName(_fromUtf8("NGOsearch"))
        NGOsearch.resize(794, 581)
        self.gridLayout = QtGui.QGridLayout(NGOsearch)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(NGOsearch)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 3)
        self.ngo_sp = QtGui.QLabel(NGOsearch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ngo_sp.sizePolicy().hasHeightForWidth())
        self.ngo_sp.setSizePolicy(sizePolicy)
        self.ngo_sp.setAlignment(QtCore.Qt.AlignCenter)
        self.ngo_sp.setObjectName(_fromUtf8("ngo_sp"))
        self.gridLayout.addWidget(self.ngo_sp, 0, 0, 1, 1)
        self.ngo_result = QtGui.QPushButton(NGOsearch)
        self.ngo_result.setObjectName(_fromUtf8("ngo_result"))
#####################################################################################################################
	self.ngo_result.clicked.connect(self.searchData5)
#####################################################################################################################
        self.gridLayout.addWidget(self.ngo_result, 2, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(NGOsearch)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 3, 1, 1)
        self.tableWidget = QtGui.QTableWidget(NGOsearch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.pushButton = QtGui.QPushButton(NGOsearch)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#####################################################################################################################
	self.pushButton.clicked.connect(self.loadData5)
#####################################################################################################################
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.retranslateUi(NGOsearch)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NGOsearch.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NGOsearch.reject)
        QtCore.QMetaObject.connectSlotsByName(NGOsearch)

    def retranslateUi(self, NGOsearch):
        NGOsearch.setWindowTitle(_translate("NGOsearch", "Dialog", None))
        self.comboBox.setItemText(0, _translate("NGOsearch", "Select an option ", None))
        self.comboBox.setItemText(1, _translate("NGOsearch", "Cardiologist", None))
        self.comboBox.setItemText(2, _translate("NGOsearch", "Internal Medicine Physician", None))
        self.comboBox.setItemText(3, _translate("NGOsearch", "Surgeon", None))
        self.comboBox.setItemText(4, _translate("NGOsearch", "Dermatologist", None))
        self.comboBox.setItemText(5, _translate("NGOsearch", "Endocrinologist", None))
        self.comboBox.setItemText(6, _translate("NGOsearch", "Infectious Disease Physician", None))
        self.comboBox.setItemText(7, _translate("NGOsearch", "Otolaryngologist", None))
        self.comboBox.setItemText(8, _translate("NGOsearch", "Neurologist", None))
        self.ngo_sp.setText(_translate("NGOsearch", "NGOs partners with Hospital Speciality: ", None))
        self.ngo_result.setText(_translate("NGOsearch", "Search", None))
        self.pushButton.setText(_translate("NGOsearch", "Display all NGOs", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NGOsearch = QtGui.QDialog()
    ui = Ui_NGOsearch()
    ui.setupUi(NGOsearch)
    NGOsearch.show()
    sys.exit(app.exec_())

