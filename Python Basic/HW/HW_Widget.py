# from PySide2 import QtWidgets, QtGui, QtCore
# import sys
#
# #先做一個app
# app = QtWidgets.QApplication()
# #做一個空白畫布
# my_widget = QtWidgets.QWidget()
# #打印
# my_widget.show()
#
# my_widget.setWindowTitle("記帳簿")
# my_widget.resize(800,800)
# #放標籤文字
# my_label = QtWidgets.QLabel("第一個記帳簿")
# my_label.setParent(my_widget) #要指定這個label要畫在 my_widget上面, 如果要開多個視窗的互動，就不用setParent 會自動開啟新視窗
# my_label.show()
# #調整標籤文字
# my_label.setGeometry(250, 5, 250, 250)
# #my_label.setStyleSheet("background-color:yellow")
# #調整字體大小
# my_font = QtGui.QFont()
# my_font.setPointSize(16)
# my_label.setFont(my_font)
#
# #字體置中
# my_label.setAlignment(QtCore.Qt.AlignHCenter)
# my_right_chart = QtWidgets.QVBoxLayout()
# my_right_chart.setParent(my_widget)
#
# index = 0
# def button_click():
#     global index
#     mylist_.addItem(str(index))
#     index += 1
#     #my_label.setText(word)
#
# def button_2():
#     items = mylist_.selectedItems()
#     mylist_.takeItem(mylist_.row(items[0]))
#
#
# my_button = QtWidgets.QPushButton("新增")
# my_button.setParent(my_widget)
# my_button.setGeometry(330, 50, 90, 30)
# my_button.show()
# my_button.clicked.connect(button_click)
#
# my_button = QtWidgets.QPushButton("刪除")
# my_button.setParent(my_widget)
# my_button.setGeometry(430, 50, 90, 30)
# my_button.show()
# my_button.clicked.connect(button_2)
#
# my_input =QtWidgets.QLineEdit() #輸入文字對話框
# my_input.setParent(my_widget)
# my_input.setGeometry(550, 50, 90, 30)
# my_input.show()
#
# layout_ = QtWidgets.QAbstractSpinBox() #拉霸對話框
# layout_.setGeometry(450, 250, 90, 30)
# layout_.setParent(my_widget)
# layout_.show()
#
# mylist_ =QtWidgets.QListWidget()
# mylist_.setParent(my_widget)
# mylist_.show()
# mylist_.addItem("1")
# mylist_.addItem("2")
# mylist_.addItem("3")
# mylist_.addItem("4")
#
# mycombo = QtWidgets.QComboBox()
# mycombo.setParent(my_widget)
# mycombo.setGeometry(450, 350, 90, 30)
# mycombo.show()
# mycombo.addItem("花費項目")
# mycombo.addItem("2")
# mycombo.addItem("3")
# mycombo.addItem("4")
# mycombo.setItemText(1, "伙食")
# mycombo.setItemText(2, "交通")
# mycombo.setItemText(3, "電話費")
#
# #用sys去執行
# sys.exit(app.exec_())







#網路上的範例：https://doc.qt.io/qtforpython/tutorials/expenses/expenses.html#first-signal-slot-connection
import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide2.QtCharts import QtCharts


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.items = 0

        # Example data
        self._data = {"Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
                      "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
                      "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120}

        # Left
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # Chart
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Right
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")
        self.plot = QPushButton("Plot")

        # Disabling 'Add' button
        self.add.setEnabled(False)

        self.right = QVBoxLayout()
        self.right.setMargin(10)
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addWidget(self.plot)
        self.right.addWidget(self.chart_view)
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        # QWidget Layout
        self.layout = QHBoxLayout()

        #self.table_view.setSizePolicy(size)
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)

        # Set the layout to the QWidget
        self.setLayout(self.layout)

        # Signals and Slots
        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table)
        self.description.textChanged[str].connect(self.check_disable)
        self.price.textChanged[str].connect(self.check_disable)

        # Fill example data
        self.fill_table()

    @Slot()
    def add_element(self):
        des = self.description.text()
        price = self.price.text()

        self.table.insertRow(self.items)
        description_item = QTableWidgetItem(des)
        price_item = QTableWidgetItem("{:.2f}".format(float(price)))
        price_item.setTextAlignment(Qt.AlignRight)

        self.table.setItem(self.items, 0, description_item)
        self.table.setItem(self.items, 1, price_item)

        self.description.setText("")
        self.price.setText("")

        self.items += 1

    @Slot()
    def check_disable(self, s):
        if not self.description.text() or not self.price.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    @Slot()
    def plot_data(self):
        # Get table information
        series = QtCharts.QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())
            series.append(text, number)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(chart)

    @Slot()
    def quit_application(self):
        QApplication.quit()

    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            description_item = QTableWidgetItem(desc)
            price_item = QTableWidgetItem("{:.2f}".format(price))
            price_item.setTextAlignment(Qt.AlignRight)
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)
            self.items += 1

    @Slot()
    def clear_table(self):
        self.table.setRowCount(0)
        self.items = 0


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widget = Widget()
    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec_())
