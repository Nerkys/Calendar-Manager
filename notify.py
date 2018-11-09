# Создание всплывающих уведомлений

from data import *
from datetime import datetime
from sys_notifications import balloon_tip
import time


def notify1():
    notes = select_all_notify()
    dt = str(datetime.now()).split()
    d = dt[0]
    t = dt[1][:5]
    d = d.split("-")
    if d[2][0] == "0":
        date_now = "(" + d[0] + ", " + d[1] + ", " + d[2][1] + ")"
    else:
        date_now = "(" + d[0] + ", " + d[1] + ", " + d[2] + ")"
    for i in notes:
        if i[0] == date_now and i[1][:5] == t:
            balloon_tip(i[1], i[3])



notify1()
time.sleep(5)