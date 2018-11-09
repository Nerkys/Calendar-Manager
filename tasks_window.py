# ќкна уведомлений при нажатии на дату в календаре

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from data import *


class Task(QWidget):

    def __init__(self, date1):
        super(Task, self).__init__()
        self.setWindowTitle('Tasks')
        self.setGeometry(500, 750, 600, 235)
        self.setWindowIcon(QIcon('pictures\_tas.jpg'))

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        global date_db
        date_db = str(date1)[18:]

        self.buttons(date_db)
        self.show()

    def buttons(self, date):
        global l
        l = select_task(date)
        for i in range(len(l)):
            btn = QRadioButton("BTN", self)
            btn.myselfindex = i
            btn.clicked.connect(self.delete_one)
            btn.setCheckable(True)
            btn.setText(str(l[i][1]) + "   " + str(l[i][2]) + "   " + str(l[i][3]))
            self.main_layout.addWidget(btn)

    def myselfClickHandler(self):
        ind = self.sender().myselfindex
        remove_task(str(l[ind][2]), str(l[ind][3]))

    def delete_one(self):
        message = 'Are you sure?'
        reply = QMessageBox.question(self, 'Message', message, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.myselfClickHandler()
        else:
            QMessageBox.Close






