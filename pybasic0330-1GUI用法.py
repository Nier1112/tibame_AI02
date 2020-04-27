#Qt的母公司做的PySide2 , 九成根 Qt的子公司 PyQt套件相同
from PySide2 import QtWidgets, QtGui, QtCore
import sys

#創建一個QApp
app = QtWidgets.QApplication()

#執行 app, sys.exit() 是指當app.exec執行結束 python 會自動關掉的用途
#sys.exit(app.exec_())
#創建一張畫布
my_widget = QtWidgets.QWidget()
#畫上去
my_widget.show()
#設定視窗標題
my_widget.setWindowTitle("第一次的應用程式")
#設定視窗大小
my_widget.resize(800, 800)
#限制拖拉大小minimumsize是限制最小視窗size
my_widget.setMinimumSize(256, 256)
#限制拖拉大小 限制最大size
my_widget.setMaximumSize(500, 500)
#固定視窗大小 不能拖拉
my_widget.setFixedSize(450, 450)
#設定視窗初限的地方, 會出現在 (100, 50)的地方, 視窗大小事256 x 256
my_widget.setGeometry(100, 50, 256, 256)

#把標籤文字放進去, my_label 是文字
my_label = QtWidgets.QLabel("Hello, Zenyata\nhow are you?")
#把 my_label 畫在 my_widget上面, 如果不指定在一個視窗, 直接 my_label.show()就可以開新視窗並寫上文字
my_label.setParent(my_widget)
my_label.show()
#設定mywidget裡面的從左上角50, 50的位子再推估 100, 50的位子並寫上文字並且會在50的置中位子, 水平的左邊位子
my_label.setGeometry(50,50, 150, 150)
#列印出我lable畫的區塊
my_label.setStyleSheet("background-color:yellow")
#把字體改大, 需要 import QtGui 才能使用, 先創一個字體物件叫做 my_font
my_font = QtGui.QFont()
my_font.setPointSize(16)
#把 my_font的文字放入 my_label裏面
my_label.setFont(my_font)
#排版的對齊 import QtCore , 讓字體置中
my_label.setAlignment(QtCore.Qt.AlignHCenter)

#按鈕按下去之後要做甚麼樣的事情
def button_click():
    print("JOJO!!!!!!!")

#創造按鈕, 按鈕名稱叫做 Press me, 放入 my_button裏面
my_button = QtWidgets.QPushButton("Press Me!!JOJO!!!!")
my_button.setParent(my_widget)  #把按鈕放入my_widget這張畫布上面
my_button.show()
#當點擊按鈕之後的事件，會連結到 button_click 這個事件,
my_button.clicked.connect(button_click) #button_click()的 ()要去掉

#做一個點擊計數器, 點擊按鈕一下就可以把數字+1 , def 裡面的count 不能更改, 需要用global宣告def裡面的count根外面的count相同
count = 0
def button_2():
    global count
    count += 1
    print(f"{count}")
    my_label.setText(str(count)) #把計數器的數字打印在 my_widget 畫布上, .setText是動態更改文字, count是字串 換成文字

my_button2 = QtWidgets.QPushButton("Press Me and count")
my_button2.setParent(my_widget)
my_button2.show()
#當點擊按鈕之後的事件，會連結到 button_click 這個事件,
my_button2.clicked.connect(button_2) #button_click()的 ()要去掉


#執行Qapp
sys.exit(app.exec_())

# PySide2 用法參考：https://doc.qt.io/qtforpython/PySide2/QtWidgets/QApplication.html#more
# Qt module 介紹：https://doc.qt.io/qtforpython/modules.html
