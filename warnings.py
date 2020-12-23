from PyQt5 import QtWidgets
from warning1_design import Warning1
from warning2_design import Warning2


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