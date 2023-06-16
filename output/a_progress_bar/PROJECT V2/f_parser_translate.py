from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTextEdit
import f_parser_translate
import g_style_changer
import f_pasrer_menu
import googletrans
import textblob
import sys




class Ui_Form(object):
    def setupUi(self, Form):
            
        self.languages = googletrans.LANGUAGES
        self.language_list = list(self.languages.values())
        Form.setObjectName("Form")
        Form.resize(1022, 515)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1021, 501))
        self.frame.setStyleSheet(g_style_changer.font_color)


        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1001, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet(g_style_changer.background_color)


        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 981, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"color: white\n"
"}")


        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(100, 150, 391, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background-color:  rgb(37, 37, 37);\n"
"font: bold;\n"
"color: white;\n"
"padding: 15px 15px;\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}")


        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(510, 150, 391, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"background-color:  rgb(37, 37, 37);\n"
"padding: 15px 15px;\n"
"font: bold;\n"
"color: white;\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}")


        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 981, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"color: white\n"
"}")


        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(680, 120, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("QComboBox{\n"
"border-radius: 0px;\n"
"color:  white;\n"
"background-color:  rgb(149, 149, 149)\n"
"}")


        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setGeometry(QtCore.QRect(270, 120, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("QComboBox{\n"
"border-radius: 0px;\n"
"color:  white;\n"
"background-color:  rgb(149, 149, 149)\n"
"}")


        self.comboBox_4.setObjectName("comboBox_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(100, 120, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"background-color:  rgb(149, 149, 149);\n"
"border-radius: px;\n"
"color:  white\n"
"}")


        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.translator_12 = QtWidgets.QPushButton(self.widget)
        self.translator_12.setGeometry(QtCore.QRect(310, 400, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.translator_12.setFont(font)
        self.translator_12.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  18px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")


        self.translator_12.setObjectName("translator_12")
        self.translator_14 = QtWidgets.QPushButton(self.widget)
        self.translator_14.setGeometry(QtCore.QRect(700, 400, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.translator_14.setFont(font)
        self.translator_14.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  18px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")


        self.translator_14.setObjectName("translator_14")
        self.translator_15 = QtWidgets.QPushButton(self.widget)
        self.translator_15.setGeometry(QtCore.QRect(100, 400, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.translator_15.setFont(font)
        self.translator_15.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  18px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")


        self.translator_15.setObjectName("translator_15")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(510, 120, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"background-color:  rgb(149, 149, 149);\n"
"border-radius: px;\n"
"color:  white\n"
"}")


        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "< GOOGLE TRANSLATOR >"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Form", "______________________________________"))
        self.label_5.setText(_translate("Form", "ВЫБЕРИТЕ ЯЗЫК:"))
        self.translator_12.setText(_translate("Form", "перевести"))
        self.translator_14.setText(_translate("Form", "выйти"))
        self.translator_15.setText(_translate("Form", "очистить"))
        self.label_6.setText(_translate("Form", "ВЫБЕРИТЕ ЯЗЫК:"))
        self.translator_14.clicked.connect(self.exit)

    def exit(self):
        
        self.mw = f_pasrer_menu.MainWindow()
        self.mw.show()
        f_parser_translate.MainWindow.hide(self)
        
        

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        


        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        
        self.setupUi(self)



        self.t_button = self.findChild(QPushButton, "translator_12")
        self.c_button = self.findChild(QPushButton, "translator_15")

        self.combo_1 = self.findChild(QComboBox, "comboBox_4")
        self.combo_2 = self.findChild(QComboBox, "comboBox_3")

        self.text_1 = self.findChild(QTextEdit, "textEdit")
        self.text_2 = self.findChild(QTextEdit, "textEdit_3")

        self.t_button.clicked.connect(self.translate)
        self.c_button.clicked.connect(self.clear)

        self.languages = googletrans.LANGUAGES

        self.language_list = list(self.languages.values())

        self.combo_1.addItems(self.language_list)
        self.combo_2.addItems(self.language_list)

        self.combo_1.setCurrentText("russian")
        self.combo_2.setCurrentText("english")


        self.show()

    def clear(self):
        self.textEdit.setText("")

        self.textEdit_3.setText("")

        self.combo_1.setCurrentText("russian")
        self.combo_2.setCurrentText("english")

    def translate(self):
        try:
            for key,value in self.languages.items():
                if (value == self.combo_1.currentText()):
                    from_language_key = key


            for key,value in self.languages.items():
                if (value == self.combo_2.currentText()):
                    to_language_key = key


            words = textblob.TextBlob(self.text_1.toPlainText())
            words = words.translate(from_lang=from_language_key, to=to_language_key)
            self.text_2.setText(str(words))


        except Exception as e:
                print(e)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())