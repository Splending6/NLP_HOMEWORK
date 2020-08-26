# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_custom.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(526, 373)
        self.tableWidget = QtWidgets.QTableWidget(widget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 50, 451, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(180, 4, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "自定义纠错集"))
        self.label.setText(_translate("widget", "自定义纠错集"))
