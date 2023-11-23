from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog

from kcsj.save import Ui_Dialog


class SaveWin(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(SaveWin, self).__init__(parent)
        self.setupUi(self)
        pixmap = QPixmap("img/question-mark-1750942_640.png")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)


class Myfile(super):
    def __init__(self, str, file_path):
        self.file_path = file_path
        self.str = str
        self.savewin = SaveWin()

    def passsavefile(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(self.str)
        msg_box = QMessageBox(QMessageBox.Information, '提示', '执行成功！')
        msg_box.exec_()

    def savefile(self, file_path, str, MyWin):
        self.savewin.show()
        self.savewin.buttonBox.accepted.connect(self.passsavefile)
        self.str = str
        self.file_path = file_path
        MyWin.setWindowTitle(file_path)

    def newfile(self, file_path, str, textEdit, MyWin):
        if len(str) != 0:
            self.savewin.show()
            self.savewin.buttonBox.accepted.connect(self.passsavefile)
            self.str = str
            self.file_path = file_path
            textEdit.clear()
            MyWin.setWindowTitle(file_path)

    def set(self, str, file_path):
        self.file_path = file_path
        self.str = str
