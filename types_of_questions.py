class QstName:
    def __init__(self):
        self._question = None
        self.rating = 0
        self.user_answer = None

    def userGetAnswer(self):
        self.user_answer = input()[:1000]

    def printQ(self):
        print(str(self._question))

    def add(self):
        self._question = "What is your name?"

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")


class Qst:  # Fabric
    def __init__(self):
        self._question = ''
        self._right_answer = None
        self.rating = 0
        self.user_mark = 0
        self.user_answer = None

    def setRating(self, rating):
        self.rating = rating

    def userGetAnswer(self):
        self.user_answer = input()
        self.userMark()


class QstTrueFalse(Qst):  # клас для виду запитань із двома варіантами відповіді правда/брехня
    def __init__(self):
        super(Qst, self).__init__()
        self._answerOptions = ["True", "False"]

    def userMark(self):
        if str(self.user_answer).lower() == str(self._right_answer).lower():
            self.user_mark = self.rating

    def printQ(self):
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        print(str(self._question) + '\n' + options)

    def add(self):
        print('Input question')
        self._question = input()
        print('Input the right answer (True or False)')
        self._right_answer = input()
        print('Input question valuation')
        self.rating = input()

    def writeTestFile(self, the_file):
        the_file.write('QstTrueFalse\n')
        the_file.write(str(self._question) + "\n")
        the_file.write(str(self._right_answer) + "\n" + str(float(self.rating)) + "\n\n")

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self._right_answer = file.readline().strip("\n")
        self.rating = float(file.readline().strip("\n"))


class QstEnterText(Qst):  # клас для виду запитань із введенням текстової відповідді
    def __init__(self):
        super(Qst, self).__init__()

    def userMark(self):
        right_answer = str(self._right_answer).lower().split()
        user_answer = str(self.user_answer).lower()

        if all(keyword in user_answer for keyword in right_answer):
            self.user_mark = self.rating

    def printQ(self):
        print(str(self._question))

    def add(self):
        print('Input question')
        self._question = input()
        print('Input the right answer')
        self._right_answer = input()
        print('Input question valuation')
        self.rating = input()

    def writeTestFile(self, the_file):
        the_file.write('QstEnterText\n')
        the_file.write(str(self._question) + "\n" + str(self._right_answer) + "\n" + str(self.rating) + "\n\n")

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self._right_answer = file.readline().strip("\n")
        self.rating = float(file.readline().strip("\n"))


class QstOneAnswer(Qst):  # запитання з вибором однієї правильної відповіді
    def __init__(self):
        super(Qst, self).__init__()
        self._answerOptions = []
        self._rightAnswerIndex = None

    def enterOption(self, option):
        self._answerOptions.append(option)

    def add(self):
        print('Input question')
        self._question = input()
        print('Input number of options')
        numOptions = int(input())
        self._answerOptions = [] * numOptions
        for i in range(numOptions):
            print('Input option ' + str(i + 1) + ' : ')
            option = input()
            self.enterOption(option)
        print('Input index of right answer')
        self._rightAnswerIndex = int(input())
        print('Input question valuation')
        self.setRating(input())

    def userMark(self):
        mark = 0
        if self.user_answer == self._answerOptions[self._rightAnswerIndex - 1]:
            mark = self.rating
        self.user_mark = mark

    def writeTestFile(self, file):
        file.write('QstOneAnswer\n')
        file.write(self._question + '\n')
        file.write(str(len(self._answerOptions)) + '\n')
        for i in self._answerOptions:
            file.write(i + '\n')
        file.write(str(self._rightAnswerIndex) + '\n')
        file.write(str(self.rating) + '\n\n')

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        numOptions = int(file.readline().strip("\n"))
        self._answerOptions = [None] * numOptions
        for i in range(numOptions):
            self._answerOptions[i] = file.readline().strip("\n")
        self._rightAnswerIndex = int(file.readline().strip("\n"))
        self.rating = float(file.readline().strip("\n"))

    def printQ(self):
        options = ''
        for i in self._answerOptions:
            options += i + '\n'
        print(str(self._question) + '\n' + options)


class QstSomeAnswer(QstOneAnswer):  # запитання з вибором декількох правильних відповідей, наслідує клас з одним правильним
    def __init__(self):
        super().__init__()
        self._rightAnswerIndexArr = []

    def add(self):
        print('Input question')
        self._question = input()
        print('Input number of options')
        numOptions = int(input())
        self._answerOptions = [] * numOptions
        for i in range(numOptions):
            print('Input option ' + str(i + 1) + ' : ')
            option = input()
            self.enterOption(option)
        print('Input number of right options')
        numRight = int(input())
        for i in range(numRight):
            print('Input index of right answer ' + str(i + 1) + ' : ')
            right = input()
            self._rightAnswerIndexArr.append(int(right))
        print('Input question valuation')
        self.setRating(input())

    def userMark(self):
        mark = 0
        markForPoint = int(self.rating) / len(self._rightAnswerIndexArr)
        for i in range(len(self.user_answer.split(', '))):
            for j in range(len(self._rightAnswerIndexArr)):
                if (self.user_answer.split(', '))[i] == self._answerOptions[int(self._rightAnswerIndexArr[j]) - 1]:
                    mark += markForPoint
                    break
        self.user_mark = mark

    def writeTestFile(self, file):
        file.write('QstSomeAnswer\n')
        file.write(str(self._question) + '\n')
        file.write(str(len(self._answerOptions)) + '\n')
        for i in range(len(self._answerOptions)):
            file.write(self._answerOptions[i] + '\n')

        file.write(str(len(self._rightAnswerIndexArr)) + '\n')

        for i in self._rightAnswerIndexArr:
            file.write(str(i) + ' ')
        file.write('\n' + str(self.rating) + '\n\n')

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        numOptions = int(file.readline().strip("\n"))
        self._answerOptions = [None] * numOptions
        for i in range(numOptions):
            self._answerOptions[i] = file.readline().strip("\n")
        numRight = int(file.readline().strip("\n"))
        self._rightAnswerIndexArr = [None] * numRight
        rights = file.readline().strip("\n").split(' ')
        for i in range(numRight):
            self._rightAnswerIndexArr[i] = rights[i]
        self.rating = float(file.readline().strip("\n"))


class QstTable(Qst):  # запитання з кількома варіантами відповіді в таблиці
    def __init__(self):
        self.num_answers = 0
        self.num_questions = 0
        self.text_answers = None
        self.text_questions = None
        self._right_answers = []
        self.user_answers = []

    def getTextAnswers(self):
        for i in range(0, self.num_answers):
            print('Option ' + str(i + 1) + ':\n')
            self.text_answers.append(input())

    def getTextQuestions(self):
        for i in range(self.num_questions):
            print('Question ' + str(i + 1) + ':\n')
            self.text_questions.append(str(input()))

    def setRightAnswer(self):
        for i in range(self.num_questions):
            ans = []
            ans.append(input())
            self._right_answers.append(ans)

    def userGetAnswer(self):
        self.user_answers = []
        for i in range(self.num_questions):
            print('Input your answers for ' + str(i + 1) + ' question')
            self.user_answers.append(input())
        self.userMark()

    def userMark(self):
        for i in range(len(self._right_answers)):
            one_right_ans = self._right_answers[i]
            one_user_ans = self.user_answers[i]
            for j in range(len(one_right_ans)):
                for k in range(len(one_user_ans)):
                    if one_right_ans[j] == one_user_ans[k]:
                        self.user_mark += self.rating / self.num_questions / len(one_right_ans)
                        break

    def printQ(self):
        print(self._question + '\n')
        print('Questions')
        for i in range(self.num_questions):
            print(str(i + 1) + '. ' + self.text_questions[i] + '\n')
        print('Options')
        for i in range(self.num_answers):
            print(str(i + 1) + '. ' + self.text_answers[i] + '\n')
        print('Input every answer in one line through (, )')

    def add(self):
        print('Input main question')
        self._question = input()
        print('Input number of questions')
        self.num_questions = int(input())
        self.text_questions = [] * self.num_questions
        print('Input number of options')
        self.num_answers = int(input())
        self.text_answers = [] * self.num_answers
        print('Input local questions')
        self.getTextQuestions()
        print('Input options')
        self.getTextAnswers()

        print('Input indexes of right answer for each local questions through (, )')
        self.setRightAnswer()
        print('Input question valuation')
        rating = float(input())
        self.setRating(rating)

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self.num_questions = int(file.readline().strip("\n"))
        self.text_questions = [None] * self.num_questions
        for i in range(self.num_questions):
            self.text_questions[i] = file.readline().strip("\n")

        self.num_answers = int(file.readline().strip("\n"))
        self.text_answers = [None] * self.num_answers
        for i in range(self.num_answers):
            self.text_answers[i] = file.readline().strip("\n")

        self._right_answers = [None] * self.num_questions
        for i in range(self.num_questions):
            self._right_answers[i] = file.readline().strip("\n")
        self.rating = float(file.readline().strip("\n"))

    def writeTestFile(self, file):
        file.write('QstTable\n')
        file.write(self._question + '\n')
        file.write(str(self.num_questions) + '\n')
        for i in range(self.num_questions):
            file.write(self.text_questions[i] + '\n')

        file.write(str(self.num_answers) + '\n')
        for i in range(self.num_answers):
            file.write(self.text_answers[i] + '\n')
        for i in range(self.num_questions):
            file.write(str(self._right_answers[i]) + '\n')
        file.write(str(self.rating) + '\n\n')


class QstScale(Qst):  # запитання з відповіддю числом (передбачало шкалу з повзунком)
    def __init__(self):
        super(Qst, self).__init__()
        # self.start = 0
        # self.end = 100

    def userMark(self):
        if float(self.user_answer) == self._right_answer:
            self.user_mark = self.rating

    def printQ(self):
        print(str(self._question), end='\n')

    def writeTestFile(self, the_file):
        the_file.write('QstScale\n')
        the_file.write(str(self._question) + "\n")
        the_file.write(str(self._right_answer) + "\n" + str(self.rating) + "\n\n")

    def add(self):
        print('Input question', end='\n')
        self._question = input()
        print('Input the right answer', end='\n')
        self._right_answer = float(input())
        print('Input question valuation', end='\n')
        self.setRating(float(input()))

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self._right_answer = float(file.readline().strip("\n"))
        self.rating = float(file.readline().strip("\n"))


class QstTableOne(Qst):  # встановлення відповідності
    def __init__(self):
        self.num_answers = 0
        self.text_answers = []
        self.text_questions = []

    def getTextAnswers(self):
        for i in range(0, self.num_answers):
            print('Answer ', str(i + 1), ':', end=' ')
            self.text_answers.append(input())

    def getTextQuestions(self):
        for i in range(self.num_answers):
            print('Question ', str(i + 1), ':', end=' ')
            self.text_questions.append(str(input()))

    def setRightAnswer(self):
        self._right_answer = input()

    def userMark(self):
        right_answer = self._right_answer.split()
        answers = self.user_answer.split()
        for i in range(len(right_answer)):
            if answers[i] == right_answer[i]:
                self.user_mark += self.rating / self.num_answers

    def printQ(self):
        print(self._question, end='\n')
        print('Questions')
        for i in range(self.num_answers):
            print(str(i + 1) + '. ' + self.text_questions[i], end='\n')
        print('Answers')
        for i in range(self.num_answers):
            print(str(i + 1) + ') ' + self.text_answers[i], end='\n')
        print('Input your answers')

    def add(self):
        print('Input main question')
        self._question = input()
        print('Input number of options/questions')
        self.num_answers = int(input())

        self.text_answers = [] * self.num_answers
        self.text_questions = [] * self.num_answers

        print('Input local questions')
        self.getTextQuestions()
        print('Input answers')
        self.getTextAnswers()

        print('Input indexes of right answer for each local questions')
        self.setRightAnswer()
        print('Input question valuation')
        self.setRating(float(input()))

    def readTestFile(self, file):
        self._question = file.readline().strip("\n")
        self.num_answers = int(file.readline().strip("\n"))
        self.text_questions = [''] * self.num_answers
        self.text_answers = [''] * self.num_answers
        for i in range(self.num_answers):
            self.text_questions[i] = file.readline().strip("\n")
            self.text_answers[i] = file.readline().strip("\n")
        self._right_answer = file.readline().strip("\n")
        self.rating = float(file.readline().strip("\n"))

    def writeTestFile(self, ftest):
        ftest.write('QstTableOne\n')
        ftest.write(self._question + '\n')
        ftest.write(str(self.num_answers) + '\n')
        for i in range(self.num_answers):
            ftest.write(self.text_questions[i] + '\n')
            ftest.write(self.text_answers[i] + '\n')
        ftest.write(self._right_answer + '\n')
        ftest.write(str(self.rating) + '\n\n')
