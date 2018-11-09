# Laba1-Safonov-Chuhvantzev
Файл запуска - main_threads 

В нем создаются 2 параллельных процесса.

1 процесс -приложение (main). 2 процесс - отправка уведомлений (notify)

main - основной файл приложения. 

В нем создается главноое окно и вызываюся остальные окна.

notification_list - окно списка задач. В нем же сортировка.

add_window - окно добавления задач. 

tasks_window - окна уведомлений, которые появляются при нажатии на календарную дату.

sys_notifications - функция отправки уведомления в центр уведомлений windows. 

data - функции общения с базой данных.

Она работает только если уведомления включены.

notify создает эти уведомления. 

Если в базе данных существует напоминание с текущим временем и датой (с точностью до минут),

то notify отправляет это напоминание в центр уведомлений windows.

# Импорты

from PyQt5.QtWidgets import *

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import QDate

from multiprocessing import Process

import time

import sys

from datetime import datetime

import sqlite3

import os

import win32con (он находится в pywin32)

import win32gui

from win32api import GetModuleHandle

