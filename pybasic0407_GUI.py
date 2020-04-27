from PySide2 import QtWidgets, QtCore, QtGui
import sys

app = QtWidgets.QApplication()
my_widget = QtWidgets.QWidget()
my_widget.resize(256, 256)
my_widget.show()

my_widget.setWindowTitle("圖片處理") #設定抬頭

#設定icon
my_icon = QtGui.QIcon("./peace.png") #把 peace.png的圖放進my_icon
my_widget.setWindowIcon(my_icon) #把my_icon放置到windowtitle
#放圖片
my_pixmap = QtGui.QPixmap("./peace.png") #pixmap是指把圖的每一個點都讀取出來
print(my_pixmap.size()) #看圖片大小
my_label = QtWidgets.QLabel() #Qlabel空的不放字體
my_label.setParent(my_widget)
my_label.setPixmap(my_pixmap.scaled(250, 250)) #scaled是用預設的方法縮放圖片大小, 用此方法就可以不用setGeometry
#my_label.setGeometry(10, 10, 150, 150)
my_label.show()

def on_click():
    print("peace,")

my_button = QtWidgets.QPushButton()
my_button.setIcon(my_icon)
my_button.setParent(my_widget)
my_button.setGeometry(255, 255, 128, 128)
my_button.show()
my_button.clicked.connect(on_click) #連結案件按下去的事件
my_button.setIconSize(QtCore.QSize(120, 120))

sys.exit(app.exec_())