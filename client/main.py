# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PyQt5.QtWidgets import *

from upload_ui import *


class MyApp(QMainWindow):
    ui = ""

    def __init__(self):
        QMainWindow.__init__(self)
        # self.ui = Ui_LoginWindow()
        # self.ui.setupUi(self)
        # self.ui.okBtn.clicked.connect(self.ok)
        # self.ui.cancelBtn.clicked.connect(self.cancel)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.addEventListen()

    def addEventListen(self):
        self.findChild(QPushButton, "buttonInputFile").clicked.connect(self.openFileDialog)
        # self.findChild(QPushButton, "buttonStartALL").clicked.connect(self.upload)

        pass
    def ok(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # if self.ui.lineEdit.text()=="eric" and self.ui.lineEdit_2.text()=="eric":
        #     self.ui = Ui_UploadWindow()
        #     self.ui.setupUi(self)
        # else:
        #     QMessageBox.warning(self,"warn","username or password wrong",QMessageBox.Yes)
        #     self.ui.lineEdit.setFocus()

    def cancel(self):
        self.close()

    def openFileDialog(self):
        print ("23232")
        openPth = "/Users/yongzi/Downloads/测试/"
        files, ok = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", openPth,
                                                 "All Files (*);;picture (*.jpeg)")
        if (ok):
            self.addFiles(files)

    # 添加单个文件 再一下方法中我们会做一些文件是否已再队列中,是否已上传到服务器的判断
    def addFiles(self,files):



        if (len(files) > 0):
            for pth in files:
                self.ui.addFile ()
        else:
            print("no files selected")

        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = MyApp()
    p.show()
    sys.exit(app.exec_())
