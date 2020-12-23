from PyQt5 import QtWidgets
from delete_test_design import Form4
import os


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