from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from pygame import mixer
import e_game_menu
import e_game_friend
import g_style_changer


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(588, 671)
        self.a = 0
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 571, 651))
        self.frame.setStyleSheet(g_style_changer.font_color)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 551, 631))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet(g_style_changer.background_color)
        self.widget.setObjectName("widget")
        self.btn3 = QtWidgets.QPushButton(self.widget)
        self.btn3.setGeometry(QtCore.QRect(10, 290, 171, 161))
        self.btn3.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.widget)
        self.btn4.setGeometry(QtCore.QRect(190, 290, 171, 161))
        self.btn4.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font-size:  90px;\n"
"    font: bold;"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.widget)
        self.btn5.setGeometry(QtCore.QRect(370, 290, 171, 161))
        self.btn5.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn5.setObjectName("btn5")
        self.btn1 = QtWidgets.QPushButton(self.widget)
        self.btn1.setGeometry(QtCore.QRect(190, 120, 171, 161))
        self.btn1.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.widget)
        self.btn2.setGeometry(QtCore.QRect(370, 120, 171, 161))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn2.setObjectName("btn2")
        self.btn6 = QtWidgets.QPushButton(self.widget)
        self.btn6.setGeometry(QtCore.QRect(10, 460, 171, 161))
        self.btn6.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"   color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.widget)
        self.btn7.setGeometry(QtCore.QRect(190, 460, 171, 161))
        self.btn7.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.widget)
        self.btn8.setGeometry(QtCore.QRect(370, 460, 171, 161))
        self.btn8.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn8.setObjectName("btn8")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 71))
        self.label.setStyleSheet("QLabel {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  30px;\n"
"}\n"
"")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_exit = QtWidgets.QPushButton(self.widget)
        self.pushButton_exit.setGeometry(QtCore.QRect(370, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_line = QtWidgets.QLabel(self.widget)
        self.label_line.setGeometry(QtCore.QRect(10, 90, 531, 20))
        self.label_line.setStyleSheet(g_style_changer.font_color)
        self.label_line.setText("")
        self.label_line.setAlignment(QtCore.Qt.AlignCenter)
        self.label_line.setObjectName("label_line")
        self.pushButton_restart = QtWidgets.QPushButton(self.widget)
        self.pushButton_restart.setGeometry(QtCore.QRect(190, 10, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_restart.setFont(font)
        self.pushButton_restart.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.btn = QtWidgets.QPushButton(self.frame)
        self.btn.setGeometry(QtCore.QRect(20, 130, 171, 161))
        self.btn.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn3.setText(_translate("Form", ""))
        self.btn4.setText(_translate("Form", ""))
        self.btn5.setText(_translate("Form", ""))
        self.btn1.setText(_translate("Form", ""))
        self.btn2.setText(_translate("Form", ""))
        self.btn6.setText(_translate("Form", ""))
        self.btn7.setText(_translate("Form", ""))
        self.btn8.setText(_translate("Form", ""))
        self.pushButton_exit.setText(_translate("Form", "ВЫЙТИ"))
        self.pushButton_restart.setText(_translate("Form", "РЕСТАРТ"))
        self.btn.setText(_translate("Form", ""))

        self.pushButton_exit.clicked.connect(self.exit_game)
        self.pushButton_restart.clicked.connect(self.restart)

    def exit_game(self):
                self.mw_main = e_game_menu.MainWindow()
                self.mw_main.show()
                e_game_friend.MainWindow_game.hide(self)

    def restart(self):
        ...

class MainWindow_game(QtWidgets.QMainWindow, Ui_Form):
        def __init__(self):
                super(MainWindow_game, self).__init__()

                self.x_wins = 0
                self.o_wins = 0


                self.setupUi(self)
                self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
                self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

                self.counter = 0

                self.button1 = self.findChild(QPushButton, "btn")
                self.button2 = self.findChild(QPushButton, "btn3")
                self.button3 = self.findChild(QPushButton, "btn6")
                self.button4 = self.findChild(QPushButton, "btn1")
                self.button5 = self.findChild(QPushButton, "btn4")
                self.button6 = self.findChild(QPushButton, "btn7")
                self.button7 = self.findChild(QPushButton, "btn2")
                self.button8 = self.findChild(QPushButton, "btn5")
                self.button9 = self.findChild(QPushButton, "btn8")

                self.button10 = self.findChild(QPushButton, "pushButton_restart")

                self.label.setText("X - Ход")

                self.button1.clicked.connect(lambda: self.clicker(self.button1))
                self.button2.clicked.connect(lambda: self.clicker(self.button2))
                self.button3.clicked.connect(lambda: self.clicker(self.button3))
                self.button4.clicked.connect(lambda: self.clicker(self.button4))
                self.button5.clicked.connect(lambda: self.clicker(self.button5))
                self.button6.clicked.connect(lambda: self.clicker(self.button6))
                self.button7.clicked.connect(lambda: self.clicker(self.button7))
                self.button8.clicked.connect(lambda: self.clicker(self.button8))
                self.button9.clicked.connect(lambda: self.clicker(self.button9))

                self.pushButton_restart.clicked.connect(self.reset)
                

                self.show()

        def checkWin(self):
                
                if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
                        self.win(self.button1, self.button4, self.button7)

                if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
                        self.win(self.button2, self.button5, self.button8)

                if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
                        self.win(self.button3, self.button6, self.button9)

                if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
                        self.win(self.button1, self.button2, self.button3)

                if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
                        self.win(self.button4, self.button5, self.button6)

                if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
                        self.win(self.button7, self.button8, self.button9)

                if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
                        self.win(self.button1, self.button5, self.button9)

                if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
                        self.win(self.button3, self.button5, self.button7)

                        


        def win(self, a, b, c):
                a.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   red;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
                b.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   red;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")


                c.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   red;\n"
"    font: bold;"
"    font-size:  90px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")


                self.label.setStyleSheet("QLabel {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  red;\n"
"    font: bold;"
"    font-size:  30px;\n"
"}\n"
"")
                
                


                        
                print(self.x_wins, self.o_wins)
                
                
                
                
                mixer.init()
                mixer.music.load("z_2.mp3")
                mixer.music.play()
                self.label.setText(f"!!! {a.text()} !!!")
                

                
                self.disable()

        def disable(self):
                button_list = [
                self.button1,
                self.button2,
                self.button3,
                self.button4,
                self.button5,
                self.button6,
                self.button7,
                self.button8,
                self.button9,]

                for b in button_list:
                        b.setEnabled(False)
    
        print('10')

        def clicker(self, b):
                if self.counter % 2 == 0:
                        mark = "×"
                        self.label.setText("O - Ход")
                else:
                        mark = "⭘"
                        self.label.setText("X - Ход")

                b.setText(mark)
                b.setEnabled(False)

                self.counter += 1
                self.checkWin()

        def reset(self):

                button_list = [
                self.button1,
                self.button2,
                self.button3,
                self.button4,
                self.button5,
                self.button6,
                self.button7,
                self.button8,
                self.button9,]

                for b in button_list:
                        b.setText("")
                        b.setEnabled(True)


                        b.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font-size:  90px;\n"
"    font: bold;"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")


                self.label.setStyleSheet("QLabel {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:   white;\n"
"    font-size:  30px;\n"
"    font: bold;"
"}"
"")
                self.label.setText("X - Ход")


                self.counter = 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw_game = MainWindow_game()
    mw_game.show()
    sys.exit(app.exec())