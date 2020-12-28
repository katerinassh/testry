from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from creator_design import Ui_MainWindow
from create_test_design import Form2
from edit_test_design import Form3
from delete_test_design import Form4
from feedback_test_design import Form5
from warning1_design import Warning1
from warning2_design import Warning2
from filter_design import Form7

import interaction_with_questions

import test
import feedback
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

        elif self.radioButton_4.isChecked():
            if self.lineEdit.text() == '':
                self.warning1()
            else:
                self.window5()

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

    def window5(self): # показывает окно для получения результатов теста
        self.w5 = FeedbackWindow(self.lineEdit.text())
        if FileNotFoundError:
            self.warning2()
        self.w5.show()
        self.hide()

    def warning1(self): # показывает окно с предупреждением о том, что назввание теста было не написано
        self.war = WarningWindow1()
        self.war.show()

    def warning2(self): # показывает окно с предупреждением о том, что такого теста не существует
        self.war = WarningWindow2()
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
        self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')

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
        self.pushButton_6 = self.findChild(QtWidgets.QPushButton, 'pushButton_6')
        self.pushButton_6.clicked.connect(self.refresh)
        self.loadFile()
        self.open()
        #self.upd_feedback()

    def loadFile(self): # загружает на форму тест из файла
        file = open('{}.txt'.format(self.title), 'r')
        with file:
            data = file.read()
        self.textEdit.setText(data)

    def refresh(self):
        self.loadFile()

    def open(self): # открывает тест
        file = open('{}.txt'.format(self.title), 'r')
        title = file.readline().strip('\n')
        description = file.readline().strip('\n')
        _ = file.readline()
        self.current_test = test.Test(title, description)

        self.current_test.readFromFile(file)

    def window1(self):
        self.w1 = MainWindow()
        self.w1.show()
        self.hide()

    def window4(self):
        self.w4 = DeleteWindow(self.title)
        self.w4.show()

    def selectQstAdd(self):
        self.wAdd = interaction_with_questions.AddQuestion(self.current_test)
        self.current_test.qamount += 1
        self.wAdd.show()

    def selectQstEdit(self):
        self.wEdit = interaction_with_questions.EditQuestion(self.current_test)
        self.wEdit.show()

    def selectQstDelete(self):
        self.wDelete = interaction_with_questions.DeleteQuestion(self.current_test)
        self.wDelete.show()


class FeedbackWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super(FeedbackWindow, self).__init__()
        self.ui = Form5()
        self.ui.setupUi(self)

        self.title = title
        self.current_test = None
        self.open()
        self.feedback = feedback.Feedback(self.title, len(self.current_test.questions))

        self.label_2 = self.findChild(QtWidgets.QLabel, 'label_2')
        self.label_2.setText(self.title)
        self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.textEdit_2 = self.findChild(QtWidgets.QTextEdit, 'textEdit_2')
        self.textEdit_2.hide()

        self.pushButton_1 = self.findChild(QtWidgets.QPushButton, 'pushButton_1')
        self.pushButton_1.clicked.connect(self.selectSortName)
        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_2.clicked.connect(self.selectSortMark)
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.pushButton_3.clicked.connect(self.selectFilter)
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.selectStatictics)

        self.pushButton_5 = self.findChild(QtWidgets.QPushButton, 'pushButton_5')
        self.pushButton_5.clicked.connect(self.window1)
        self.pushButton_6 = self.findChild(QtWidgets.QPushButton, 'pushButton_6')  #  кнопка збереження змін в основному файлі
        self.pushButton_6.clicked.connect(self.saveChanges)
        self.pushButton_7 = self.findChild(QtWidgets.QPushButton, 'pushButton_7')
        self.pushButton_7.clicked.connect(self.loadFile)
        self.loadFile()

    def loadFile(self): # загружает на форму ответы из файла
        file = open('{}_answers.txt'.format(self.title), 'r')
        with file:
            data = file.read()
            file.close()
        self.textEdit_2.hide()
        self.textEdit.setText(data)

    def saveChanges(self):
        data = self.textEdit.text()
        print(data)
        # file = open('{}_answers.txt'.format(self.title), 'w')
        # with file:
        #     file.write(data)
        #     file.close()
        # self.loadFile()

    def open(self):  # открывает тест
        file = open('{}.txt'.format(self.title), 'r')
        title = file.readline().strip('\n')
        description = file.readline().strip('\n')
        _ = file.readline()
        self.current_test = test.Test(title, description)

        self.current_test.readFromFile(file)

    def selectSortName(self):
        self.feedback.sort_by_name()
        file = open('{}_name-sorted.txt'.format(self.title), 'r')
        with file:
            data = file.read()
        self.textEdit_2.show()
        self.textEdit_2.setText(data)

    def selectSortMark(self):
        self.feedback.sort_by_mark()
        file = open('{}_mark-sorted.txt'.format(self.title), 'r')
        with file:
            data = file.read()
        self.textEdit_2.show()
        self.textEdit_2.setText(data)

    def selectStatictics(self):
        max_mark = float(self.current_test.totalTestMark())
        self.feedback.statistic_by_mark(max_mark)
        file = open('{}_statistic.txt'.format(self.title), 'r')
        with file:
            data = file.read()
        self.textEdit_2.show()
        self.textEdit_2.setText(data)

    def selectFilter(self):
        self.wFilter = FilterWindow(self.title)
        self.wFilter.show()

        # name = self.wFilter.file_name()
        # file = open('{}_{}.txt'.format(self.title, name), "r")
        # with file:
        #     data = file.read()
        # self.textEdit_2.show()
        # self.textEdit_2.setText(data)

        # info = []
        # info = FilterWindow.btn_pushed()
        # mark = info[0]
        # dir = info[1]

        # mark = FilterWindow.mark
        # dir = FilterWindow.limit_dir
        #
        # print(mark, dir)
        # self.feedback.filter_by_mark(n, n)
        #
        # lim_name = self.limit_dir + str(self.mark)
        # file = open('{}_{}.txt'.format(self.title, lim_name), 'r')
        # with file:
        #     data = file.read()
        # self.textEdit_2.show()
        # self.textEdit_2.setText(data)

    def window1(self):
        self.w1 = MainWindow()
        self.w1.show()
        self.hide()

    def window4(self):
        self.w4 = DeleteWindow(self.title)
        self.w4.show()


class FilterWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super(FilterWindow, self).__init__()
        self.ui = Form7()
        self.ui.setupUi(self)

        self.title = title
        self.current_test = None
        self.open()
        self.feedback = feedback.Feedback(self.title, len(self.current_test.questions))

        self.radioButton = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.radioButton_3 = self.findChild(QtWidgets.QRadioButton, 'radioButton_3')
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.btn_pushed)

    def btn_pushed(self):
        limit_dir = 'more'
        if self.radioButton.isChecked():
            limit_dir = 'more'
        elif self.radioButton_3.isChecked():
            limit_dir = 'less'
        mark = self.lineEdit.text()
        self.hide()

        self.feedback.filter_by_mark(mark, limit_dir)

        lim_name = limit_dir + str(mark)
        file = open('{}_{}.txt'.format(self.title, lim_name), "r")
        with file:
            data = file.read()
        FeedbackWindow.textEdit_2.show()
        FeedbackWindow.textEdit_2.setText(data)

    def file_name(self):
        return self.limit_dir + str(self.mark)


    def open(self): # открывает тест
        file = open('{}.txt'.format(self.title), 'r')
        title = file.readline().strip('\n')
        description = file.readline().strip('\n')
        _ = file.readline()
        self.current_test = test.Test(title, description)

        self.current_test.readFromFile(file)



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


class WarningWindow1(QtWidgets.QMainWindow):
    def __init__(self):
        super(WarningWindow1, self).__init__()
        self.ui = Warning1()
        self.ui.setupUi(self)

        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.close)


class WarningWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(WarningWindow2, self).__init__()
        self.ui = Warning2()
        self.ui.setupUi(self)

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.close)


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
