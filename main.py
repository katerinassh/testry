from PyQt5 import QtWidgets
from creator import Ui_MainWindow
from create_test import Form2
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.radioButton = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.radioButton_2 = self.findChild(QtWidgets.QRadioButton, 'radioButton_2')
        self.radioButton_3 = self.findChild(QtWidgets.QRadioButton, 'radioButton_3')
        self.radioButton_4 = self.findChild(QtWidgets.QRadioButton, 'radioButton_4')
        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')

        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)

    def pushButton_2_clicked(self):
        if self.radioButton.isChecked():
            self.pushButton_2.clicked.connect(self.window2)

    def main_window(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    def window2(self):
        self.w = CreateWindow(self.lineEdit.text())
        self.w.show()
        self.hide()


class CreateWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super(CreateWindow, self).__init__()
        self.ui = Form2()
        self.ui.setupUi(self)

        self.textEdit_2 = self.findChild(QtWidgets.QTextEdit, 'textEdit_2')
        self.textEdit_2.append(title)



app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())