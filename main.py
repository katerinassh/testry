from PyQt5 import QtWidgets
from creator import Ui_MainWindow
from create_test import Form2
from edit_test import Form3
from delete_test import Form4
import sys
import test
import os


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_test = None
        self.feedback = None

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
        elif self.radioButton_3.isChecked():
            self.pushButton_2.clicked.connect(self.window3)
        elif self.radioButton_2.isChecked():
            self.pushButton_2.clicked.connect(self.window4)

    def main_window(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    def window2(self):
        self.w2 = CreateWindow(self.lineEdit.text())
        self.w2.show()
        self.hide()

    def window3(self):
        self.w3 = EditWindow(self.lineEdit.text())
        self.w3.show()
        self.hide()

    def window4(self):
        self.w4 = DeleteWindow(self.lineEdit.text())
        self.w4.show()


class CreateWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super(CreateWindow, self).__init__()
        self.ui = Form2()
        self.ui.setupUi(self)
        self.current_test = None
        self.feedback = None
        self.title = title

        self.textEdit_2 = self.findChild(QtWidgets.QTextEdit, 'textEdit_2')
        self.textEdit_2.append(title)
        self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')

        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_2.clicked.connect(self.window1)
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.pushButton_3.clicked.connect(self.create_new_test)

    def window1(self):
        self.w1 = MainWindow()
        self.w1.show()
        self.hide()

    def create_new_test(self): # создаётся новый тест, открывается окно для редактирования
        self.current_test = test.Test(self.textEdit_2.toPlainText(), self.textEdit.toPlainText())
        self.current_test.workTestFile()
        self.current_test.createAnswerFile()

        self.w3 = EditWindow(self.title)
        self.w3.show()
        self.hide()


class EditWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super(EditWindow, self).__init__()
        self.ui = Form3()
        self.ui.setupUi(self)
        self.title = title

        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        self.label_2.setText(self.title)
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.window1)
        self.pushButton_5 = self.findChild(QtWidgets.QPushButton, 'pushButton_5')
        self.pushButton_5.clicked.connect(self.window4)

    def window1(self):
        self.w1 = MainWindow()
        self.w1.show()
        self.hide()

    def window4(self):
        self.w4 = DeleteWindow(self.title)
        self.w4.show()


class DeleteWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super(DeleteWindow, self).__init__()
        self.ui = Form4()
        self.ui.setupUi(self)
        self.title = title

        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        self.label_2.setText(self.title)
        self.label_3 = self.findChild(QtWidgets.QLabel, 'label_3')
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.close)

    def delete(self): # удаляет тест
        os.remove('{}.txt'.format(self.title))
        os.remove('{}_answers.txt'.format(self.title))
        self.label_3.setText('Deleted!')


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())