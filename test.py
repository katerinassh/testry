import types_of_questions
import os


class Test:   # клас менеджер-тест, взаємодія і з адміністратором, і зі звичайним користувачем
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.questions = []
        self.qamount = 0
        self.total_mark = 0
        self.mark = 0
        self.ftest = None
        self.add('QstName')

    def workTestFile(self):  # метод створює файл, у який записуються питання тесту
        ftest = open('{}.txt'.format(self.title), "w")
        ftest.write(self.title + "\n")
        ftest.write(self.description + "\n\n")
        ftest.close()
        ftest = open('{}.txt'.format(self.title), "a")
        for i in range(1, len(self.questions)):
            self.questions[i].writeTestFile(ftest)
        ftest.close()

    def createAnswerFile(self):  # метод створює файл, у який будуть записуватись відповіді респондентів
        fanswers = open('{}_answers.txt'.format(self.title), "w")
        fanswers.write(self.title + "\n\n")
        fanswers.close()

    def workAnswerFile(self):  # метод записує усі відповіді певного респондента
        fanswers = open('{}_answers.txt'.format(self.title), "a")
        fanswers.write(str(self.questions[0].user_answer) + "\n")
        i = 1
        while i < (len(self.questions)):
            fanswers.write(str(i) + "\n")
            if hasattr(self.questions[i], 'user_answer'):
                fanswers.write(str(self.questions[i].user_answer) + "\n")
            else:
                fanswers.write(str(self.questions[i].user_answers) + "\n")
            fanswers.write(str(self.questions[i].user_mark) + "\n")
            i += 1
        fanswers.write("\n" + str(self.totalUserMark()) + "\n\n")
        fanswers.close()

    def add(self, type):  # метод додає нове питання у тест
        self.qamount += 1
        if type == 'QstName':
            qst = types_of_questions.QstName()
        if type == 'QstTrueFalse':
            qst = types_of_questions.QstTrueFalse()
        if type == 'QstEnterText':
            qst = types_of_questions.QstEnterText()
        if type == 'QstOneAnswer':
            qst = types_of_questions.QstOneAnswer()
        if type == 'QstSomeAnswer':
            qst = types_of_questions.QstSomeAnswer()
        if type == 'QstTable':
            qst = types_of_questions.QstTable()
        if type == 'QstScale':
            qst = types_of_questions.QstScale()
        if type == 'QstTableOne':
            qst = types_of_questions.QstTableOne()
        qst.add()
        self.questions.append(qst)

    def remove(self, number):  # метод видаляє певне питання з тесту
        self.questions.pop(number - 1)
        self.qamount -= 1
        self.workTestFile()

    def rewrite(self, number):  # метод переписує певне питання
        self.remove(number)
        print('Input type of new question')
        type = input()
        if type == 'QstTrueFalse':
            qst = types_of_questions.QstTrueFalse()
        if type == 'QstEnterText':
            qst = types_of_questions.QstEnterText()
        if type == 'QstOneAnswer':
            qst = types_of_questions.QstOneAnswer()
        if type == 'QstSomeAnswer':
            qst = types_of_questions.QstSomeAnswer()
        if type == 'QstTable':
            qst = types_of_questions.QstTable()
        if type == 'QstScale':
            qst = types_of_questions.QstScale()
        if type == 'QstTableOne':
            qst = types_of_questions.QstTableOne()
        qst.add()
        self.questions.insert(number - 1, qst)
        self.workTestFile()

    def totalUserMark(self):  # метод рахує бал користувача за всі питання разом
        self.mark = 0
        for i in range(1, len(self.questions)):
            self.mark += float(self.questions[i].user_mark)
        return self.mark

    def totalTestMark(self):  # метод рахує повний бал тесту
        self.total_mark = 0
        for i in range(1, len(self.questions)):
            self.total_mark += float(self.questions[i].rating)
        return self.total_mark

    def passingTest(self):  # метод відображає кожне питання для проходження, зберігає відповідь користувача
        print(self.title)
        print(self.description + '\n')
        for i in range(len(self.questions)):
            self.questions[i].user_mark = 0
            self.questions[i].printQ()
            self.questions[i].userGetAnswer()
        print('Congratulation!\n' + 'Your mark ' + str(round(self.totalUserMark(), 3)) + "/" + str(self.totalTestMark()))
        self.workAnswerFile()

    def readFromFile(self, file):
        while not file.tell() == os.fstat(file.fileno()).st_size:
            type = file.readline().strip('\n')
            if type == 'QstName':
                qst = types_of_questions.QstName()
            if type == 'QstTrueFalse':
                qst = types_of_questions.QstTrueFalse()
            if type == 'QstEnterText':
                qst = types_of_questions.QstEnterText()
            if type == 'QstOneAnswer':
                qst = types_of_questions.QstOneAnswer()
            if type == 'QstSomeAnswer':
                qst = types_of_questions.QstSomeAnswer()
            if type == 'QstTable':
                qst = types_of_questions.QstTable()
            if type == 'QstScale':
                qst = types_of_questions.QstScale()
            if type == 'QstTableOne':
                qst = types_of_questions.QstTableOne()
            qst.readTestFile(file)
            _ = file.readline()
            self.questions.append(qst)
