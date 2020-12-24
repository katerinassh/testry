from PyQt5 import QtWidgets
from add1_design import Form5



class AddQuestion(QtWidgets.QMainWindow): # окно для выбора типа вопроса
    def __init__(self, title):
        super(AddQuestion, self).__init__()
        self.ui = Form5()
        self.ui.setupUi(self)
        self.title = title
        self.questions = []
        self.qamount = 0
        self.ftest = None
        self.add('QstName')

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')
        #self.comboBox.currentText()

    def add(self, type):  # метод додає нове питання у тест
        self.qamount += 1
       # if type == 'QstName':
       #     qst = types_of_questions.QstName()
       #if type == 'QstTrueFalse':
        #    qst = types_of_questions.QstTrueFalse()
       # if type == 'QstEnterText':
       #    qst = types_of_questions.QstEnterText()
      #  if type == 'QstOneAnswer':
        #    qst = types_of_questions.QstOneAnswer()
       # if type == 'QstSomeAnswer':
       #    qst = types_of_questions.QstSomeAnswer()
      #  if type == 'QstTable':
        #    qst = types_of_questions.QstTable()
      #  if type == 'QstScale':
       #     qst = types_of_questions.QstScale()
      #  if type == 'QstTableOne':
       #     qst = types_of_questions.QstTableOne()
       # qst.add()
       # self.questions.append(qst)