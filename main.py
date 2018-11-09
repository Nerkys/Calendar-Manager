# Основное окно приложения

import sys

from PyQt5.QtWidgets import (QMessageBox, QMainWindow, QWidget, QAction, qApp, QVBoxLayout, QApplication, QCalendarWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate

from data import *
from tasks_window import Task
from add_window import AddWindow
from notifications_list import Notifications


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def add(self):
        self.ex1 = AddWindow()

    def all_notifications(self):
        self.w2 = Notifications()

    def clear_all(self):
        message = 'Are you sure?'
        reply = QMessageBox.question(self, 'Message', message, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            clear_tasks()
        else:
            QMessageBox.Close

    def tasks_show(self):
        date1 = cal.selectedDate()
        self.w1 = Task(date1)

    def init_ui(self):
        global cal
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.tasks_show)

        tools = QMainWindow()
        exit_action = QAction(QIcon('pictures\exit.png'), 'Exit', tools)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)
        add_action = QAction(QIcon('pictures\plus.png'), 'Add notification', tools)
        add_action.triggered.connect(self.add)
        list_action = QAction(QIcon("pictures\list.png"), "Notifications list", tools)
        list_action.triggered.connect(self.all_notifications)
        clear_action = QAction(QIcon("pictures\_basket.bmp"), "Clear all tasks", tools)
        clear_action.triggered.connect(self.clear_all)

        tools.toolbar = tools.addToolBar('Exit')
        tools.toolbar.addAction(add_action)
        tools.toolbar.addAction(list_action)
        tools.toolbar.addAction(clear_action)
        tools.toolbar.addAction(exit_action)

        vbox = QVBoxLayout()
        vbox.addWidget(tools)
        vbox.addWidget(cal)
        vbox.addStretch(1)


        self.setLayout(vbox)
        self.setGeometry(500, 400, 600, 600)
        self.setWindowTitle('Task reminder by Saf & CHu Calculated')
        self.setWindowIcon(QIcon('pictures\cal'))
        self.show()
        self.tasks_show()

    def show_date(self, date1):
        self.lbl.setText(str(select_task(date1.toString())))


