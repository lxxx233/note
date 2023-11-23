from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMessageBox, QWidget

from kcsj.find import Ui_Form


class FindWin(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(FindWin, self).__init__(parent)
        self.setupUi(self)
        self.radioButton_2.setChecked(True)


class MyEdit(super):
    def __init__(self):
        self.font = None
        self.findwin = FindWin()
        self.text = ""
        self.text1 = ""

    def finduishow(self, textEdit):
        self.findwin.show()
        self.findwin.pushButton.clicked.connect(lambda: self.findtext(textEdit))
        self.findwin.pushButton_1.clicked.connect(lambda: self.replacetext(textEdit))

    def findtext(self, textEdit):
        self.text = self.findwin.lineEdit.text()
        if self.text == "":
            QtWidgets.QMessageBox.information(QMessageBox.Information, "提示", "请输入搜索内容!")
            return False
        if self.findwin.checkBox.isChecked() and self.findwin.radioButton.isChecked():
            result = textEdit.find(self.text,
                                   QtGui.QTextDocument.FindCaseSensitively | QtGui.QTextDocument.FindBackward)
        elif self.findwin.checkBox.isChecked() and self.findwin.radioButton_2.isChecked():
            result = textEdit.find(self.text, QtGui.QTextDocument.FindCaseSensitively)
        elif not self.findwin.checkBox.isChecked() and self.findwin.radioButton.isChecked():
            result = textEdit.find(self.text, QtGui.QTextDocument.FindBackward)
        else:
            result = textEdit.find(self.text)

        if not result:
            msg_box = QMessageBox(QMessageBox.Information, '提示', '找不到' + self.text)
            msg_box.exec_()
        return result

    def replacetext(self, textEdit):
        if not self.findtext(textEdit):
            return False

        self.text1 = self.findwin.lineEdit_1.text()
        if self.text1 == "":
            msg_box = QMessageBox(QMessageBox.Information, "提示", "请输入搜索内容!")
            msg_box.exec_()
            return False

        textEdit.cut()
        textEdit.insertPlainText(self.text1)

    def fontselect(self, textEdit):
        font, ok = QtWidgets.QFontDialog.getFont(self.font)
        if ok:
            self.font = font
            textEdit.setFont(font)
