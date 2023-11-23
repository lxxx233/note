import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog

from kcsj.Edit import MyEdit
from kcsj.File import Myfile
from kcsj.Setui import MySet
from kcsj.window import Ui_MainWindow


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.current_font = None
        self.file_path = "新建文本文档.txt"
        self.str = ""
        self.myfile = Myfile(str=self.str, file_path=self.file_path)
        self.myedit = MyEdit()
        self.myset = MySet()
        self.setupUi(self)
        self.View_5.setChecked(True)
        self.textEdit.setStyleSheet("background-color: transparent;")

        self.textEdit.cursorPositionChanged.connect(self.cursorPosition)
        self.setfile()
        self.findedit()
        self.veiwset()
        self.setting()

    def setfile(self):
        self.myfile.set(str=self.str, file_path=self.file_path)
        self.File_2.triggered.connect(
            lambda: self.myfile.savefile(self.file_path, self.textEdit.toPlainText(), self))

        self.File_5.triggered.connect(lambda: self.openfile())

        self.File_3.triggered.connect(
            lambda: self.myfile.savefile(self.opensave(), self.textEdit.toPlainText(), self))

        self.File_1.triggered.connect(
            lambda: self.myfile.newfile(self.file_path, self.textEdit.toPlainText(), self.textEdit, self))

        self.File_4.triggered.connect(lambda: exit())

    def openfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)
        self.readfile(file_path)
        self.setWindowTitle(file_path)
        return file_path

    def readfile(self, file_path):
        file = QFile(file_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            stream.setCodec("UTF-8")
            self.textEdit.setPlainText(stream.readAll())
            file.close()

    def opensave(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # 弹出文件保存对话框
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)
        return file_path

    def findedit(self):
        self.Edit_6.triggered.connect(lambda: self.myedit.finduishow(self.textEdit))
        self.Edit_1.triggered.connect(lambda: self.textEdit.undo())
        self.Edit_2.triggered.connect(lambda: self.textEdit.cut())
        self.Edit_3.triggered.connect(lambda: self.textEdit.copy())
        self.Edit_4.triggered.connect(lambda: self.textEdit.paste())
        self.Edit_5.triggered.connect(lambda: self.textEdit.cut())
        self.Edit_8.triggered.connect(lambda: self.textEdit.selectAll())
        self.Edit_9.triggered.connect(lambda: self.myedit.fontselect(self.textEdit))

    def veiwset(self):
        self.current_font = self.textEdit.currentFont()
        self.View_2.triggered.connect(lambda: self.increase_font_size())
        self.View_3.triggered.connect(lambda: self.decrease_font_size())
        self.View_4.triggered.connect(lambda: self.reductive_font_size())
        self.View_5.toggled.connect(self.toolset)

    def setting(self):
        self.Help_1.triggered.connect(lambda: self.myset.setui(self.textEdit, self))

    def toolset(self):
        if self.View_5.isChecked():
            self.toolBar.show()
        else:
            self.toolBar.hide()

    def increase_font_size(self):
        # 获取当前文本的字体信息
        current_font = self.textEdit.currentFont()
        # 调整字体大小
        new_size = current_font.pointSize() + 2
        current_font.setPointSize(new_size)

        # 将新的字体信息应用于当前文本
        self.textEdit.setFont(current_font)

    def decrease_font_size(self):
        current_font = self.textEdit.currentFont()
        # 调整字体大小
        new_size = current_font.pointSize() - 2
        current_font.setPointSize(new_size)

        # 将新的字体信息应用于当前文本
        self.textEdit.setFont(current_font)

    def reductive_font_size(self):
        self.textEdit.setFont(self.current_font)

    def statusbarshow(self, str):
        self.statusBar.clearMessage()
        self.statusBar.showMessage(str, 0)

    def addstatusbarshow(self, str):
        self.statusBar.showMessage(str, 0)

    def cursorPosition(self):
        row = self.textEdit.textCursor().blockNumber()
        col = self.textEdit.textCursor().columnNumber()
        self.statusBar.showMessage("行 %d , 列 %d" % (row + 1, col + 1))


if __name__ == '__main__':
    QApp = QApplication(sys.argv)
    ui = MyWin()
    ui.show()
    sys.exit(QApp.exec_())
