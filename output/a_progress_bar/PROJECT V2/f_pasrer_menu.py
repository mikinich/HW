from PyQt5 import QtCore, QtGui, QtWidgets
import f_pasrer_menu
import c_main_interface
from PyQt5.QtWidgets import QMessageBox
import g_style_changer

import f_parser_translate
import f_parser_valute
import f_parser_chatGPT


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 562)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 481, 521))
        self.frame.setStyleSheet(g_style_changer.font_color)

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 461, 501))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet(g_style_changer.background_color)

        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 20, 461, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    border-radius: 100px;\n"
"    color: white;\n"
"    background-color: none;\n"
"}")

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_bot = QtWidgets.QPushButton(self.widget)
        self.pushButton_bot.setGeometry(QtCore.QRect(90, 220, 281, 71))
        self.pushButton_bot.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_bot.setObjectName("pushButton_bot")
        self.pushButton_friend = QtWidgets.QPushButton(self.widget)
        self.pushButton_friend.setGeometry(QtCore.QRect(90, 300, 281, 71))
        self.pushButton_friend.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_friend.setObjectName("pushButton_friend")
        self.pushButton_state = QtWidgets.QPushButton(self.widget)
        self.pushButton_state.setGeometry(QtCore.QRect(90, 140, 281, 71))
        self.pushButton_state.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_state.setObjectName("pushButton_state")
        self.pushButton_exit = QtWidgets.QPushButton(self.widget)
        self.pushButton_exit.setGeometry(QtCore.QRect(90, 380, 281, 71))
        self.pushButton_exit.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_exit.setObjectName("pushButton_exit")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(170, 120, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(280, 120, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(60, 120, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "MENU"))
        self.pushButton_bot.setText(_translate("Form", "ВАЛЮТЫ"))
        self.pushButton_friend.setText(_translate("Form", "НЕЙРОСЕТЬ"))
        self.pushButton_state.setText(_translate("Form", "ПЕРЕВОДЧИК"))
        self.pushButton_exit.setText(_translate("Form", "ВЫЙТИ"))

        self.pushButton_bot.clicked.connect(self.valute)
        self.pushButton_friend.clicked.connect(self.neiro)
        self.pushButton_state.clicked.connect(self.translate)
        self.pushButton_exit.clicked.connect(self.exit)



    def valute(self):
        print('valute')
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Хотел как в переводчике выбор валюты через скролл бар красиво сделать, но что-то пошло не так и время кончилось. В следущем проекте мб добавлю, если не придумаю ничего лучше :)")
        msgBox.setWindowTitle("EROR 0xLOL")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec_()


    def neiro(self):
        self.mw = f_parser_chatGPT.MainWindow()
        self.mw.show()
        f_pasrer_menu.MainWindow.hide(self)


    def translate(self):
        self.mw = f_parser_translate.MainWindow()
        self.mw.show()
        f_pasrer_menu.MainWindow.hide(self)
        




    def exit(self):
        self.mw = c_main_interface.MainWindow_main()
        self.mw.show()
        f_pasrer_menu.MainWindow.hide(self)





class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self) 
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())