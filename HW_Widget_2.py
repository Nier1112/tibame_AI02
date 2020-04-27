from PySide2 import QtWidgets, QtGui, QtCore
import sys
from PySide2.QtWidgets import QHeaderView, QVBoxLayout, QHBoxLayout
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtCore import Qt
#做一個app, 裡面有一個Qwidget()物件，放入my_widget裡面
app = QtWidgets.QApplication()
my_widget = QtWidgets.QWidget()
my_widget.resize(800, 600)
my_widget.show()

my_widget.setWindowTitle("記帳簿")
my_widget.setWindowIcon(QtGui.QIcon("./money.jpg"))

#左邊做一個顯示檔案的table
left_ = QtWidgets.QTableWidget()
#下面都是設定這個table的外觀
left_.setColumnCount(2)
left_.setHorizontalHeaderLabels(["項目", "價格"]) #把表頭放進left_的表格裡面
left_.horizontalHeader().setSectionsClickable(False) #設定表頭不能點選
left_.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #設定可伸縮表頭符合視窗大小

#add按鍵按下去之後做的事情
my_items = 0
def add_elemt():
    global my_items
    des = right_description.text() #拿取right_description裡面的文字
    price = right_price.text()
    left_.insertRow(my_items) #每當寫入的時候先增加一個列
    des_items = QtWidgets.QTableWidgetItem(des)
    price_items = QtWidgets.QTableWidgetItem(f"{price}")
    left_.setItem(my_items, 0, des_items)
    left_.setItem(my_items, 1, price_items)
    my_items += 1

#clear按鍵按下去之後做的事情
def clear_element():
    left_.setRowCount(0) #全部清除

#劃出圓餅圖
def plotpie():
    pies  = QtCharts.QPieSeries() #將一個圓餅圖物件放入pies裡面
    for i in range(left_.rowCount()): #用for迴圈將讀取欄
        word = left_.item(i, 0).text() #item第一個參數是跑rowCount(), 0是指取左邊那一欄的文字
        cost = left_.item(i, 1).text() #第一個參數是跑過rowCount(), 1是指取右邊那一欄文字
        pies.append(word, float(cost)) #將文字和數字加入pies裡面

    chart = QtCharts.QChart()   #製作一個Chart畫布物件，放入chart裡面
    chart.addSeries(pies)       #將pies資訊放入chart裡面
    chart.legend().setAlignment(Qt.AlignTop) #文字往上對齊
    right_chart.setChart(chart)  #將chart資訊放入right_chart裡面


#右邊零件製造
right_de = QtWidgets.QLabel("項目")
right_description = QtWidgets.QLineEdit() #項目的對話框
right_pri = QtWidgets.QLabel("價格")
right_price = QtWidgets.QLineEdit()  #價格的對話框
#add 按鍵, 連結到add_elemt
right_add = QtWidgets.QPushButton("add")
right_add.setIcon(QtGui.QIcon("./add.jpg"))
right_add.clicked.connect(add_elemt)
#畫圓餅圖按鍵
right_plot = QtWidgets.QPushButton("plot")
right_plot.clicked.connect(plotpie)
#空的圓餅圖
right_chart = QtCharts.QChartView()
right_chart.setRenderHint(QPainter.Antialiasing) #在右邊先佔一個位子
#clear按鍵，按下去全部消除
right_clear = QtWidgets.QPushButton("clear")
right_clear.clicked.connect(clear_element)

#離開按鍵, 設定文字，圖片, 設定離開程式
right_quite = QtWidgets.QPushButton("quiet")
right_quite.setIcon(QtGui.QIcon("./exit.png"))
right_quite.clicked.connect(my_widget.close)


#把上面右邊元件以垂直排列放到 right_裡面
right_ = QVBoxLayout() #設定一個垂直排列的畫布元件下面是把這些東西放到right_裡面
right_.addWidget(right_de)
right_.addWidget(right_description)
right_.addWidget(right_pri)
right_.addWidget(right_price)
right_.addWidget(right_add)
right_.addWidget(right_plot)
right_.addWidget(right_chart)
#right_.addStretch() #add按鈕以下製作一個可拉伸的空間
right_.addWidget(right_clear)
right_.addWidget(right_quite)


layout = QHBoxLayout() #設定一個水平輸出元件放到layout裡面
layout.addWidget(left_) #把left_裡面的 Qtalbe元件都放入layout裡面
layout.addLayout(right_) #把right_的原件都放到layout裡面
my_widget.setLayout(layout) #把layout放到my_widget裡面

#執行系統
sys.exit(app.exec_())