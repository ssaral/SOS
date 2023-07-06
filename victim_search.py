# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'victim_search.ui'
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

class Ui_victim_search(object):
#####################################################################################################################
    def loadData6(self):
	connection = sqlite3.connect("authenticate.db")
	query = "SELECT * FROM victim_entry"
	result = connection.execute(query)
	self.tableWidget.setRowCount(0)
	
	for row_number, row_data in enumerate(result):
		self.tableWidget.insertRow(row_number)		
		for column_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))

	connection.close()
####################################################################################################################
    def searchData6(self):
	vic1 = self.vic_e_name.text()
	comboText1 = self.vic_e_sexr.currentText()
	age1 = self.vic_e_ager.text()
	mob1 = self.vic_e_mobno.text()
	vic = unicode(vic1)
	sex = unicode(comboText1)
	age = unicode(age1)
	mob = unicode(mob1)
	connection = sqlite3.connect("authenticate.db")
	result = connection.execute("SELECT * FROM victim_entry WHERE name = (?) AND sex = (?) AND age = (?) AND ID = (?)",[vic,sex,age,mob])
	self.tableWidget.setRowCount(0)
	
	for row_number, row_data in enumerate(result):
		self.tableWidget.insertRow(row_number)		
		for column_number, data in enumerate(row_data):
			self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))

	connection.close()
####################################################################################################################
    def setupUi(self, victim_search):
        victim_search.setObjectName(_fromUtf8("victim_search"))
        victim_search.resize(807, 638)
        self.gridLayout = QtGui.QGridLayout(victim_search)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.search_criteria = QtGui.QLabel(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_criteria.sizePolicy().hasHeightForWidth())
        self.search_criteria.setSizePolicy(sizePolicy)
        self.search_criteria.setObjectName(_fromUtf8("search_criteria"))
        self.gridLayout.addWidget(self.search_criteria, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 6, 1, 2)
        self.vol_result = QtGui.QPushButton(victim_search)
        self.vol_result.setObjectName(_fromUtf8("vol_result"))
        self.gridLayout.addWidget(self.vol_result, 2, 3, 1, 3)
        self.vic_e_sexr = QtGui.QComboBox(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vic_e_sexr.sizePolicy().hasHeightForWidth())
        self.vic_e_sexr.setSizePolicy(sizePolicy)
        self.vic_e_sexr.setObjectName(_fromUtf8("vic_e_sexr"))
        self.vic_e_sexr.addItem(_fromUtf8(""))
        self.vic_e_sexr.addItem(_fromUtf8(""))
        self.vic_e_sexr.addItem(_fromUtf8(""))
        self.vic_e_sexr.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.vic_e_sexr, 0, 4, 1, 1)
        self.vic_e_name = QtGui.QLineEdit(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vic_e_name.sizePolicy().hasHeightForWidth())
        self.vic_e_name.setSizePolicy(sizePolicy)
        self.vic_e_name.setObjectName(_fromUtf8("vic_e_name"))
        self.gridLayout.addWidget(self.vic_e_name, 0, 1, 1, 3)
        self.vic_e_ager = QtGui.QLineEdit(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vic_e_ager.sizePolicy().hasHeightForWidth())
        self.vic_e_ager.setSizePolicy(sizePolicy)
        self.vic_e_ager.setObjectName(_fromUtf8("vic_e_ager"))
        self.gridLayout.addWidget(self.vic_e_ager, 0, 5, 1, 1)
        self.vic_e_mobno = QtGui.QLineEdit(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vic_e_mobno.sizePolicy().hasHeightForWidth())
        self.vic_e_mobno.setSizePolicy(sizePolicy)
        self.vic_e_mobno.setObjectName(_fromUtf8("vic_e_mobno"))
        self.gridLayout.addWidget(self.vic_e_mobno, 0, 6, 1, 1)
        self.tableWidget = QtGui.QTableWidget(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 2, 8)
        self.pushButton = QtGui.QPushButton(victim_search)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#####################################################################################################################
	self.pushButton.clicked.connect(self.loadData6)
#####################################################################################################################
        self.gridLayout.addWidget(self.pushButton, 3, 5, 1, 1)
        self.vic_search = QtGui.QPushButton(victim_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vic_search.sizePolicy().hasHeightForWidth())
        self.vic_search.setSizePolicy(sizePolicy)
        self.vic_search.setObjectName(_fromUtf8("vic_search"))
#####################################################################################################################
	self.vic_search.clicked.connect(self.searchData6)
#####################################################################################################################
        self.gridLayout.addWidget(self.vic_search, 3, 0, 1, 1)

        self.retranslateUi(victim_search)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), victim_search.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), victim_search.reject)
        QtCore.QMetaObject.connectSlotsByName(victim_search)

    def retranslateUi(self, victim_search):
        victim_search.setWindowTitle(_translate("victim_search", "Dialog", None))
        self.search_criteria.setText(_translate("victim_search", "Search Criteria", None))
        self.vol_result.setText(_translate("victim_search", "Search", None))
        self.vic_e_sexr.setItemText(0, _translate("victim_search", "Select from one below", None))
        self.vic_e_sexr.setItemText(1, _translate("victim_search", "Male", None))
        self.vic_e_sexr.setItemText(2, _translate("victim_search", "Female", None))
        self.vic_e_sexr.setItemText(3, _translate("victim_search", "Transgender", None))
        self.vic_e_name.setPlaceholderText(_translate("victim_search", "Name", None))
        self.vic_e_ager.setPlaceholderText(_translate("victim_search", "Age Range", None))
        self.vic_e_mobno.setPlaceholderText(_translate("victim_search", "Mob_no", None))
        self.pushButton.setText(_translate("victim_search", "Display all Vicitms", None))
        self.vic_search.setText(_translate("victim_search", "Search", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    victim_search = QtGui.QDialog()
    ui = Ui_victim_search()
    ui.setupUi(victim_search)
    victim_search.show()
    sys.exit(app.exec_())

