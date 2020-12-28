from PyQt5 import QtCore, QtGui, QtWidgets


class Form_AddQstScale(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 413)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 620, 420))
        self.frame.setStyleSheet("background-color: rgb(246, 247, 250);\n"
"color: rgb(110, 55, 238);\n"
"font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(139, 140, 166);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 191, 41))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(480, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.07, y1:0.227364, x2:0.895, y2:0.847, stop:0 rgba(110, 55, 238, 255), stop:0.487562 rgba(138, 110, 215, 255), stop:1 rgba(147, 134, 190, 255));\n"
"border-radius: 18px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 501, 31))
        self.label_3.setStyleSheet("color: rgba(110, 55, 238, 255)")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 521, 41))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 181, 41))
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 110, 441, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dlg 2\"; ")
        self.lineEdit.setObjectName("lineEdit")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(280, 210, 70, 30))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dlg 2\"; ")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(30, 260, 560, 20))
        self.horizontalScrollBar.setStyleSheet("background-color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dlg 2\"; ")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 310, 61, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dlg 2\"; ")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Enter the question:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Adding a question with text answer</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter the right answer (words that need to be included):</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Enter the valuation:</span></p></body></html>"))
        self.lineEdit.setText(_translate("Form", "question"))
        self.lineEdit_2.setText(_translate("Form", "0"))