import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QFileDialog

from kcsj.File import Myfile
from kcsj.window import Ui_MainWindow


class MyWin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.file_path="新建文本文档.txt"
        self.str=""
        self.myfile = Myfile(str=self.str, file_path=self.file_path)
        self.setupUi(self)

        self.setfile()

    def setfile(self):
        self.myfile.set(str=self.str, file_path=self.file_path)
        self.File_2.triggered.connect(lambda: self.myfile.savefile(self.file_path,self.textEdit.toPlainText(),self.statusBar))

        self.File_5.triggered.connect(lambda: self.openfile())

        self.File_3.triggered.connect(lambda: self.myfile.savefile(self.opensave(),self.textEdit.toPlainText(),self.statusBar))

        self.File_1.triggered.connect(lambda: self.myfile.newfile(self.file_path,self.textEdit.toPlainText(),self.statusBar,self.textEdit))

        self.File_4.triggered.connect(lambda: exit())



    def openfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Text Files (*.txt);;All Files (*)", options=options)
        self.readfile(file_path)
        self.statusbarshow(file_path)
        return file_path

    def opensave(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # 弹出文件保存对话框
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)
        return file_path

    def readfile(self,file_path):
        file = QFile(file_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.textEdit.setPlainText(stream.readAll())
            file.close()

    def statusbarshow(self,str):
        self.statusBar.clearMessage()
        self.statusBar.showMessage(str, 0)

    def addstatusbarshow(self,str):
        self.statusBar.showMessage(str, 0)

if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    ui = MyWin()
    ui.show()
    sys.exit(QApp.exec_())