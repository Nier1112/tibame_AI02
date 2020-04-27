from PySide2 import QtWidgets, QtGui, QtCore
import sys
#製作一個可以輸入文字的對話框

app = QtWidgets.QApplication()
my_widget = QtWidgets.QWidget()
my_widget.show()

my_input = QtWidgets.QLineEdit()
my_input.setParent(my_widget)
my_input.setGeometry(5, 5, 100, 20)
my_input.show()

def get_value():  #做一個函式, 按鈕按下去會執行的東西
    print(my_input.text()) #取值的方法 在框框內打甚麼就取什麼

my_button = QtWidgets.QPushButton("取值按下去")
my_button.setParent(my_widget)
my_button.setGeometry(5, 25, 100, 20)
my_button.show()
my_input.setEchoMode((QtWidgets.QLineEdit.Password)) #可以把輸入的文字變成遮罩, 做密碼輸入的時候可以用
my_input.setPlaceholderText("Password^_^") #再輸入對話框內做一個透明的提式訊息
my_button.clicked.connect(get_value)   #把輸入的值連結到 get_value這個函式

sys.exit(app.exec_())
