from PyQt5 import QtCore, QtGui, QtWidgets
import c_main_interface
import b_password
import time


class Ui_Form_password(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(666, 278)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 20, 641, 241))
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0.766, y1:1, x2:0.932, y2:1, stop:0 rgba(76, 20, 106, 255), stop:1 rgba(171, 0, 173, 255))"
"}")
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
"    font: bold;\n"
"color: white;\n"
"}")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 621, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet("QWidget {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.00568182 rgba(59, 59, 59, 255), stop:1 rgba(75, 75, 75, 255))\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 601, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"    font: bold;\n"
"color: white\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 80, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color: none\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(190, 130, 221, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"

"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")    
        self.pushButton.setObjectName("pushButton")
        self.widget.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Введите пароль"))
        self.pushButton.setText(_translate("Form", "Продолжить"))
        self.pushButton.clicked.connect(self.name_clicked)



    def name_clicked(self):
        a  = self.lineEdit.text()
        if a == '2023':
            print('Добро пожаловать!!!')
            self.mw_main = c_main_interface.MainWindow_main()
            self.mw_main.show()
            b_password.MainWindow_password.hide(self)
        elif a == '':
            print('!!! ВЫ НЕ ВВЕЛИ ПАРОЛЬ !!!' * 25)
            self.label.setText('Введите пароль')
        else:
            print('Неверный пароль')
            self.label.setText('Неверный пароль')

class MainWindow_password(QtWidgets.QMainWindow, Ui_Form_password):
    def __init__(self):
        super(MainWindow_password, self).__init__()
        
        self.setupUi(self) 
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw_password = MainWindow_password()
    mw_password.show()
    sys.exit(app.exec())
    