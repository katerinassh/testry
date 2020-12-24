from PyQt5 import QtWidgets
from add1_design import Form5
from edit_question_design import Form6
from delete_question_design import Form7



class AddQuestion(QtWidgets.QMainWindow): # окно для выбора типа вопроса
    def __init__(self, test):
        super(AddQuestion, self).__init__()
        self.ui = Form5()
        self.ui.setupUi(self)
        self.current_test = test

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')
        self.current_test.add(str(self.comboBox.currentText()))


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