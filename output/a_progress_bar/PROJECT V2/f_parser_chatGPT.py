from PyQt5 import QtCore, QtGui, QtWidgets
import f_parser_chatGPT
import f_pasrer_menu
import openai
import g_style_changer


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1090, 591)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1071, 571))

        self.frame.setStyleSheet(g_style_changer.font_color)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1051, 551))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet(g_style_changer.background_color)

        self.widget.setObjectName("widget")
        self.search_button = QtWidgets.QPushButton(self.widget)
        self.search_button.setGeometry(QtCore.QRect(980, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  22px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")

        self.search_button.setObjectName("search_button")
        self.otvet_line = QtWidgets.QTextEdit(self.widget)
        self.otvet_line.setGeometry(QtCore.QRect(10, 180, 1031, 351))
        self.otvet_line.setStyleSheet("QTextEdit{\n"
"background-color:  rgb(37, 37, 37);\n"
"font: bold;\n"
"color: white;\n"
"padding: 25px 25px;\n"
"font: bold;\n"
"border-radius: 5px;\n"
"font-size:  18px;\n"
"}")

        self.otvet_line.setObjectName("otvet_line")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(16, 10, 1021, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"\n"
"}")

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 1031, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"color: white;\n"
"\n"
"}")

        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.exit_button = QtWidgets.QPushButton(self.widget)
        self.exit_button.setGeometry(QtCore.QRect(1010, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  none;\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  22px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.exit_button.setObjectName("exit_button")
        self.vopros_line = QtWidgets.QTextEdit(self.widget)
        self.vopros_line.setGeometry(QtCore.QRect(10, 130, 961, 41))
        self.vopros_line.setStyleSheet("QTextEdit{\n"
"background-color:  rgb(37, 37, 37);\n"
"font: bold;\n"
"color: white;\n"
"padding: 5px 6px;\n"
"font: bold;\n"
"border-radius: 5px;\n"
"font-size:  18px;\n"
"scrollbar: off;\n"
"}")    
        
        self.vopros_line.setPlaceholderText('Задайте вопрос нейросети')
        self.vopros_line.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vopros_line.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.vopros_line.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.vopros_line.setObjectName("vopros_line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_button.setText(_translate("Form", "🔎"))
        self.otvet_line.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", "Chat GPT"))
        self.label_3.setText(_translate("Form", "_______________________________________________________________________________________"))
        self.exit_button.setText(_translate("Form", "⮾"))
        self.vopros_line.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.exit_button.setText(_translate("Form", "⮾"))
        self.vopros_line.setPlaceholderText('Задайте вопрос нейросети')

        self.exit_button.clicked.connect(self.exit)
        self.search_button.clicked.connect(self.chatgpt_ask)
        
        
    def exit(self):
        self.mw = f_pasrer_menu.MainWindow()
        self.mw.show()
        f_parser_chatGPT.MainWindow.hide(self)


    def chatgpt_ask(self):
        
        openai.api_key = "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"

        vopros = self.vopros_line.toPlainText()

        my_file = open("z_z_99_chatGPT.txt")
        file_contents = my_file.read()

        prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\n" + file_contents + "Human: \nAI:",

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\n" + file_contents + "Human: " + vopros + "\nAI:",
        max_tokens=1024,
        frequency_penalty=0.0,
        presence_penalty=0.6,

        stop= [" Human: ", " AI:"]

        )
        my_file.close()

        otvet = response.choices[0].text
        self.otvet_line.setText(otvet)

        my_file = open("z_z_99_chatGPT.txt", "a+")
        my_file.write("Human: " + vopros + "\nAI:" + otvet + "\n")
        my_file.close()


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




