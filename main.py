from PyQt5 import QtWidgets
from creator import Ui_MainWindow
import sys


class mainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mainScreen()
application.show()

sys.exit(app.exec())