from PySide2 import QtWidgets, QtGui, QtCore
import sys
#從另外一個 .py檔案 匯入 裏面的 class, Counter
from pybasic0330_counter import Counter  # 檔名不能有 - 符號, 會無法 import

app = QtWidgets.QApplication()
my_widget = QtWidgets.QWidget()
my_widget.show()

my_counter1 = Counter()
my_counter2 = Counter()
my_counter3 = Counter()
my_counter4 = Counter()
my_counter5 = Counter()

h_layout = QtWidgets.QVBoxLayout()  #QHBoxLayout(), 水平排好, QHVBoxLayout() 垂直排好
h_layout.addWidget(my_counter1)
h_layout.addWidget(my_counter2)
h_layout.addWidget(my_counter3)
h_layout.addWidget(my_counter4)
h_layout.addWidget(my_counter5)

my_widget.setLayout(h_layout)

sys.exit(app.exec_())


