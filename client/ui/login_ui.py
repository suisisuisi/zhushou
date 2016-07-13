# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 353, 134))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.cancelBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        # self.menuBar = QtWidgets.QMenuBar(MainWindow)
        # self.menuBar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        # self.menuBar.setObjectName("menuBar")
        # # MainWindow.setMenuBar(self.menuBar)
        # self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        # self.mainToolBar.setEnabled(True)
        # self.mainToolBar.setObjectName("mainToolBar")
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        # self.statusBar = QtWidgets.QStatusBar(MainWindow)
        # self.statusBar.setObjectName("statusBar")
        # MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

  


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名:"))
        self.label_2.setText(_translate("MainWindow", "密码:"))
        self.okBtn.setText(_translate("MainWindow", "确定"))
        self.cancelBtn.setText(_translate("MainWindow", "取消"))

