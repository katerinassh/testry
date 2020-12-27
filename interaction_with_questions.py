from PyQt5 import QtWidgets
from add1_design import Form0

from addQstText_design import Form_AddQstText
from addQstTF_design import Form_AddQstTF
from addQstOneAnswer_design import Form_AddQstOneAnswer
from addQstSomeAnswer_design import Form_AddQstSomeAnswer

from edQstTF_design import Form_EdQstTF
from edQstText_design import Form_EdQstText
from edQstOneAnswer_design import Form_EdQstOneAnswer
from edQstSomeAnswer_design import Form_EdQstSomeAnswer

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
        self.qst.numOptions = 2

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
        self.qst.numOptions = 3

    def display_4(self):
        self.pushButton_3.hide()
        self.radioButton_4.show()
        self.lineEdit_6.show()
        self.qst.numOptions = 4

    def display_5(self):
        self.pushButton_4.hide()
        self.radioButton_5.show()
        self.lineEdit_7.show()
        self.qst.numOptions = 5

    def add(self): # добавление параметров
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst._question = self.lineEdit.text()
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.qst.setRating(self.lineEdit_2.text())
        self.qst.rating = self.lineEdit_2.text()

        if self.lineEdit_3.text() != '':
            self.qst._answerOptions.append(self.lineEdit_3.text())
        if self.lineEdit_4.text() != '':
            self.qst._answerOptions.append(self.lineEdit_4.text())
        if self.lineEdit_5.text() != '':
            self.qst._answerOptions.append(self.lineEdit_5.text())
        if self.lineEdit_6.text() != '':
            self.qst._answerOptions.append(self.lineEdit_6.text())
        if self.lineEdit_7.text() != '':
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
        self.numOptions = 2

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

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

        self.qst.numOptions = 3

    def display_4(self):
        self.pushButton_3.hide()
        self.checkBox_4.show()
        self.lineEdit_6.show()

        self.qst.numOptions = 4

    def display_5(self):
        self.pushButton_4.hide()
        self.checkBox_5.show()
        self.lineEdit_7.show()

        self.qst.numOptions = 5

    def add(self): # добавление параметров
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst._question = self.lineEdit.text()
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.qst.setRating(self.lineEdit_2.text())
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

        if self.checkBox.isChecked():
            self.qst._rightAnswerIndexArr.append('1')
        if self.checkBox_2.isChecked():
            self.qst._rightAnswerIndexArr.append('2')
        if self.checkBox_3.isChecked():
            self.qst._rightAnswerIndexArr.append('3')
        if self.checkBox_4.isChecked():
            self.qst._rightAnswerIndexArr.append('4')
        if self.checkBox_5.isChecked():
            self.qst._rightAnswerIndexArr.append('5')

    def w(self):  # добавление вопроса в тест и файл теста
        self.add()
        self.current_test.questions.append(self.qst)
        self.current_test.workTestFile()
        self.hide()


class EditQuestion(QtWidgets.QMainWindow): # окно для выбора вопроса для редактирования
    def __init__(self, test):
        super(EditQuestion, self).__init__()
        self.ui = Form6()
        self.ui.setupUi(self)
        self.current_test = test
        self.qst = None

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.select_qst_for_editing)
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')
        for i in range(1, len(self.current_test.questions)):
            self.comboBox.addItem(str(i) + " - " + self.current_test.questions[i]._question)

    def select_qst_for_editing(self): # определеняет, какой вопрос нужно открыть для редактирования
        number = int(str(self.comboBox.currentText()).split(" - ")[0])
        type = self.current_test.questions[number].__doc__
        self.qst = self.current_test.questions[number]
        if type == 'True/False':
            self.wEdQstTF = EdQstTF(self.current_test, self.qst, number)
            self.wEdQstTF.show()
        elif type == 'Text answer':
            self.wEdQstText = EdQstText(self.current_test, self.qst, number)
            self.wEdQstText.show()
        elif type == 'With answer options':
            self.wEdQstOneAnswer = EdQstOneAnswer(self.current_test, self.qst, number)
            self.wEdQstOneAnswer.show()
        elif type == 'Flags':
            self.wEdQstSomeAnswer = EdQstSomeAnswer(self.current_test, self.qst, number)
            self.wEdQstSomeAnswer.show()
        #elif type == 'Linear Scale':
            # self.wEdQstScale = EdQstScale(self.current_test, self.qst, number)
            # self.wEdQstScale.show()
        #elif type == 'Table with answer options':
            # self.wEdTableOne = EdQstTableOne(self.current_test, self.qst, number)
            # self.wEdQstTableOne.show()
        #elif type == 'Grid of flags':
            # self.wAddTable = AddQstTable(self.current_test, self.qst, number)
            # self.wAddQstTable.show()
        self.hide()


class EdQstTF(QtWidgets.QMainWindow): # окно для редактирование true/false question
    def __init__(self, test, qst, number):
        super(EdQstTF, self).__init__()
        self.ui = Form_EdQstTF()
        self.ui.setupUi(self)

        self.current_test = test
        self.qst = qst
        self.number = number

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.lineEdit.setText(self.qst._question)
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.lineEdit_2.setText(str(self.qst.rating))
        self.radioButton = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.radioButton_2 = self.findChild(QtWidgets.QRadioButton, 'radioButton_2')
        if self.qst._right_answer == 'True':
            self.radioButton.setChecked(True)
        if self.qst._right_answer == 'False':
            self.radioButton_2.setChecked(True)

    def edit(self): # пересмотр полей с параметрами
        self.qst._question = self.lineEdit.text()
        self.qst.rating = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            self.qst._right_answer = "True"
        elif self.radioButton_2.isChecked():
            self.qst._right_answer = "False"

    def w(self):  # удаление вопроса с теста, замена на отредактированый и запись в файл теста
        self.edit()
        self.current_test.questions.pop(self.number)
        self.current_test.questions.insert(self.number, self.qst)
        self.current_test.workTestFile()
        self.hide()


class EdQstText(QtWidgets.QMainWindow): # окно для редактирование Text answer question
    def __init__(self, test, qst, number):
        super(EdQstText, self).__init__()
        self.ui = Form_EdQstText()
        self.ui.setupUi(self)

        self.current_test = test
        self.qst = qst
        self.number = number

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.lineEdit.setText(self.qst._question)
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.lineEdit_2.setText(str(self.qst.rating))
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.lineEdit_4.setText(self.qst._right_answer)

    def edit(self):  # пересмотр полей с параметрами
        self.qst._question = self.lineEdit.text()
        self.qst.rating = self.lineEdit_2.text()
        self.qst._right_answer = self.lineEdit_4.text()

    def w(self):  # удаление вопроса с теста, замена на отредактированый и запись в файл теста
        self.edit()
        self.current_test.questions.pop(self.number)
        self.current_test.questions.insert(self.number, self.qst)
        self.current_test.workTestFile()
        self.hide()


class EdQstOneAnswer(QtWidgets.QMainWindow): # окно для редактирование question with options
    def __init__(self, test, qst, number):
        super(EdQstOneAnswer, self).__init__()
        self.ui = Form_EdQstOneAnswer()
        self.ui.setupUi(self)

        self.current_test = test
        self.qst = qst
        self.number = number

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.lineEdit.setText(self.qst._question)
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.lineEdit_2.setText(str(self.qst.rating))

        self.radioButton = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.radioButton_2 = self.findChild(QtWidgets.QRadioButton, 'radioButton_2')
        self.radioButton_3 = self.findChild(QtWidgets.QRadioButton, 'radioButton_3')
        self.radioButton_4 = self.findChild(QtWidgets.QRadioButton, 'radioButton_4')
        self.radioButton_5 = self.findChild(QtWidgets.QRadioButton, 'radioButton_5')
        self.lineEdit_3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        self.lineEdit_3.setText(self.qst._answerOptions[0])
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.lineEdit_4.setText(self.qst._answerOptions[1])
        self.lineEdit_5 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.lineEdit_6 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_6')
        self.lineEdit_7 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_7')
        self.radioButton_3.hide()
        self.radioButton_4.hide()
        self.radioButton_5.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()

        self.pushButton_2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_2.clicked.connect(self.display_3)
        self.pushButton_3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.pushButton_3.clicked.connect(self.display_4)
        self.pushButton_4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.pushButton_4.clicked.connect(self.display_5)

        if (len(self.qst._answerOptions) >= 3):
            self.lineEdit_5.setText(self.qst._answerOptions[2])
            self.radioButton_3.show()
            self.lineEdit_5.show()
            self.pushButton_2.hide()
        if (len(self.qst._answerOptions) >= 4):
            self.lineEdit_6.setText(self.qst._answerOptions[3])
            self.radioButton_4.show()
            self.lineEdit_6.show()
            self.pushButton_3.hide()
        if (len(self.qst._answerOptions) == 5):
            self.radioButton_5.show()
            self.lineEdit_7.show()
            self.pushButton_4.hide()

        if self.qst._rightAnswerIndex == 1:
            self.radioButton.setChecked(True)
        elif self.qst._rightAnswerIndex == 2:
            self.radioButton_2.setChecked(True)
        elif self.qst._rightAnswerIndex == 3:
            self.radioButton_3.setChecked(True)
        elif self.qst._rightAnswerIndex == 4:
            self.radioButton_4.setChecked(True)
        elif self.qst._rightAnswerIndex == 5:
            self.radioButton_5.setChecked(True)

    def edit(self): # пересмотр полей с параметрами
        self.qst._question = self.lineEdit.text()
        self.qst.rating = self.lineEdit_2.text()
        self.qst._answerOptions = [] * self.qst.numOptions
        if self.qst.numOptions >= 1:
            if self.lineEdit_3.text() != '':
                self.qst._answerOptions.append(self.lineEdit_3.text())
        if self.qst.numOptions >= 2:
            if self.lineEdit_4.text() != '':
                self.qst._answerOptions.append(self.lineEdit_4.text())
        if self.qst.numOptions >= 3:
            if self.lineEdit_5.text() != '':
                self.qst._answerOptions.append(self.lineEdit_5.text())
        if self.qst.numOptions >= 4:
            if self.lineEdit_6.text() != '':
                self.qst._answerOptions.append(self.lineEdit_6.text())
        if self.qst.numOptions == 5:
            if self.lineEdit_7.text() != '':
                self.qst._answerOptions.append(self.lineEdit_7.text())
        if self.radioButton.isChecked():
            self.qst._rightAnswerIndex = 1
        elif self.radioButton_2.isChecked():
            self.qst._rightAnswerIndex = 2
        elif self.radioButton_3.isChecked():
            self.qst._rightAnswerIndex = 3
        elif self.radioButton_4.isChecked():
            self.qst._rightAnswerIndex = 4
        else:
            self.qst._rightAnswerIndex = 5

    def display_3(self): # отображение 3 опций
        self.pushButton_2.hide()
        self.radioButton_3.show()
        self.lineEdit_5.show()
        self.qst.numOptions = 3

    def display_4(self): # отображение 4 опций
        self.pushButton_3.hide()
        self.radioButton_4.show()
        self.lineEdit_6.show()
        self.qst.numOptions = 4

    def display_5(self): # отображение 5 опций
        self.pushButton_4.hide()
        self.radioButton_5.show()
        self.lineEdit_7.show()
        self.qst.numOptions = 5

    def w(self):  # удаление вопроса с теста, замена на отредактированый и запись в файл теста
        self.edit()
        self.current_test.questions.pop(self.number)
        self.current_test.questions.insert(self.number, self.qst)
        self.current_test.workTestFile()
        self.hide()


class DeleteQuestion(QtWidgets.QMainWindow): # окно для выбора вопроса для удаления
    def __init__(self, test):
        super(DeleteQuestion, self).__init__()
        self.ui = Form7()
        self.ui.setupUi(self)
        self.current_test = test

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.delete_qst)
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')
        for i in range(1, len(self.current_test.questions)):
            self.comboBox.addItem(str(i) + " - " + self.current_test.questions[i]._question)

    def delete_qst(self): # удаляет выбранный вопрос
        number = int(str(self.comboBox.currentText()).split(" - ")[0])
        self.current_test.questions.pop(number)
        self.current_test.qamount -= 1
        self.current_test.workTestFile()
        self.hide()
