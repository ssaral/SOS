# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ngo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ngo_search import Ui_NGOsearch
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

class Ui_NGOs(object):
#######################################################################################################################
    def indata5(self):
	n7=self.ngo_e_name.text()
	id7=self.nog_e_id.text()
	add7=self.ngo_e_add.text()
	adds7=self.lineEdit_9.text()
	addc7=self.lineEdit_8.text()	
	int1=self.ngo_e_int.text()
	fr1=self.ngo_e_fr.text()
	n8=self.lineEdit_4.text()
	id8=self.lineEdit_2.text()
	add8=self.lineEdit_3.text()
	adds8=self.lineEdit_7.text()
	addc8=self.lineEdit_6.text()
	comboText1 = self.comboBox.currentText()
	cs1=self.lineEdit.text()
	n = unicode(n7)
	ido = unicode(id7)
	addo = unicode(add7)
	addos = unicode(adds7)
	addoc = unicode(addc7)
	into = unicode(int1)
	fr = unicode(fr1)
	n1 = unicode(n8)
	ido1 = unicode(id8)
	addo1 = unicode(add8)
	addos1 = unicode(adds8)
	addoc1 = unicode(addc8)
	sp = unicode(comboText1)
	cs = unicode(cs1)
	connection = sqlite3.connect("authenticate.db")
	connection.execute("INSERT INTO ngo_entry VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[n,ido,addo,addos,addoc,into,fr,n1,ido1,addo1,addos1,addoc1,sp,cs])
	print("NGOs Details Added Successfully..!!")
	connection.commit()
	connection.close()
#######################################################################################################################
    def gosearch(self):
	print("NGOs Search Button clicked")
	self.ngo_searchWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_NGOsearch()		
	self.ui.setupUi(self.ngo_searchWindow)
	self.ngo_searchWindow.show()
#######################################################################################################################
    def setupUi(self, NGOs):
        NGOs.setObjectName(_fromUtf8("NGOs"))
        NGOs.resize(869, 541)
        self.gridLayout_3 = QtGui.QGridLayout(NGOs)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ID = QtGui.QLabel(NGOs)
        self.ID.setObjectName(_fromUtf8("ID"))
        self.gridLayout.addWidget(self.ID, 2, 0, 1, 1)
        self.vic_e_sex = QtGui.QLabel(NGOs)
        self.vic_e_sex.setObjectName(_fromUtf8("vic_e_sex"))
        self.gridLayout.addWidget(self.vic_e_sex, 6, 0, 1, 1)
        self.name = QtGui.QLabel(NGOs)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.nog_e_id = QtGui.QLineEdit(NGOs)
        self.nog_e_id.setObjectName(_fromUtf8("nog_e_id"))
        self.gridLayout.addWidget(self.nog_e_id, 1, 2, 1, 1)
        self.agerange = QtGui.QLabel(NGOs)
        self.agerange.setObjectName(_fromUtf8("agerange"))
        self.gridLayout.addWidget(self.agerange, 1, 0, 1, 1)
        self.ngo_e_fr = QtGui.QLineEdit(NGOs)
        self.ngo_e_fr.setObjectName(_fromUtf8("ngo_e_fr"))
        self.gridLayout.addWidget(self.ngo_e_fr, 6, 2, 1, 1)
        self.status = QtGui.QLabel(NGOs)
        self.status.setObjectName(_fromUtf8("status"))
        self.gridLayout.addWidget(self.status, 5, 0, 1, 1)
        self.ngo_e_name = QtGui.QLineEdit(NGOs)
        self.ngo_e_name.setObjectName(_fromUtf8("ngo_e_name"))
        self.gridLayout.addWidget(self.ngo_e_name, 0, 2, 1, 1)
        self.ngo_e_int = QtGui.QLineEdit(NGOs)
        self.ngo_e_int.setObjectName(_fromUtf8("ngo_e_int"))
        self.gridLayout.addWidget(self.ngo_e_int, 5, 2, 1, 1)
        self.ngo_e_add = QtGui.QLineEdit(NGOs)
        self.ngo_e_add.setObjectName(_fromUtf8("ngo_e_add"))
        self.gridLayout.addWidget(self.ngo_e_add, 2, 2, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(NGOs)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout.addWidget(self.lineEdit_8, 4, 2, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(NGOs)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout.addWidget(self.lineEdit_9, 3, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label = QtGui.QLabel(NGOs)
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
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(NGOs)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 4, 1, 2, 1)
        self.label_9 = QtGui.QLabel(NGOs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_6 = QtGui.QLineEdit(NGOs)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 5, 2, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(NGOs)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 4, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(NGOs)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 8, 2, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(NGOs)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 2, 1, 1)
        self.label_3 = QtGui.QLabel(NGOs)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(NGOs)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(NGOs)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(NGOs)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(NGOs)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(NGOs)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_4 = QtGui.QLabel(NGOs)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(NGOs)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)
        self.label_8 = QtGui.QLabel(NGOs)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(NGOs)
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
        self.gridLayout_2.addWidget(self.comboBox, 6, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(NGOs)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#######################################################################################################################
	self.pushButton.clicked.connect(self.gosearch)	
#######################################################################################################################
        self.gridLayout_3.addWidget(self.pushButton, 5, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(NGOs)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
#######################################################################################################################
	self.pushButton_2.clicked.connect(self.indata5)
#######################################################################################################################

        self.gridLayout_3.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.retranslateUi(NGOs)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NGOs.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NGOs.reject)
        QtCore.QMetaObject.connectSlotsByName(NGOs)

    def retranslateUi(self, NGOs):
        NGOs.setWindowTitle(_translate("NGOs", "Dialog", None))
        self.ID.setText(_translate("NGOs", "Address", None))
        self.vic_e_sex.setText(_translate("NGOs", "Funds Received", None))
        self.name.setText(_translate("NGOs", "Name of organization", None))
        self.agerange.setText(_translate("NGOs", "Organization ID", None))
        self.status.setText(_translate("NGOs", "InTake Capacity", None))
        self.ngo_e_add.setPlaceholderText(_translate("NGOs", "Main Line", None))
        self.lineEdit_8.setPlaceholderText(_translate("NGOs", "Country", None))
        self.lineEdit_9.setPlaceholderText(_translate("NGOs", "State", None))
        self.label.setText(_translate("NGOs", "NGOs Details", None))
        self.label_9.setText(_translate("NGOs", "NGOs Option: ", None))
        self.lineEdit_6.setPlaceholderText(_translate("NGOs", "Country", None))
        self.lineEdit_7.setPlaceholderText(_translate("NGOs", "State", None))
        self.lineEdit.setPlaceholderText(_translate("NGOs", "Expenditure on Patients", None))
        self.lineEdit_3.setPlaceholderText(_translate("NGOs", "Main Line", None))
        self.label_3.setText(_translate("NGOs", "Name", None))
        self.label_2.setText(_translate("NGOs", "Hospital", None))
        self.label_5.setText(_translate("NGOs", "Details(Partners)", None))
        self.label_7.setText(_translate("NGOs", "Services Provided", None))
        self.label_4.setText(_translate("NGOs", "Address", None))
        self.label_6.setText(_translate("NGOs", "Cost Spent", None))
        self.label_8.setText(_translate("NGOs", "ID", None))
        self.comboBox.setItemText(0, _translate("NGOs", "Select from one below", None))
        self.comboBox.setItemText(1, _translate("NGOs", "Cardiologist", None))
        self.comboBox.setItemText(2, _translate("NGOs", "Internal Medicine Physician", None))
        self.comboBox.setItemText(3, _translate("NGOs", "Surgeon", None))
        self.comboBox.setItemText(4, _translate("NGOs", "Dermatologist", None))
        self.comboBox.setItemText(5, _translate("NGOs", "Endocrinologist", None))
        self.comboBox.setItemText(6, _translate("NGOs", "Infectious Disease Physician ", None))
        self.comboBox.setItemText(7, _translate("NGOs", "Otolaryngologist ", None))
        self.comboBox.setItemText(8, _translate("NGOs", "Neurologist", None))
        self.pushButton.setText(_translate("NGOs", "Click for NGOs Option", None))
        self.pushButton_2.setText(_translate("NGOs", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NGOs = QtGui.QDialog()
    ui = Ui_NGOs()
    ui.setupUi(NGOs)
    NGOs.show()
    sys.exit(app.exec_())

