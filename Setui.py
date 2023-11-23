from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QBrush, QPixmap, QTextCursor
from PyQt5.QtWidgets import QWidget, QFileDialog, QColorDialog

from kcsj.set import Ui_Form


class SetWin(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(SetWin, self).__init__(parent)
        self.setupUi(self)


class MySet(super):
    def __init__(self):
        self.font = None
        self.setwin = SetWin()

    def setui(self, textEdit, MyWin):
        self.setwin.show()
        self.setwin.pushButton.clicked.connect(lambda: self.setfont(textEdit))
        self.setwin.pushButton_2.clicked.connect(lambda: self.setbackground(MyWin))

    def setfont(self, textEdit):
        font, ok = QtWidgets.QFontDialog.getFont(self.font)
        if ok:
            self.font = font
            textEdit.setFont(font)

    def setbackground(self, MyWin):
        palette = QtGui.QPalette()
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(MyWin, "选择图片", "", "Image Files (*.png *.jpg *.bmp)",
                                                   options=options)
        palette.setBrush(MyWin.backgroundRole(), QBrush(
            QPixmap(file_path).scaled(MyWin.size(),
                                      QtCore.Qt.IgnoreAspectRatio,
                                      QtCore.Qt.SmoothTransformation)))
        MyWin.setPalette(palette)


