# Файл запуска, параллельные процессы приложения и уведомлений

from multiprocessing import Process
from notify import notify1
from main import App, QApplication
import time
import sys


def start2():
    while True:
        notify1()
        time.sleep(5)


def start1():
    while True:
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())


p1 = Process(target=start1())
p1.start()
p2 = Process(target=start2())
p2.start()

p1.join()
p2.join()


