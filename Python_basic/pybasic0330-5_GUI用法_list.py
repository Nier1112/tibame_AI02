from PySide2 import QtWidgets, QtGui, QtCore
import sys
#製作一個可以輸入文字的對話框

app = QtWidgets.QApplication()
my_widget = QtWidgets.QWidget()
my_widget.show()

#創建一個列表的顯式, 可以加入東西和刪除東西
my_list = QtWidgets.QListWidget()
my_list.setParent(my_list)
my_list.show()

index = 0
def add_item():
    global index
    index += 1
    my_list.addItem(str(f"內容:"))

def del_item():
    itmes = my_list.selectedItems()
    #print(itmes[0].text())     #用 selectedItems() 拿取的東西是一個 list
    # items 是我所選擇的項目, my_list,takeItems 是拿取 my_list.row 這一行裏面 index=0的 items
    my_list.takeItem(my_list.row(itmes[0]))   #take.takeItem(0) 是拿取最上面那一個　item

#創建一個新增按鈕
button_add = QtWidgets.QPushButton("新增")
button_add.setParent(my_widget)
button_add.setGeometry(0, 200, 100, 20)
button_add.show()
button_add.clicked.connect(add_item)

#創建一個刪除按鈕
button_del = QtWidgets.QPushButton("刪除")
button_del.setParent(my_widget)
button_del.setGeometry(105, 200, 100, 20)
button_del.show()
button_del.clicked.connect(del_item)



sys.exit(app.exec_())