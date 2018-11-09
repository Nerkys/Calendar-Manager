# Окно добавления задачи

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from data import *


class AddWindow(QtWidgets.QWidget):

    def __init__(self):
        super(AddWindow, self).__init__()
        self.setWindowTitle('Add')
        self.setGeometry(500, 400, 300, 300)
        self.setWindowIcon(QIcon('pictures\_new.bmp'))

        self.rec1 = QtWidgets.QRadioButton("Every day")
        self.rec2 = QtWidgets.QRadioButton("Every week")

        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        self.lines = []
        self.button = QtWidgets.QPushButton('Add Notification')

        self.main_layout.addWidget(self.rec1)
        self.main_layout.addWidget(self.rec2)

        self.lables = ["Date (Year, Month, Day)", "Time", "Category", "Text"]

        self.build_widgets()
        self.show()

    def build_widgets(self):
        for i in range(4):
            texts = QtWidgets.QLabel(self.lables[i])
            line = QtWidgets.QLineEdit()
            self.main_layout.addWidget(texts)
            self.main_layout.addWidget(line)
            self.lines.append(line)

        self.button.clicked.connect(self.add_notification)
        self.main_layout.addWidget(self.button)

    def add_notification(self):
        add_task(str(self.lines[0].text()), str(self.lines[1].text()), str(self.lines[2].text()), str(self.lines[3].text()))


