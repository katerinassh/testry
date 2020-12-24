from PyQt5 import QtWidgets
from creator_design import Ui_MainWindow
from create_test_design import Form2
from edit_test_design import Form3
from delete_test_design import Form4
import interaction_with_questions

import warnings
import test
import sys
import os


class MainWindow(QtWidgets.QMainWindow): # главный экран программы
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_test = None
        self.title = None
        self.feedback = None

        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.radioButton = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.radioButton_2 = self.findChild(QtWidgets.QRadioButton, 'radioButton_2')
        self.radioButton_3 = self.findChild(QtWidgets.QRadioButton, 'radioButton_3')
        self.radioButton_4 = self.findChild(QtWidgets.QRadioButton, 'radioButton_4')
        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')

        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)

    def pushButton_2_clicked(self): # выбор действия с creator mode
        if self.radioButton.isChecked():
            self.window2()

        elif self.radioButton_3.isChecked():
            if self.lineEdit.text() == '':
                self.warning1()
            else:
                self.window3()

        elif self.radioButton_2.isChecked():
            if self.lineEdit.text() == '':
                self.warning1()
            else:
                self.window4()

    def main_window(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    def window2(self): # показывает окно для создания теста
        self.w2 = CreateWindow(self.lineEdit.text())
        self.w2.show()
        self.hide()

    def window3(self): # показывает окно для редактирования теста
        self.w3 = EditWindow(self.lineEdit.text())
        if FileNotFoundError:
            self.warning2()
        self.w3.show()
        self.hide()

    def window4(self): # показывает окно для удаления теста
        self.w4 = DeleteWindow(self.lineEdit.text())
        if FileNotFoundError:
            self.warning2()
        self.w4.show()

    def warning1(self): # показывает окно с предупреждением о том, что назввание теста было не написано
        self.war = warnings.WarningWindow1()
        self.war.show()

    def warning2(self): # показывает окно с предупреждением о том, что такого теста не существует
        self.war = warnings.WarningWindow2()
        self.war.show()


class CreateWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super(CreateWindow, self).__init__()
        self.ui = Form2()
        self.ui.setupUi(self)
        self.current_test = None
        self.feedback = None
        self.title = title

        self.textEdit_2 = self.findChild(QtWidgets.QTextEdit, 'textEdit_2')
        self.textEdit_2.append(self.title)
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
        self.title = self.textEdit_2.toPlainText()
        self.current_test = test.Test(self.title, self.textEdit.toPlainText())
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
        self.current_test = None

        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        self.label_2.setText(self.title)
        self.label_3 = self.findChild(QtWidgets.QLabel, 'label_3')

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.selectQstAdd)
        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_2.clicked.connect(self.selectQstEdit)
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.pushButton_3.clicked.connect(self.selectQstDelete)
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.window1)
        self.pushButton_5 = self.findChild(QtWidgets.QPushButton, 'pushButton_5')
        self.pushButton_5.clicked.connect(self.window4)
        self.loadFile()
        self.open()
        #self.upd_feedback()

    def loadFile(self): # загружает на форму тест из файла
        file = open('{}.txt'.format(self.title), 'r')
        with file:
            data = file.read()
        self.label_3.setText(data)

    def open(self): # открывает тест
        file = open('{}.txt'.format(self.title), 'r')
        title = file.readline().strip('\n')
        description = file.readline().strip('\n')
        _ = file.readline()
        self.current_test = test.Test(title, description)
        #self.current_test.readFromFile(file)

   # def upd_feedback(self):
    #    self.feedback = feedback.Feedback(self.current_test.title, len(self.current_test.questions))

    def window1(self):
        self.w1 = MainWindow()
        self.w1.show()
        self.hide()

    def window4(self):
        self.w4 = DeleteWindow(self.title)
        self.w4.show()

    def selectQstAdd(self):
        self.wAdd = interaction_with_questions.AddQuestion(self.title, self.current_test)
        self.wAdd.show()

    def selectQstEdit(self):
        self.wEdit = interaction_with_questions.EditQuestion(self.title, self.current_test)
        self.wEdit.show()

    def selectQstDelete(self):
        self.wDelete = interaction_with_questions.DeleteQuestion(self.title, self.current_test)
        self.wDelete.show()


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
        self.pushButton_4.clicked.connect(self.window1)

    def window1(self):
        self.w1 = MainWindow()
        self.w1.show()
        self.hide()

    def delete(self): # удаляет тест
        os.remove('{}.txt'.format(self.title))
        os.remove('{}_answers.txt'.format(self.title))
        self.label_3.setText('Deleted!')


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())