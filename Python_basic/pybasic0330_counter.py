from PySide2 import QtWidgets, QtGui, QtCore

#有一個 counter 繼承 QtWidgets的元件, counter就是一個 QtWidgets的畫布可以讓人在上面放東西
class Counter(QtWidgets.QWidget):
    def __init__(self):
        super(Counter, self).__init__()

        self.count = 0

        self.label_count = QtWidgets.QLabel("Hello, Zenyata\nhow are you?")
        self.label_count.setParent(self)
        self.label_count.show()
        self.label_count.setGeometry(0, 0, 200, 50)
        self.label_count.show()
        self.label_count.setStyleSheet("background-color:yellow")
        self.font_label = QtGui.QFont()
        self.font_label.setPointSize(16)
        self.label_count.setFont(self.font_label)
        self.label_count.setAlignment(QtCore.Qt.AlignHCenter)
        self.button_add = QtWidgets.QPushButton("Press Me!!JOJO!!!!")
        self.button_add.setParent(self)  # 把按鈕放入my_widget這張畫布上面
        self.button_add.show()
        self.button_add.setGeometry(0, 50, 200, 50)
        self.button_add.clicked.connect(self.add_one) #注意是 self.add_one 這個 function

    def add_one(self):
        self.count += 1 #設定按鈕按下去 +1
        self.label_count.setText(str(self.count)) #設定把加過的數值用動態表示文字

