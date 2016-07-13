# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QBoxLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(800, 600)
        MainWindow.setMaximumSize(800, 600)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        btn_select_file = QtWidgets.QPushButton("选择文件")
        btn_select_file.setStyleSheet("""QPushButton{margin:5px 0;padding:15px 0;}""")
        btn_select_file.setMaximumSize(QtCore.QSize(120, 60))
        btn_select_file.setObjectName('btn')

        start_all_btn = QtWidgets.QPushButton("开始")
        start_all_btn.setStyleSheet("""QPushButton{margin:5px 0;padding:15px 0;}""")
        start_all_btn.setMaximumSize(QtCore.QSize(120, 60))
        start_all_btn.setObjectName('ButtonStartAll')

        pause_all_btn = QtWidgets.QPushButton("暂停")
        pause_all_btn.setStyleSheet("""QPushButton{margin:5px 0;padding:15px 0;}""")
        pause_all_btn.setMaximumSize(QtCore.QSize(120, 60))
        pause_all_btn.setObjectName('ButtonPauseAll')

        upload_btn_group = QtWidgets.QWidget()
        upload_btn_group.setMaximumHeight(300)
        upload_btn_group_layout = QtWidgets.QHBoxLayout();
        upload_btn_group.setLayout(upload_btn_group_layout)
        upload_btn_group_layout.addWidget(btn_select_file)
        upload_btn_group_layout.addWidget(start_all_btn)
        upload_btn_group_layout.addWidget(pause_all_btn)
        upload_btn_group_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(upload_btn_group)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.scrollArea)

        self.scrollLayout = QtWidgets.QVBoxLayout()
        self.scrollLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollLayout.setSpacing(0)

        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        self.verticalLayout.addWidget(self.scrollWidget, 2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea.setWidget(self.scrollWidget)
        self.scrollArea.show()

        # 作为弹簧 把任务顶上去
        springs_widget = QtWidgets.QWidget()
        self.scrollLayout.addWidget(springs_widget, 9, QtCore.Qt.AlignTop)
        self.centralWidget.setLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setMainUi(self):

        pass

    def setGroupBtn(self):

        pass

    def setFileRow(self):

        pass

    def add_file_container(self, wfile):
        file_widget = QtWidgets.QWidget()
        file_widget.setMaximumHeight(50)
        file_widget.setContentsMargins(5, 5, 5, 5)

        file_widget.setStyleSheet(
            """QWidget{border-top:1px solid #ccc;background:#fff;padding:0;margin:0;height:70px;}""")
        file_layout = QtWidgets.QHBoxLayout()
        file_layout.setSpacing(0)

        icon = QtWidgets.QPushButton()
        icon.setStyleSheet("""QPushButton{margin:0px 5px;background-image:url(./ico/rar.png);width:32px;height:32px;padding:0px;border:0px;}
                    """)
        # fz_size_label.setMaximumSize(QtCore.QSize(300, 25))
        file_layout.addWidget(icon)

        file_info_widget = QtWidgets.QWidget()
        file_info_widget.setStyleSheet("""QWidget{border:none;}""")
        file_info_layout = QtWidgets.QVBoxLayout()
        file_info_layout.setSpacing(0)
        file_info_layout.setContentsMargins(0, 0, 0, 0)
        file_info_widget.setLayout(file_info_layout)

        file_name = QtWidgets.QLabel(wfile.name)
        file_name.setMinimumSize(QtCore.QSize(250, 25))
        file_name.setMaximumSize(QtCore.QSize(250, 25))
        file_name.setStyleSheet("""QLabel{margin:0 20px 0 0;}
            """)
        file_info_layout.addWidget(file_name)

        file_size = QtWidgets.QLabel(str(wfile.size))
        file_size.setStyleSheet("""QLabel{font-size:11px;color:#777;margin:0 20px 0 0;}
            """)
        file_size.setMinimumSize(QtCore.QSize(300, 25))
        file_size.setMaximumSize(QtCore.QSize(300, 25))
        file_info_layout.addWidget(file_size)

        file_layout.addWidget(file_info_widget)

        # file_progress_bar
        file_progress_widget = QtWidgets.QWidget()
        file_progress_widget.setStyleSheet("""QWidget{border:none;margin:0;padding:0;}""")
        file_progress_layout = QtWidgets.QVBoxLayout()
        file_progress_layout.setSpacing(0)
        file_progress_layout.setContentsMargins(0, 0, 0, 0)
        file_progress_widget.setLayout(file_progress_layout)

        file_process_bar = QtWidgets.QProgressBar()
        file_process_bar.setValue(26)
        file_process_bar.setTextVisible(0)
        file_process_bar.setMinimumSize(QtCore.QSize(100, 25))
        file_process_bar.setMaximumSize(QtCore.QSize(100, 25))
        file_progress_layout.addWidget(file_process_bar)

        file_process_text = QtWidgets.QLabel("0%")
        file_process_text.setStyleSheet("""QLabel{;margin:0;padding:0;font-size:11px;color:#777;}""")
        # fz_process_text.setMinimumSize(QtCore.QSize(100, 25))
        # fz_process_text.setMaximumSize(QtCore.QSize(100, 25))
        file_progress_layout.addWidget(file_process_text)

        file_layout.addWidget(file_progress_widget)
        # file_progress_bar end

        file_btn_widget = QtWidgets.QWidget()
        file_btn_widget.setStyleSheet("""QWidget{border:none;margin:0;padding:0;}""")
        file_btn_layout = QtWidgets.QHBoxLayout()
        file_btn_layout.setSpacing(0)
        file_btn_layout.setContentsMargins(5, 5, 5, 5)
        file_btn_widget.setLayout(file_btn_layout)

        start_btn = QtWidgets.QPushButton("开始")
        start_btn.setStyleSheet("background:none;")
        start_btn.setMinimumSize(QtCore.QSize(40, 25))
        start_btn.setMaximumSize(QtCore.QSize(40, 25))
        file_btn_layout.addWidget(start_btn)

        cancel_btn = QtWidgets.QPushButton("删除")
        cancel_btn.setStyleSheet("background:none;")
        cancel_btn.setMinimumSize(QtCore.QSize(40, 25))
        cancel_btn.setMaximumSize(QtCore.QSize(40, 25))
        file_btn_layout.addWidget(cancel_btn)
        file_layout.addWidget(file_btn_widget)

        file_widget.setLayout(file_layout)
        file_layout.setContentsMargins(0, 0, 0, 0)
        file_layout.setSpacing(0)
        allCount = self.scrollLayout.count()
        print(allCount)
        if allCount == 1:
            self.scrollLayout.insertWidget(0, file_widget)
        else:
            self.scrollLayout.insertWidget(allCount - 1, file_widget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



