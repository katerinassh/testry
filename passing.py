from PyQt5 import QtWidgets
import test
import types_of_questions
import sys

from passQstText_design import Form_QstText
from passQstTF_design import Form_QstTF
from passQstOneAnswer_design import Form_QstOneAnswer
from passQstName_design import Form_QstName


class passing:
    def __init__(self, curr_test):
        self.curr = curr_test
        self.w = []

    def curr_question(self):
        i = -1
        for qst in self.curr.questions:
            if isinstance(qst, types_of_questions.QstName):
                self.w.append(w_QstName(qst))
                i += 1
                self.w[i].show()
            elif isinstance(qst, types_of_questions.QstTrueFalse):
                self.w.append(w_QstTF(qst))
                i += 1
                self.w[i].show()
            elif isinstance(qst, types_of_questions.QstEnterText):
                self.w.append(w_QstText(qst))
                i += 1
                self.w[i].show()
            elif isinstance(qst, types_of_questions.QstOneAnswer):
                self.w.append(w_QstOneAnswer(qst))
                i += 1
                self.w[i].show()
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
        #self.curr.workTestfile()


class w_QstName(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstName, self).__init__()
        self.qst = qst
        self.ui = Form_QstName()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.confirm_QstName)

    def confirm_QstName(self):
        self.qst.user_answer = self.ui.lineEdit.text
        self.hide()


class w_QstTF(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstTF, self).__init__()
        self.qst = qst
        self.ui = Form_QstTF()
        self.ui.setupUi(self)
        self.ui.label_5.setText(self.qst.get_question())
        self.ui.pushButton.clicked.connect(self.confirm_QstTF)

    def confirm_QstTF(self):
        if self.ui.radioButton.isChecked():
            self.qst.user_answer = 'True'
        elif self.ui.radioButton_2.isChecked():
            self.qst.user_answer = 'False'
        else:
            self.qst.user_answer = ''
        self.hide()


class w_QstText(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstText, self).__init__()
        self.qst = qst
        self.ui = Form_QstText()
        self.ui.setupUi(self)
        self.ui.label_5.setText(self.qst.get_question())
        self.ui.pushButton.clicked.connect(self.confirm_QstText)

    def confirm_QstText(self):
        self.qst.user_answer = self.ui.lineEdit.text
        self.hide()


class w_QstOneAnswer(QtWidgets.QMainWindow):
    def __init__(self, qst):
        super(w_QstOneAnswer, self).__init__()
        self.ui = Form_QstOneAnswer()
        self.ui.setupUi(self)
        self.qst = qst
        self.ui.radioButton_1.setChecked(True)

        self.ui.radioButton_1.setText(self.qst.get_options()[0])
        if self.qst.numOptions <= 1:
            self.ui.radioButton_2.setCheckable(False)
            self.ui.radioButton_3.setCheckable(False)
            self.ui.radioButton_4.setCheckable(False)
            self.ui.radioButton_5.setCheckable(False)
        elif self.qst.numOptions <= 2:
            self.ui.radioButton_2.setText(self.qst.get_options()[1])
            self.ui.radioButton_3.setCheckable(False)
            self.ui.radioButton_4.setCheckable(False)
            self.ui.radioButton_5.setCheckable(False)
        elif self.qst.numOptions <= 3:
            self.ui.radioButton_2.setText(self.qst.get_options()[1])
            self.ui.radioButton_3.setText(self.qst.get_options()[2])
            self.ui.radioButton_4.setCheckable(False)
            self.ui.radioButton_5.setCheckable(False)
        elif self.qst.numOptions <= 4:
            self.ui.radioButton_2.setText(self.qst.get_options()[1])
            self.ui.radioButton_3.setText(self.qst.get_options()[2])
            self.ui.radioButton_4.setText(self.qst.get_options()[3])
            self.ui.radioButton_5.setCheckable(False)
        elif self.qst.numOptions <= 5:
            self.ui.radioButton_2.setText(self.qst.get_options()[1])
            self.ui.radioButton_3.setText(self.qst.get_options()[2])
            self.ui.radioButton_4.setText(self.qst.get_options()[3])
            self.ui.radioButton_5.setText(self.qst.get_options()[4])

        self.ui.label_5.setText(str(self.qst.get_question()))
        self.ui.pushButton.clicked.connect(self.confirm_QstOneAnswer)

    def confirm_QstOneAnswer(self):
        self.qst.user_answer = ''
        if self.ui.radioButton_1.isChecked():
            self.qst.user_answer = '0'
        elif self.ui.radioButton_2.isChecked():
            self.qst.user_answer = '1'
        elif self.ui.radioButton_3.isChecked():
            self.qst.user_answer = '2'
        elif self.ui.radioButton_4.isChecked():
            self.qst.user_answer = '3'
        elif self.ui.radioButton_5.isChecked():
            self.qst.user_answer = '4'

        self.hide()


app = QtWidgets.QApplication(sys.argv)

qst0 = types_of_questions.QstName()

qst1 = types_of_questions.QstTrueFalse()
qst1.setRating(1)
qst1.set_question('TF')
qst1.set_right('True')

qst2 = types_of_questions.QstEnterText()
qst2.setRating(100)
qst2.set_question('Texting')
qst2.set_right('text')

qst3 = types_of_questions.QstOneAnswer()
qst3.add()

qsts = [qst0, qst1, qst2, qst3]
Test = test.Test('Testing', 'info')
Test.questions = qsts

passing1 = passing(Test)
passing1.curr_question()

sys.exit(app.exec_())
