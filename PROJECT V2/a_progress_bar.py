from PyQt5 import QtCore, QtGui, QtWidgets
import time
import random
import sys
import b_password
import a_progress_bar
import x_stylesheet_font


class Ui_Form_progress_bar(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 278)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(50, 20, 441, 221))
        self.frame.setStyleSheet(x_stylesheet_font.stylesheet_purple)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(20, 70, 381, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(124, 113, 116);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.00568182 rgba(147, 48, 255, 255), stop:1 rgba(155, 0, 173, 255))\n"
"}")    

        n = 250
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(n)
        self.progressBar.setRange(0, n)



        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"color: white;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 140, 231, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  29px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.pushButton.setObjectName("pushButton")
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
        self.widget.setGeometry(QtCore.QRect(10, 10, 421, 201))
        self.widget.setStyleSheet("QWidget {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.00568182 rgba(59, 59, 59, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.progressBar.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton.clicked.connect(lambda status, n_size=n: self.run(n_size))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PROGRESS BAR"))
        self.pushButton.setText(_translate("Form", "ЗАПУСТИТЬ"))

    def run(self, n):
        for i in range(n):
            time.sleep(0.01)
            self.fake_data = ['Loading resuorces', 'Authentication in progress', 'Key verification', 'Creating an active session', 'Loading your account', 'Connecting...', 'Rendering main menu']
            self.label_2.setText(random.choice(self.fake_data))
            if i == 249:
                self.label_2.setText('Finished')
                self.mw_password = b_password.MainWindow_password()
                self.mw_password.show()
                a_progress_bar.MainWindow_progress_bar.hide(self)
                
            self.progressBar.setValue(i+1)


class MainWindow_progress_bar(QtWidgets.QMainWindow, Ui_Form_progress_bar):
    def __init__(self):
        super(MainWindow_progress_bar, self).__init__()
        
        self.setupUi(self) 
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__ == "__main__":      
     import sys
     app = QtWidgets.QApplication(sys.argv)
     mw_progress_bar = MainWindow_progress_bar()
     mw_progress_bar.show()
     sys.exit(app.exec())
