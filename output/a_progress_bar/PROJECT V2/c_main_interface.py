from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import d_drum_pad
import c_main_interface
import e_game_menu

import f_pasrer_menu
import h_info_main

import g_style_changer

class Ui_Form_main(object):
    def setupUi(self, Form):

        
        Form.setObjectName("Form")
        Form.resize(951, 576)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 921, 551))
        
        self.frame.setStyleSheet(g_style_changer.font_color)
        
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"color: white;\n"
"}")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 901, 531))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet(g_style_changer.background_color)
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 391, 141))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font: bold;\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 30, 391, 141))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font: bold;"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 190, 391, 141))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font: bold;"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 190, 391, 141))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font: bold;"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 350, 391, 141))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font: bold;"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 350, 391, 141))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font: bold;"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.pushButton.setText(_translate("Form", "ДРУМПАД")) #1
        self.pushButton.clicked.connect(self.btn1)

        self.pushButton_2.setText(_translate("Form", "ВЫХОД")) #4
        self.pushButton_2.clicked.connect(self.btn4)

        self.pushButton_3.setText(_translate("Form", "ПОЛЕЗНОЕ")) #2
        self.pushButton_3.clicked.connect(self.btn2)

        self.pushButton_4.setText(_translate("Form", "ТЕМА")) #5
        self.pushButton_4.clicked.connect(self.btn5)

        self.pushButton_5.setText(_translate("Form", "ИГРА")) #3
        self.pushButton_5.clicked.connect(self.btn3)

        self.pushButton_6.setText(_translate("Form", "КОНТАКТЫ")) #6
        self.pushButton_6.clicked.connect(self.btn6)

    def btn4(self):
        sys.exit()



    def btn1(self):
        self.mw_drum = d_drum_pad.MainWindow_drum()
        self.mw_drum.show()
        c_main_interface.MainWindow_main.hide(self)



    def btn2(self):
        self.mw = f_pasrer_menu.MainWindow()
        self.mw.show()
        c_main_interface.MainWindow_main.hide(self)



    def btn3(self):
        self.mw_game = e_game_menu.MainWindow()
        self.mw_game.show()
        c_main_interface.MainWindow_main.hide(self)


    def btn5(self):
        
        self.mw_game = g_style_changer.MainWindow()
        self.mw_game.show()
        c_main_interface.MainWindow_main.hide(self)


    def btn6(self):
        
        self.mw_game = h_info_main.MainWindow()
        self.mw_game.show()
        c_main_interface.MainWindow_main.hide(self)







class MainWindow_main(QtWidgets.QMainWindow, Ui_Form_main):
    def __init__(self):
        super(MainWindow_main, self).__init__()
        
        self.setupUi(self) 
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw_main = MainWindow_main()
    mw_main.show()
    sys.exit(app.exec())