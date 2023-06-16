from PyQt5 import QtCore, QtGui, QtWidgets
import x_stylesheet_font
import c_main_interface
import g_style_changer


font_color = x_stylesheet_font.stylesheet_purple
background_color = x_stylesheet_font.background_base


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1009, 750)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 991, 731))
        self.frame.setStyleSheet(font_color)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 991, 731))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget.setStyleSheet("QWidget {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.00568182 rgba(59, 59, 59, 255), stop:1 rgba(75, 75, 75, 255)) \n"
"}")
        
        
        self.widget.setObjectName("widget")
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
        self.purple = QtWidgets.QPushButton(self.widget)
        self.purple.setGeometry(QtCore.QRect(50, 160, 131, 131))
        self.purple.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(164, 37, 232, 255), stop:1 rgba(138, 0, 178, 255));\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.purple.setText("")
        self.purple.setObjectName("purple")
        self.red = QtWidgets.QPushButton(self.widget)
        self.red.setGeometry(QtCore.QRect(190, 160, 131, 131))
        self.red.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color:  qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.00568182 rgba(232, 86, 86, 255), stop:1 rgba(178, 0, 37, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.red.setText("")
        self.red.setObjectName("red")
        self.green = QtWidgets.QPushButton(self.widget)
        self.green.setGeometry(QtCore.QRect(330, 160, 131, 131))
        self.green.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color:  qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.00568182 rgba(88, 232, 86, 255), stop:1 rgba(0, 178, 20, 255));\n"
"    color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.00568182 rgba(88, 232, 86, 255), stop:1 rgba(0, 178, 20, 255));\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.green.setText("")
        self.green.setObjectName("green")
        self.blue = QtWidgets.QPushButton(self.widget)
        self.blue.setGeometry(QtCore.QRect(470, 160, 131, 131))
        self.blue.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color:  qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.703, fx:0.5, fy:0.5, stop:0 rgba(17, 136, 196, 255), stop:1 rgba(0, 104, 255, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.blue.setText("")
        self.blue.setObjectName("blue")
        self.yellow = QtWidgets.QPushButton(self.widget)
        self.yellow.setGeometry(QtCore.QRect(50, 300, 131, 131))
        self.yellow.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.703, fx:0.5, fy:0.5, stop:0 rgba(196, 168, 17, 255), stop:1 rgba(255, 216, 0, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.yellow.setText("")
        self.yellow.setObjectName("yellow")
        self.orange = QtWidgets.QPushButton(self.widget)
        self.orange.setGeometry(QtCore.QRect(190, 300, 131, 131))
        self.orange.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.703, fx:0.5, fy:0.5, stop:0 rgba(196, 78, 17, 255), stop:1 rgba(255, 129, 0, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.orange.setText("")
        self.orange.setObjectName("orange")
        self.off_edge = QtWidgets.QPushButton(self.widget)
        self.off_edge.setGeometry(QtCore.QRect(470, 300, 131, 131))
        self.off_edge.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.off_edge.setObjectName("off_edge")
        self.gray = QtWidgets.QPushButton(self.widget)
        self.gray.setGeometry(QtCore.QRect(330, 300, 131, 131))
        self.gray.setStyleSheet("QPushButton {\n"
"    border-radius:  55px;\n"
"    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0.0170455 rgba(113, 113, 113, 255), stop:1 rgba(82, 82, 82, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.gray.setText("")
        self.gray.setObjectName("gray")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 30, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: None;\n"
"}")
        
        
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.purple_wind = QtWidgets.QPushButton(self.widget)
        self.purple_wind.setGeometry(QtCore.QRect(660, 160, 131, 131))
        self.purple_wind.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0.506, y1:1, x2:0.511, y2:0, stop:0.0170455 rgba(126, 56, 142, 255), stop:1 rgba(66, 62, 138, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.purple_wind.setText("")
        self.purple_wind.setObjectName("purple_wind")
        self.green_wind = QtWidgets.QPushButton(self.widget)
        self.green_wind.setGeometry(QtCore.QRect(800, 160, 131, 131))
        self.green_wind.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color: qlineargradient(spread:repeat, x1:0.506, y1:1, x2:0.511, y2:0, stop:0.0170455 rgba(41, 106, 90, 255), stop:1 rgba(27, 106, 46, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.green_wind.setText("")
        self.green_wind.setObjectName("green_wind")
        self.yellow_wind = QtWidgets.QPushButton(self.widget)
        self.yellow_wind.setGeometry(QtCore.QRect(660, 300, 131, 131))
        self.yellow_wind.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  qlineargradient(spread:repeat, x1:0.506, y1:1, x2:0.511, y2:0, stop:0 rgba(221, 126, 78, 255), stop:1 rgba(144, 141, 50, 255));\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.yellow_wind.setText("")
        self.yellow_wind.setObjectName("yellow_wind")
        self.standart_wind = QtWidgets.QPushButton(self.widget)
        self.standart_wind.setGeometry(QtCore.QRect(800, 300, 131, 131))
        self.standart_wind.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        
        
        self.standart_wind.setObjectName("standart_wind")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(680, 30, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: None;\n"
"}")
        
        
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.test_frame = QtWidgets.QFrame(self.widget)
        self.test_frame.setGeometry(QtCore.QRect(50, 470, 891, 211))
        self.test_frame.setStyleSheet(font_color)
        self.test_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_frame.setObjectName("test_frame")
        self.test_widget = QtWidgets.QWidget(self.test_frame)
        self.test_widget.setGeometry(QtCore.QRect(10, 10, 871, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.test_widget.setFont(font)
        self.test_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.test_widget.setStyleSheet(background_color)
        self.test_widget.setObjectName("test_widget")
        self.label_3 = QtWidgets.QLabel(self.test_widget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 871, 161))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: None;\n"
"}")
        
        
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.exit_btn = QtWidgets.QPushButton(self.widget)
        self.exit_btn.setGeometry(QtCore.QRect(950, 0, 41, 41))
        self.exit_btn.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  none;\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  22px;\n"
"}\n"
"\n"
"")
        
        
        self.exit_btn.setObjectName("exit_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exit_button.setText(_translate("Form", "⮾"))
        self.off_edge.setText(_translate("Form", "НЕТ"))
        self.label.setText(_translate("Form", "ЦВЕТ РАМКИ"))
        self.standart_wind.setText(_translate("Form", "BASE"))
        self.label_2.setText(_translate("Form", "ЦВЕТ ФОНА"))
        self.label_3.setText(_translate("Form", "Привет, я окно для тестов!"))
        self.exit_btn.setText(_translate("Form", "⮾"))
        
        self.exit_btn.clicked.connect(self.exit)
        
        self.purple.clicked.connect(self.purple_def)
        self.red.clicked.connect(self.red_def)
        self.green.clicked.connect(self.green_def)      
        self.blue.clicked.connect(self.blue_def)
        self.yellow.clicked.connect(self.yellow_def)
        self.orange.clicked.connect(self.orange_def)
        self.gray.clicked.connect(self.gray_def)
        self.off_edge.clicked.connect(self.off_edge_def)  

        self.purple_wind.clicked.connect(self.purple_wind_def)
        self.green_wind.clicked.connect(self.green_wind_def)
        self.yellow_wind.clicked.connect(self.yellow_wind_def)
        self.standart_wind.clicked.connect(self.standart_wind_def)


    def exit(self):
        self.mw = c_main_interface.MainWindow_main()
        self.mw.show()
        g_style_changer.MainWindow.hide(self)


    def purple_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_purple
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def red_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_red
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def green_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_green
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def blue_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_blue
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def yellow_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_yellow
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def orange_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_orange
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def gray_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_gray
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def off_edge_def(self):
        global font_color
        font_color = x_stylesheet_font.stylesheet_none
        self.test_frame.setStyleSheet(g_style_changer.font_color)


    def purple_wind_def(self):
        global background_color
        background_color = x_stylesheet_font.background_purple
        self.test_widget.setStyleSheet(g_style_changer.background_color)


    def green_wind_def(self):
        global background_color
        background_color = x_stylesheet_font.background_green
        self.test_widget.setStyleSheet(g_style_changer.background_color)


    def yellow_wind_def(self):
        global background_color
        background_color = x_stylesheet_font.background_yellow
        self.test_widget.setStyleSheet(g_style_changer.background_color)
                

    def standart_wind_def(self):
        global background_color
        background_color = x_stylesheet_font.background_base
        self.test_widget.setStyleSheet(g_style_changer.background_color)




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
    