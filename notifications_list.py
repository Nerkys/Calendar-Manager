#Окно списка уведомлений и сортировки

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from data import *


class Notifications(QtWidgets.QWidget):

    def __init__(self):
        super(Notifications, self).__init__()
        self.setWindowTitle('Notifications')
        self.setGeometry(500, 400, 300, 300)
        self.setWindowIcon(QIcon('pictures\cal.jpg'))

        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        self.sort_1 = QtWidgets.QRadioButton("Sort by category")
        self.sort_2 = QtWidgets.QRadioButton("Sort by date")

        self.sort_1.clicked.connect(self.sort_p1)
        self.sort_2.clicked.connect(self.sort_p2)

        self.txt = QtWidgets.QTextEdit()
        self.txt.setText(select_all())
        self.main_layout.addWidget(self.sort_1)
        self.main_layout.addWidget(self.sort_2)
        self.main_layout.addWidget(self.txt)
        self.show()

    def sort_p1(self):
        if self.sort_1.isChecked():
            self.txt.setText(select_all())

    def sort_p2(self):
        if self.sort_2.isChecked():
            self.txt.setText(select_all_date())