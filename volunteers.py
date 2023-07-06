# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'volunteers.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from vol_search import Ui_volun_search
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

class Ui_Volunteers(object):
#######################################################################################################################
    def indata2(self):
	n3=self.vol_e_name.text()
	id2=self.vol_e_id.text()
	mob2=self.vol_e_mob.text()
	age2=self.vol_e_age.text()
	comboText1=self.comboBox.currentText()
	n = unicode(n3)
	ids = unicode(id2)
	mob = unicode(mob2)
	age = unicode(age2)
	sex = unicode(comboText1)
	connection = sqlite3.connect("authenticate.db")
	connection.execute("INSERT INTO vol_entry VALUES(?,?,?,?,?)",[n,ids,mob,age,sex])
	print("Volunteers Details Added Successfully..!!")
	connection.commit()
	connection.close()
#######################################################################################################################
    def gotosearch(self):
	print("Volunteeer Search Button clicked")
	self.vol_searchWindow=QtGui.QDialog() #object of new window
	self.ui= Ui_volun_search()		
	self.ui.setupUi(self.vol_searchWindow)
	self.vol_searchWindow.show()
#######################################################################################################################
    def setupUi(self, Volunteers):
        Volunteers.setObjectName(_fromUtf8("Volunteers"))
        Volunteers.resize(861, 454)
        self.gridLayout_2 = QtGui.QGridLayout(Volunteers)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(Volunteers)
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
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.age = QtGui.QLabel(Volunteers)
        self.age.setObjectName(_fromUtf8("age"))
        self.gridLayout.addWidget(self.age, 3, 0, 1, 1)
        self.name = QtGui.QLabel(Volunteers)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.vol_e_name = QtGui.QLineEdit(Volunteers)
        self.vol_e_name.setObjectName(_fromUtf8("vol_e_name"))
        self.gridLayout.addWidget(self.vol_e_name, 0, 2, 1, 1)
        self.sex = QtGui.QLabel(Volunteers)
        self.sex.setObjectName(_fromUtf8("sex"))
        self.gridLayout.addWidget(self.sex, 4, 0, 1, 1)
        self.id = QtGui.QLabel(Volunteers)
        self.id.setObjectName(_fromUtf8("id"))
        self.gridLayout.addWidget(self.id, 1, 0, 1, 1)
        self.mob = QtGui.QLabel(Volunteers)
        self.mob.setObjectName(_fromUtf8("mob"))
        self.gridLayout.addWidget(self.mob, 2, 0, 1, 1)
        self.vol_e_id = QtGui.QLineEdit(Volunteers)
        self.vol_e_id.setObjectName(_fromUtf8("vol_e_id"))
        self.gridLayout.addWidget(self.vol_e_id, 1, 2, 1, 1)
        self.vol_e_age = QtGui.QLineEdit(Volunteers)
        self.vol_e_age.setObjectName(_fromUtf8("vol_e_age"))
        self.gridLayout.addWidget(self.vol_e_age, 3, 2, 1, 1)
        self.vol_e_mob = QtGui.QLineEdit(Volunteers)
        self.vol_e_mob.setObjectName(_fromUtf8("vol_e_mob"))
        self.gridLayout.addWidget(self.vol_e_mob, 2, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(Volunteers)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.areaofwork = QtGui.QLabel(Volunteers)
        self.areaofwork.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.areaofwork.setObjectName(_fromUtf8("areaofwork"))
        self.gridLayout_3.addWidget(self.areaofwork, 10, 0, 1, 1)
        self.vol_e_cont = QtGui.QLineEdit(Volunteers)
        self.vol_e_cont.setObjectName(_fromUtf8("vol_e_cont"))
        self.gridLayout_3.addWidget(self.vol_e_cont, 9, 2, 1, 1)
        self.address = QtGui.QLabel(Volunteers)
        self.address.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.address.setObjectName(_fromUtf8("address"))
        self.gridLayout_3.addWidget(self.address, 7, 0, 1, 1)
        self.vol_e_aoi = QtGui.QLineEdit(Volunteers)
        self.vol_e_aoi.setObjectName(_fromUtf8("vol_e_aoi"))
        self.gridLayout_3.addWidget(self.vol_e_aoi, 10, 2, 1, 1)
        self.vol_e_state = QtGui.QLineEdit(Volunteers)
        self.vol_e_state.setObjectName(_fromUtf8("vol_e_state"))
        self.gridLayout_3.addWidget(self.vol_e_state, 8, 2, 1, 1)
        self.vol_e_add1_2 = QtGui.QLineEdit(Volunteers)
        self.vol_e_add1_2.setObjectName(_fromUtf8("vol_e_add1_2"))
        self.gridLayout_3.addWidget(self.vol_e_add1_2, 7, 2, 1, 1)
        self.vol_add = QtGui.QPushButton(Volunteers)
        self.vol_add.setObjectName(_fromUtf8("vol_add"))
#######################################################################################################################
	self.vol_add.clicked.connect(self.indata2)	
#######################################################################################################################
        self.gridLayout_3.addWidget(self.vol_add, 11, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.vol_detail_text = QtGui.QLabel(Volunteers)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vol_detail_text.sizePolicy().hasHeightForWidth())
        self.vol_detail_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Symbola"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.vol_detail_text.setFont(font)
        self.vol_detail_text.setAlignment(QtCore.Qt.AlignCenter)
        self.vol_detail_text.setObjectName(_fromUtf8("vol_detail_text"))
        self.gridLayout_2.addWidget(self.vol_detail_text, 2, 0, 1, 1)
        self.vol_table = QtGui.QPushButton(Volunteers)
        self.vol_table.setObjectName(_fromUtf8("vol_table"))
#######################################################################################################################
	self.vol_table.clicked.connect(self.gotosearch)	
#######################################################################################################################
        self.gridLayout_2.addWidget(self.vol_table, 3, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Volunteers)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(Volunteers)
	QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Volunteers.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Volunteers.reject)
        QtCore.QMetaObject.connectSlotsByName(Volunteers)

    def retranslateUi(self, Volunteers):
        Volunteers.setWindowTitle(_translate("Volunteers", "Dialog", None))
        self.label.setText(_translate("Volunteers", "Volunteers", None))
        self.age.setText(_translate("Volunteers", "Age", None))
        self.name.setText(_translate("Volunteers", "Name ", None))
        self.sex.setText(_translate("Volunteers", "Sex", None))
        self.id.setText(_translate("Volunteers", "ID (in_vcard)", None))
        self.mob.setText(_translate("Volunteers", "Mobile Number", None))
        self.comboBox.setItemText(0, _translate("Volunteers", "Select one from below", None))
        self.comboBox.setItemText(1, _translate("Volunteers", "Male", None))
        self.comboBox.setItemText(2, _translate("Volunteers", "Female", None))
        self.comboBox.setItemText(3, _translate("Volunteers", "Transgender", None))
        self.areaofwork.setText(_translate("Volunteers", "Area Of Interest", None))
        self.vol_e_cont.setPlaceholderText(_translate("Volunteers", "Country", None))
        self.address.setText(_translate("Volunteers", "Address", None))
        self.vol_e_state.setPlaceholderText(_translate("Volunteers", "State", None))
        self.vol_e_add1_2.setPlaceholderText(_translate("Volunteers", "Main Line", None))
        self.vol_add.setText(_translate("Volunteers", "Submit", None))
        self.vol_detail_text.setText(_translate("Volunteers", "Volunteers Details", None))
        self.vol_table.setText(_translate("Volunteers", "Click here to search Volunteers", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Volunteers = QtGui.QDialog()
    ui = Ui_Volunteers()
    ui.setupUi(Volunteers)
    Volunteers.show()
    sys.exit(app.exec_())

