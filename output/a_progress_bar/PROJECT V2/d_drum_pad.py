from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer
import c_main_interface
import d_drum_pad
from PyQt5.QtWidgets import QMessageBox
import g_style_changer

class Ui_Form_drum(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(709, 815)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 691, 801))
        self.frame.setStyleSheet(g_style_changer.font_color)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 671, 781))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet(g_style_changer.background_color)
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 151, 141))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color: white;\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(165, 0, 255, 255), stop:1 rgba(209, 0, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 170, 151, 141))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 216, 0, 255), stop:1 rgba(255, 173, 0, 255));\n"
"    color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 216, 0, 255), stop:1 rgba(255, 173, 0, 255));\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 170, 151, 141))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(104, 140, 255, 255), stop:1 rgba(0, 82, 255, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 170, 151, 141))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(138, 255, 118, 255), stop:0.0284091 rgba(163, 255, 147, 255), stop:1 rgba(36, 201, 0, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 620, 151, 141))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color: white;\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(165, 0, 255, 255), stop:1 rgba(209, 0, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 320, 151, 141))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.00568182 rgba(83, 179, 237, 255), stop:1 rgba(0, 217, 227, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 320, 151, 141))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(138, 255, 118, 255), stop:0.0284091 rgba(163, 255, 147, 255), stop:1 rgba(36, 201, 0, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 320, 151, 141))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color: white;\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(165, 0, 255, 255), stop:1 rgba(209, 0, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 320, 151, 141))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(243, 58, 97, 255), stop:1 rgba(200, 59, 130, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 470, 151, 141))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 216, 0, 255), stop:1 rgba(255, 173, 0, 255));\n"
"    color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 216, 0, 255), stop:1 rgba(255, 173, 0, 255));\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setGeometry(QtCore.QRect(180, 470, 151, 141))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(243, 58, 97, 255), stop:1 rgba(200, 59, 130, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setGeometry(QtCore.QRect(500, 470, 151, 141))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 216, 0, 255), stop:1 rgba(255, 173, 0, 255));\n"
"    color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 216, 0, 255), stop:1 rgba(255, 173, 0, 255));\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 620, 151, 141))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(104, 140, 255, 255), stop:1 rgba(0, 82, 255, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_14.setGeometry(QtCore.QRect(340, 470, 151, 141))
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.00568182 rgba(83, 179, 237, 255), stop:1 rgba(0, 217, 227, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget)
        self.pushButton_15.setGeometry(QtCore.QRect(340, 620, 151, 141))
        self.pushButton_15.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(138, 255, 118, 255), stop:0.0284091 rgba(163, 255, 147, 255), stop:1 rgba(36, 201, 0, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget)
        self.pushButton_16.setGeometry(QtCore.QRect(500, 620, 151, 141))
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(104, 140, 255, 255), stop:1 rgba(0, 82, 255, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.widget)
        self.pushButton_17.setGeometry(QtCore.QRect(20, 20, 151, 141))
        self.pushButton_17.setStyleSheet("QPushButton {\n"
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
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget)
        self.pushButton_18.setGeometry(QtCore.QRect(180, 20, 151, 141))
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    font: bold;\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_20 = QtWidgets.QPushButton(self.widget)
        self.pushButton_20.setGeometry(QtCore.QRect(500, 20, 151, 141))
        self.pushButton_20.setStyleSheet("QPushButton {\n"
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
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_19 = QtWidgets.QPushButton(self.widget)
        self.pushButton_19.setGeometry(QtCore.QRect(340, 20, 151, 141))
        self.pushButton_19.setStyleSheet("QPushButton {\n"
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
        self.pushButton_19.setObjectName("pushButton_19")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_17.setText(_translate("Form", "REC"))
        self.pushButton_18.setText(_translate("Form", "STOP"))
        self.pushButton_20.setText(_translate("Form", "ВЫХОД"))
        self.pushButton_19.setText(_translate("Form", "HEAR"))
        self.pushButton_20.clicked.connect(self.exit)

        #17, 18, 19, 20
        self.pushButton.clicked.connect(self.sound1)
        self.pushButton_2.clicked.connect(self.sound2)
        self.pushButton_3.clicked.connect(self.sound3)
        self.pushButton_4.clicked.connect(self.sound4)
        self.pushButton_5.clicked.connect(self.sound14) 
        self.pushButton_6.clicked.connect(self.sound5) 
        self.pushButton_7.clicked.connect(self.sound6) 
        self.pushButton_8.clicked.connect(self.sound7)
        self.pushButton_9.clicked.connect(self.sound8)
        self.pushButton_10.clicked.connect(self.sound9)
        self.pushButton_11.clicked.connect(self.sound10)
        self.pushButton_12.clicked.connect(self.sound12)
        self.pushButton_13.clicked.connect(self.sound13)
        self.pushButton_14.clicked.connect(self.sound11) 
        self.pushButton_15.clicked.connect(self.sound15)
        self.pushButton_16.clicked.connect(self.sound16)
        self.pushButton_17.clicked.connect(self.rec)
        self.pushButton_18.clicked.connect(self.stop)
        self.pushButton_19.clicked.connect(self.hear)


    music_list = []


    def exit(self):
        self.mw_main = c_main_interface.MainWindow_main()
        self.mw_main.show()
        d_drum_pad.MainWindow_drum.hide(self)

    def rec(self):
        print('rec')
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Не работает")
        msgBox.setWindowTitle("ОУ ЧОРТ ОШИБКА")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec_()




    def stop(self):
        print('rec')
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Не осилил")
        msgBox.setWindowTitle("МДА...")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec_()



    def hear(self):
        print('hear')
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Да")
        msgBox.setWindowTitle("Нет")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec_()





    def sound1(self):
        mixer.init()
        mixer.music.load("z_1.mp3")
        mixer.music.play()
        print('1')

    def sound2(self):
        mixer.init()
        mixer.music.load("z_2.mp3")
        mixer.music.play()
        print('2')

    def sound3(self):
        mixer.init()
        mixer.music.load("z_3.mp3")
        mixer.music.play()
        print('3')

    def sound4(self):
        mixer.init()
        mixer.music.load("z_4.mp3")
        mixer.music.play()
        print('4')

    def sound5(self):
        mixer.init()
        mixer.music.load("z_5.mp3")
        mixer.music.play()
        print('5')

    def sound6(self):
        mixer.init()
        mixer.music.load("z_6.mp3")
        mixer.music.play()
        print('6')

    def sound7(self):
        mixer.init()
        mixer.music.load("z_7.mp3")
        mixer.music.play()
        print('7')

    def sound8(self):
        mixer.init()
        mixer.music.load("z_8.mp3")
        mixer.music.play()
        print('8')

    def sound9(self):
        mixer.init()
        mixer.music.load("z_9.mp3")
        mixer.music.play()
        print('9')

    def sound10(self):
        mixer.init()
        mixer.music.load("z_10.mp3")
        mixer.music.play()
        print('10')

    def sound11(self):
        mixer.init()
        mixer.music.load("z_11.mp3")
        mixer.music.play()
        print('11')

    def sound12(self):
        mixer.init()
        mixer.music.load("z_12.mp3")
        mixer.music.play()
        print('12')

    def sound13(self):
        mixer.init()
        mixer.music.load("z_13.mp3")
        mixer.music.play()
        print('13')

    def sound14(self):
        mixer.init()
        mixer.music.load("z_14.mp3")
        mixer.music.play()
        print('14')

    def sound15(self):
        mixer.init()
        mixer.music.load("z_15.mp3")
        mixer.music.play()
        print('15')

    def sound16(self):
        mixer.init()
        mixer.music.load("z_16.mp3")
        mixer.music.play()
        print('16')



class MainWindow_drum(QtWidgets.QMainWindow, Ui_Form_drum):
    def __init__(self):
        super(MainWindow_drum, self).__init__()
        
        self.setupUi(self) 
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw_drum = MainWindow_drum()
    mw_drum.show()
    sys.exit(app.exec())
