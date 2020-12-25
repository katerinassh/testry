from PyQt5 import QtWidgets
from add1_design import Form0
from addQstText_design import Form_AddQstText
from addQstTF_design import Form_AddQstTF
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
            self.wAddQstTF = AddQstTF()
            self.wAddQstTF.show()
        elif str(self.comboBox.currentText()) == 'Text answer':
            self.qst = types_of_questions.QstEnterText()
            self.wAddQstText = AddQstText(self.current_test, self.qst)
            self.wAddQstText.show()
        elif str(self.comboBox.currentText()) == 'With answer options':
            qst = types_of_questions.QstOneAnswer()
        elif str(self.comboBox.currentText()) == 'Flags':
            qst = types_of_questions.QstSomeAnswer()
        elif str(self.comboBox.currentText()) == 'Linear Scale':
            qst = types_of_questions.QstScale()
        elif str(self.comboBox.currentText()) == 'Table with answer options':
            qst = types_of_questions.QstTableOne()
        elif str(self.comboBox.currentText()) == 'Grid of flags':
            qst = types_of_questions.QstTable()
        else:
            qst = types_of_questions.QstName()
        self.hide()


class AddQstText(QtWidgets.QMainWindow):
    def __init__(self, test, qst):
        super(AddQstText, self).__init__()
        self.ui = Form_AddQstText()
        self.ui.setupUi(self)
        self.current_test = test
        self.qst = qst

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.w)

    def add(self):
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst._question = self.lineEdit.text()
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.qst._right_answer = self.lineEdit_4.text()
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.qst.rating = self.lineEdit_2.text()

    def w(self):
        self.add()
        self.current_test.questions.append(self.qst)
        self.hide()


class AddQstTF(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddQstTF, self).__init__()
        self.ui = Form_AddQstTF()
        self.ui.setupUi(self)




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