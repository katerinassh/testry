from PyQt5 import QtWidgets
from add1_design import Form0

from addQstText_design import Form_AddQstText
from addQstTF_design import Form_AddQstTF
from addQstOneAnswer_design import Form_AddQstOneAnswer
from addQstSomeAnswer_design import Form_AddQstSomeAnswer

from edit_question_design import Form6
from delete_question_design import Form7

import types_of_questions


class AddQuestion(QtWidgets.QMainWindow): #окно для выбора типа вопроса
    def __init__(self, test):
        super(AddQuestion, self).__init__()
        self.ui = Form0()
        self.ui.setupUi(self)
        self.current_test = test
        self.qst = None

        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton_next')
        self.pushButton.clicked.connect(self.add)

    def add(self):  # метод додає нове питання у тест
        if str(self.comboBox.currentText()) == 'True/False':
            self.qst = types_of_questions.QstTrueFalse()
            self.wAddQstTF = AddQstTF(self.current_test, self.qst)
            self.wAddQstTF.show()
        elif str(self.comboBox.currentText()) == 'Text answer':
            self.qst = types_of_questions.QstEnterText()
            self.wAddQstText = AddQstText(self.current_test, self.qst)
            self.wAddQstText.show()
        elif str(self.comboBox.currentText()) == 'With answer options':
            self.qst = types_of_questions.QstOneAnswer()
            self.wAddQstOneAnswer = AddQstOneAnswer(self.current_test, self.qst)
            self.wAddQstOneAnswer.show()
        elif str(self.comboBox.currentText()) == 'Flags':
            self.qst = types_of_questions.QstSomeAnswer()
            self.wAddQstSomeAnswer = AddQstSomeAnswer(self.current_test, self.qst)
            self.wAddQstSomeAnswer.show()
        elif str(self.comboBox.currentText()) == 'Linear Scale':
            self.qst = types_of_questions.QstScale()
            #self.wAddQstScale = AddQstScale(self.current_test, self.qst)
            #self.wAddQstScale.show()
        elif str(self.comboBox.currentText()) == 'Table with answer options':
            self.qst = types_of_questions.QstTableOne()
            #self.wAddTableOne = AddQstTableOne(self.current_test, self.qst)
            #self.wAddQstTableOne.show()
        elif str(self.comboBox.currentText()) == 'Grid of flags':
            self.qst = types_of_questions.QstTable()
            #self.wAddTable = AddQstTable(self.current_test, self.qst)
            #self.wAddQstTable.show()
        else:
            self.qst = types_of_questions.QstName()
        self.hide()


class AddQstText(QtWidgets.QMainWindow): # окно для добавление типа вопроса QstEnterText
    def __init__(self, test, qst):
        super(AddQstText, self).__init__()
        self.ui = Form_AddQstText()
        self.ui.setupUi(self)

        self.current_test = test
        self.qst = qst

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

    def add(self): # добавление параметров
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst._question = self.lineEdit.text()
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.qst._right_answer = self.lineEdit_4.text()
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.qst.rating = self.lineEdit_2.text()

    def w(self): #добавление вопроса в тест и файл теста
        self.add()
        self.current_test.questions.append(self.qst)
        self.current_test.workTestFile()
        self.hide()


class AddQstTF(QtWidgets.QMainWindow):
    def __init__(self, test, qst):
        super(AddQstTF, self).__init__()
        self.ui = Form_AddQstTF()
        self.ui.setupUi(self)

        self.current_test = test
        self.qst = qst

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

        self.radioButton = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.radioButton_2 = self.findChild(QtWidgets.QRadioButton, 'radioButton_2')


    def add(self): # добавление параметров
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst._question = self.lineEdit.text()
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.qst.rating = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            self.qst._right_answer = "True"
        elif self.radioButton_2.isChecked():
            self.qst._right_answer = "False"

    def w(self):  # добавление вопроса в тест и файл теста
        self.add()
        self.current_test.questions.append(self.qst)
        self.current_test.workTestFile()
        self.hide()


class AddQstOneAnswer(QtWidgets.QMainWindow):
    def __init__(self, test, qst):
        super(AddQstOneAnswer, self).__init__()
        self.ui = Form_AddQstOneAnswer()
        self.ui.setupUi(self)

        self.current_test = test
        self.qst = qst
        # self.qst.numOptions = 2

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_2.clicked.connect(self.display_3)
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.pushButton_3.clicked.connect(self.display_4)
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.display_5)

        self.radioButton = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.radioButton_2 = self.findChild(QtWidgets.QRadioButton, 'radioButton_2')
        self.radioButton_3 = self.findChild(QtWidgets.QRadioButton, 'radioButton_3')
        self.radioButton_3.hide()
        self.radioButton_4 = self.findChild(QtWidgets.QRadioButton, 'radioButton_4')
        self.radioButton_4.hide()
        self.radioButton_5 = self.findChild(QtWidgets.QRadioButton, 'radioButton_5')
        self.radioButton_5.hide()

        self.lineEdit_3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.lineEdit_5 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.lineEdit_5.hide()
        self.lineEdit_6 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_6')
        self.lineEdit_6.hide()
        self.lineEdit_7 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_7')
        self.lineEdit_7.hide()

    def display_3(self):
        self.pushButton_2.hide()
        self.radioButton_3.show()
        self.lineEdit_5.show()
        # self.qst.numOptions = 3

    def display_4(self):
        self.pushButton_3.hide()
        self.radioButton_4.show()
        self.lineEdit_6.show()
        # self.qst.numOptions = 4

    def display_5(self):
        self.pushButton_4.hide()
        self.radioButton_5.show()
        self.lineEdit_7.show()
        # self.qst.numOptions = 5

    def add(self): # добавление параметров
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst._question = self.lineEdit.text()
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        # self.qst.setRating(self.lineEdit_2.text())
        self.qst.rating = self.lineEdit_2.text()

        if self.lineEdit_3.text() != 'choice':
            self.qst._answerOptions.append(self.lineEdit_3.text())
        if self.lineEdit_4.text() != 'choice':
            self.qst._answerOptions.append(self.lineEdit_4.text())
        if self.lineEdit_5.text() != 'choice':
            self.qst._answerOptions.append(self.lineEdit_5.text())
        if self.lineEdit_6.text() != 'choice':
            self.qst._answerOptions.append(self.lineEdit_6.text())
        if self.lineEdit_7.text() != 'choice':
            self.qst._answerOptions.append(self.lineEdit_7.text())

        if self.radioButton.isChecked():
            self.qst._rightAnswerIndex = 1
        elif self.radioButton_2.isChecked():
            self.qst._rightAnswerIndex = 2
        elif self.radioButton_3.isChecked():
            self.qst._rightAnswerIndex = 3
        elif self.radioButton_4.isChecked():
            self.qst._rightAnswerIndex = 4
        elif self.radioButton_5.isChecked():
            self.qst._rightAnswerIndex = 5

    def w(self):  # добавление вопроса в тест и файл теста
        self.add()
        self.current_test.questions.append(self.qst)
        self.current_test.workTestFile()
        self.hide()


class AddQstSomeAnswer(QtWidgets.QMainWindow):
    def __init__(self, test, qst):
        super(AddQstSomeAnswer, self).__init__()
        self.ui = Form_AddQstSomeAnswer()
        self.ui.setupUi(self)

        self.current_test = test
        self.qst = qst

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        # self.pushButton.clicked.connect(self.w)

        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_2.clicked.connect(self.display_3)
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.pushButton_3.clicked.connect(self.display_4)
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.display_5)

        self.checkBox = self.findChild(QtWidgets.QCheckBox, 'checkBox')
        self.checkBox_2 = self.findChild(QtWidgets.QCheckBox, 'checkBox_2')
        self.checkBox_3 = self.findChild(QtWidgets.QCheckBox, 'checkBox_3')
        self.checkBox_3.hide()
        self.checkBox_4 = self.findChild(QtWidgets.QCheckBox, 'checkBox_4')
        self.checkBox_4.hide()
        self.checkBox_5 = self.findChild(QtWidgets.QCheckBox, 'checkBox_5')
        self.checkBox_5.hide()

        self.lineEdit_3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.lineEdit_5 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.lineEdit_5.hide()
        self.lineEdit_6 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_6')
        self.lineEdit_6.hide()
        self.lineEdit_7 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_7')
        self.lineEdit_7.hide()

    def display_3(self):
        self.pushButton_2.hide()
        self.checkBox_3.show()
        self.lineEdit_5.show()

        # self.qst.numOptions = 3

    def display_4(self):
        self.pushButton_3.hide()
        self.checkBox_4.show()
        self.lineEdit_6.show()

        # self.qst.numOptions = 4

    def display_5(self):
        self.pushButton_4.hide()
        self.checkBox_5.show()
        self.lineEdit_7.show()

        # self.qst.numOptions = 5

    # def add(self): # добавление параметров
    #     self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
    #     self.qst._question = self.lineEdit.text()
    #     self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
    #     # self.qst.setRating(self.lineEdit_2.text())
    #     self.qst.rating = self.lineEdit_2.text()
    #
    #     if self.lineEdit_3.text() != 'choice':
    #         self.qst._answerOptions.append(self.lineEdit_3.text())
    #     if self.lineEdit_4.text() != 'choice':
    #         self.qst._answerOptions.append(self.lineEdit_4.text())
    #     if self.lineEdit_5.text() != 'choice':
    #         self.qst._answerOptions.append(self.lineEdit_5.text())
    #     if self.lineEdit_6.text() != 'choice':
    #         self.qst._answerOptions.append(self.lineEdit_6.text())
    #     if self.lineEdit_7.text() != 'choice':
    #         self.qst._answerOptions.append(self.lineEdit_7.text())
    #
    #     if self.checkBox.isChecked():
    #         self.qst._rightAnswerIndexArr.append('1')
    #     if self.checkBox_2.isChecked():
    #         self.qst._rightAnswerIndexArr.append('2')
    #     if self.checkBox_3.isChecked():
    #         self.qst._rightAnswerIndexArr.append('3')
    #     if self.checkBox_4.isChecked():
    #         self.qst._rightAnswerIndexArr.append('4')
    #     if self.checkBox_5.isChecked():
    #         self.qst._rightAnswerIndexArr.append('5')
    #
    # def w(self):  # добавление вопроса в тест и файл теста
    #     self.add()
    #     self.current_test.questions.append(self.qst)
    #     self.current_test.workTestFile()
    #     self.hide()


class EditQuestion(QtWidgets.QMainWindow): # окно для выбора вопроса для редактирования
    def __init__(self, test):
        super(EditQuestion, self).__init__()
        self.ui = Form6()
        self.ui.setupUi(self)
        self.current_test = test

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')
        for i in range(1, len(self.current_test.questions)):
            self.comboBox.addItem(str(i) + " - " + self.current_test.questions[i]._question)


class DeleteQuestion(QtWidgets.QMainWindow): # окно для выбора вопроса для удаления
    def __init__(self, test):
        super(DeleteQuestion, self).__init__()
        self.ui = Form6()
        self.ui.setupUi(self)
        self.current_test = test

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')