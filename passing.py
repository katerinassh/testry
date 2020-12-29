from PyQt5 import QtWidgets
import test
import types_of_questions

from passQstText_design import Form_QstText
from passQstTF_design import Form_QstTF
from passQstOneAnswer_design import Form_QstOneAnswer
from passQstName_design import Form_QstName


class passing:
    def __init__(self, curr_test):
        self.curr = curr_test
        self.w = None

    def curr_question(self):
        for qst in self.curr.questions:
            if isinstance(qst, types_of_questions.QstName):
                self.w = w_QstName(qst)
                self.w.confirm_QstName()
            elif isinstance(qst, types_of_questions.QstTrueFalse):
                self.w = w_QstTF(qst)
                self.w.confirm_QstTF()
            elif isinstance(qst, types_of_questions.QstEnterText):
                self.w = w_QstText(qst)
                self.w.confirm_QstText()
            elif isinstance(qst, types_of_questions.QstOneAnswer):
                self.w = w_QstOneAnswer(qst)
                self.w.confirm_QstOneAnswer()
            # elif isinstance(qst, types_of_questions.QstSomeAnswer):
                # self.w = w_QstSomeAnswer(qst)
                # self.w.confirm_QstSomeAnswer()
            # elif isinstance(qst, types_of_questions.QstScale):
                # self.w = w_QstScale(qst)
                # self.w.confirm_QstScale()
            # elif isinstance(qst, types_of_questions.QstTableOne):
                # self.w = w_QstTableOne(qst)
                # self.w.confirm_QstTableOne()
            # elif isinstance(qst, types_of_questions.QstTable):
                # self.w = w_QstTable(qst)
                # self.w.confirm_QstTable()
        self.curr.workTestfile()


class w_QstName(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstName, self).__init__()
        self.qst = qst
        self.ui = Form_QstTF()
        self.ui.setupUi(self)
        label_qst = self.ui.findChild(QtWidgets.QLabel, 'label_5')
        label_qst.text = self.qst.get_question()
        self.ui.findChild(QtWidgets.QPushButton, 'pushButton').connect(self.confirm_QstName())
        self.ui.show()

    def confirm_QstName(self):
        line_edit = self.ui.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst.user_answer = line_edit.text()
        self.ui.hide()


class w_QstTF(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstTF, self).__init__()
        self.qst = qst
        self.ui = Form_QstTF()
        self.ui.setupUi(self)
        self.ui.findChild(QtWidgets.QPushButton, 'pushButton').connect(self.confirm_QstTF())
        self.ui.show()

    def confirm_QstTF(self):
        radio_button1 = self.ui.findChild(QtWidgets.QRadioButton, 'radioButton')
        radio_button2 = self.ui.findChild(QtWidgets.QRadioButton, 'radioButton_2')
        if radio_button1.isChecked():
            self.qst.user_answer = 'True'
        elif radio_button2.isChecked():
            self.qst.user_answer = 'False'
        else:
            self.qst.user_answer = ''
        self.ui.hide()


class w_QstText(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstText, self).__init__()
        self.qst = qst
        self.ui = Form_QstText()
        self.ui.setupUi(self)
        label_qst = self.ui.findChild(QtWidgets.QLabel, 'label_5')
        label_qst.text = self.qst.get_question()
        self.ui.findChild(QtWidgets.QPushButton, 'pushButton').connect(self.confirm_QstText())
        self.ui.show()

    def confirm_QstText(self):
        line_edit = self.ui.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.qst.user_answer = line_edit.text()
        self.ui.hide()


class w_QstOneAnswer(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstSomeAnswer, self).__init__()
        self.ui = Form_QstOneAnswer()
        self.ui.setupUi(self)
        self.qst = qst
        self.radio_button = []
        for i in range(1, 5):
            self.radio_button.append()
            self.radio_button[i] = self.ui.findChild(QtWidgets.QRadioButton, 'radioButton_{}'.format(str(i)))
            if i<=self.qst.numOptions:
                self.radio_button[i].text = self.qst.get_options(i-1)
            else:
                self.radio_button[i].checkable = False
            if i==1:
                self.radio_button[i].checked = True
        label_qst = self.ui.findChild(QtWidgets.QLabel, 'label_5')
        label_qst.text = self.qst.get_question()
        self.ui.findChild(QtWidgets.QPushButton, 'pushButton').connect(self.confirm_QstOneAnswer())
        self.ui.show()

    def confirm_QstOneAnswer(self):
        self.qst.user_answer = 0
        for i in range(1,self.qst.numOptions):
            if self.radio_button[i].checked():
                self.qst.user_answer = str(i-1)
                break
        self.ui.hide()


qst = types_of_questions.QstTrueFalse()
qst.add()