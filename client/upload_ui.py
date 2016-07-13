# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QBoxLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.setMainUi(MainWindow)
        self.setMenuBar()
        self.setFileContainer()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setMainUi(self,MainWindow):
        MainWindow.setMinimumSize(800, 600)
        MainWindow.setMaximumSize(800, 600)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(6)
        self.mainLayout.setContentsMargins(5, 5, 5, 5)
        self.mainWidget.setLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.mainWidget)
        pass

    def setMenuBar(self):
        self.buttonInputFile = QtWidgets.QPushButton("选择文件")
        self.buttonInputFile.setStyleSheet("""QPushButton{margin:5px 0;padding:15px 0;}""")
        self.buttonInputFile.setMaximumSize(QtCore.QSize(120, 60))
        self.buttonInputFile.setObjectName('buttonInputFile')

        self.buttonStartALL = QtWidgets.QPushButton("开始")
        self.buttonStartALL.setStyleSheet("""QPushButton{margin:5px 0;padding:15px 0;}""")
        self.buttonStartALL.setMaximumSize(QtCore.QSize(120, 60))
        self.buttonStartALL.setObjectName('buttonStartALL')

        self.buttonPauseALL = QtWidgets.QPushButton("暂停")
        self.buttonPauseALL.setStyleSheet("""QPushButton{margin:5px 0;padding:15px 0;}""")
        self.buttonPauseALL.setMaximumSize(QtCore.QSize(120, 60))
        self.buttonPauseALL.setObjectName('buttonPauseALL')

        self.buttonGroup = QtWidgets.QWidget()
        self.buttonGroup.setMaximumHeight(300)
        ButtonGroupLayout = QtWidgets.QHBoxLayout();
        self.buttonGroup.setLayout(ButtonGroupLayout)
        ButtonGroupLayout.addWidget(self.buttonInputFile)
        ButtonGroupLayout.addWidget(self.buttonStartALL )
        ButtonGroupLayout.addWidget(self.buttonPauseALL )
        ButtonGroupLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.buttonGroup)
        pass

    def setFileContainer(self):

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.scrollArea)
        self.fileContainerLayout = QtWidgets.QVBoxLayout()
        self.fileContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.fileContainerLayout.setSpacing(0)
        self.fileContainer = QtWidgets.QWidget()
        self.fileContainer.setLayout(self.fileContainerLayout)
        self.mainLayout.addWidget(self.fileContainer, 2)
        self.scrollArea.setWidget(self.fileContainer)
        self.scrollArea.show()
        # 作为弹簧 把任务顶上去
        springs_widget = QtWidgets.QWidget()
        self.fileContainerLayout.addWidget(springs_widget, 9, QtCore.Qt.AlignTop)
        pass

    def addFile(self):
        file = QtWidgets.QWidget()
        file.setMaximumHeight(50)
        file.setContentsMargins(5, 5, 5, 5)

        file.setStyleSheet(
            """QWidget{border-top:1px solid #ccc;background:#fff;padding:0;margin:0;height:70px;}""")
        fileLayout = QtWidgets.QHBoxLayout()
        fileLayout.setSpacing(0)

        icon = QtWidgets.QPushButton()
        icon.setStyleSheet("""QPushButton{margin:0px 5px;background-image:url(./ico/rar.png);width:32px;height:32px;padding:0px;border:0px;}
                    """)
        # fz_size_label.setMaximumSize(QtCore.QSize(300, 25))
        fileLayout.addWidget(icon)

        fleInfo = QtWidgets.QWidget()
        fleInfo.setStyleSheet("""QWidget{border:none;}""")
        fileInfoLayout = QtWidgets.QVBoxLayout()
        fileInfoLayout.setSpacing(0)
        fileInfoLayout.setContentsMargins(0, 0, 0, 0)
        fleInfo.setLayout(fileInfoLayout)

        fileName = QtWidgets.QLabel("232323232323.pdf")
        fileName.setMinimumSize(QtCore.QSize(250, 25))
        fileName.setMaximumSize(QtCore.QSize(250, 25))
        fileName.setStyleSheet("""QLabel{margin:0 20px 0 0;}
            """)
        fileInfoLayout.addWidget(fileName)

        fileSize = QtWidgets.QLabel(str("232323"))
        fileSize.setStyleSheet("""QLabel{font-size:11px;color:#777;margin:0 20px 0 0;}
            """)
        fileSize.setMinimumSize(QtCore.QSize(300, 25))
        fileSize.setMaximumSize(QtCore.QSize(300, 25))
        fileInfoLayout.addWidget(fileSize)

        fileLayout.addWidget(fleInfo)

        # file_progress_bar
        fileProgress = QtWidgets.QWidget()
        fileProgress.setStyleSheet("""QWidget{border:none;margin:0;padding:0;}""")
        fileProgressLayout = QtWidgets.QVBoxLayout()
        fileProgressLayout.setSpacing(0)
        fileProgressLayout.setContentsMargins(0, 0, 0, 0)
        fileProgress.setLayout(fileProgressLayout)

        fileProcessBar = QtWidgets.QProgressBar()
        fileProcessBar.setValue(26)
        fileProcessBar.setTextVisible(0)
        fileProcessBar.setMinimumSize(QtCore.QSize(100, 25))
        fileProcessBar.setMaximumSize(QtCore.QSize(100, 25))
        fileProgressLayout.addWidget(fileProcessBar)

        fileProcessText = QtWidgets.QLabel("0%")
        fileProcessText.setStyleSheet("""QLabel{;margin:0;padding:0;font-size:11px;color:#777;}""")
        # fz_process_text.setMinimumSize(QtCore.QSize(100, 25))
        # fz_process_text.setMaximumSize(QtCore.QSize(100, 25))
        fileProgressLayout.addWidget(fileProcessText)

        fileLayout.addWidget(fileProgress)
        # file_progress_bar end

        fileBtnGroup = QtWidgets.QWidget()
        fileBtnGroup.setStyleSheet("""QWidget{border:none;margin:0;padding:0;}""")
        fileBtnGroupLayout = QtWidgets.QHBoxLayout()
        fileBtnGroupLayout.setSpacing(0)
        fileBtnGroupLayout.setContentsMargins(5, 5, 5, 5)
        fileBtnGroup.setLayout(fileBtnGroupLayout)

        fileStartBtn = QtWidgets.QPushButton("开始")
        fileStartBtn.setStyleSheet("background:none;")
        fileStartBtn.setMinimumSize(QtCore.QSize(40, 25))
        fileStartBtn.setMaximumSize(QtCore.QSize(40, 25))
        fileBtnGroupLayout.addWidget(fileStartBtn)

        fileCancelBtn = QtWidgets.QPushButton("删除")
        fileCancelBtn.setStyleSheet("background:none;")
        fileCancelBtn.setMinimumSize(QtCore.QSize(40, 25))
        fileCancelBtn.setMaximumSize(QtCore.QSize(40, 25))
        fileBtnGroupLayout.addWidget(fileCancelBtn)
        fileLayout.addWidget(fileBtnGroup)

        file.setLayout(fileLayout)
        fileLayout.setContentsMargins(0, 0, 0, 0)
        fileLayout.setSpacing(0)
        allCount = self.fileContainerLayout.count()
        print(allCount)
        if allCount == 1:
            self.fileContainerLayout.insertWidget(0, file)
        else:
            self.fileContainerLayout.insertWidget(allCount - 1, file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



