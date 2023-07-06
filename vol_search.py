# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vol_search.ui'
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

class Ui_volun_search(object):
#####################################################################################################################
    def loadData(self):
	connection = sqlite3.connect("authenticate.db")
	query = "SELECT * FROM vol_entry"
	result = connection.execute(query)
	self.tableWidget.setRowCount(0)
	
	for row_number, row_data in enumerate(result):
		self.tableWidget.insertRow(row_number)		
		for column_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))

	connection.close()
####################################################################################################################
    def searchData(self):
	vic1 = self.vol_e_id.text()
	vic = unicode(vic1)
	connection = sqlite3.connect("authenticate.db")
	result = connection.execute("SELECT * FROM vol_entry WHERE id = (?)",[vic])
	self.tableWidget.setRowCount(0)
	
	for row_number, row_data in enumerate(result):
		self.tableWidget.insertRow(row_number)		
		for column_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))

	connection.close()
####################################################################################################################
    def setupUi(self, volun_search):
        volun_search.setObjectName(_fromUtf8("volun_search"))
        volun_search.resize(788, 591)
        self.gridLayout = QtGui.QGridLayout(volun_search)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(volun_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.vol_result = QtGui.QPushButton(volun_search)
        self.vol_result.setObjectName(_fromUtf8("vol_result"))
#####################################################################################################################
	self.vol_result.clicked.connect(self.loadData)
#####################################################################################################################
        self.gridLayout.addWidget(self.vol_result, 2, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(volun_search)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 3, 1, 1)
        self.vol_e_id = QtGui.QLineEdit(volun_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vol_e_id.sizePolicy().hasHeightForWidth())
        self.vol_e_id.setSizePolicy(sizePolicy)
        self.vol_e_id.setObjectName(_fromUtf8("vol_e_id"))
        self.gridLayout.addWidget(self.vol_e_id, 0, 1, 1, 1)
        self.vol_id = QtGui.QLabel(volun_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vol_id.sizePolicy().hasHeightForWidth())
        self.vol_id.setSizePolicy(sizePolicy)
        self.vol_id.setObjectName(_fromUtf8("vol_id"))
        self.gridLayout.addWidget(self.vol_id, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(volun_search)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#####################################################################################################################
	self.pushButton.clicked.connect(self.searchData)
#####################################################################################################################
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.retranslateUi(volun_search)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), volun_search.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), volun_search.reject)
        QtCore.QMetaObject.connectSlotsByName(volun_search)

    def retranslateUi(self, volun_search):
        volun_search.setWindowTitle(_translate("volun_search", "Dialog", None))
        self.vol_result.setText(_translate("volun_search", "Display All Volunteers", None))
        self.vol_e_id.setPlaceholderText(_translate("volun_search", "Volunteer ID in Vcard", None))
        self.vol_id.setText(_translate("volun_search", "Volunteer ID", None))
        self.pushButton.setText(_translate("volun_search", "Search", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    volun_search = QtGui.QDialog()
    ui = Ui_volun_search()
    ui.setupUi(volun_search)
    volun_search.show()
    sys.exit(app.exec_())

