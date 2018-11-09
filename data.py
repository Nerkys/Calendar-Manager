# Функции общения с базой данных

import sqlite3

conn = sqlite3.connect("database_lab_1.db")
cursor = conn.cursor()
#cursor.execute("""CREATE TABLE notifications (date text, time text, category text, text1 text)""")


def add_task(date, time, category, text):
    sql = """INSERT INTO notifications
    VALUES (?, ?, ?, ?)
    """
    cursor.executemany(sql, [(date, time, category, text)])
    conn.commit()


def remove_task(category, text):
    sql = """DELETE FROM notifications WHERE category = ? AND text1 ='%s'"""%text
    cursor.execute(sql, [(category)])
    conn.commit()


def select_task(date):
    sql = "SELECT * FROM notifications WHERE date=?"
    cursor.execute(sql, [(date)])
    return cursor.fetchall()

def select_all_notify():
    cursor.execute("SELECT * FROM notifications ORDER BY category")
    rows = cursor.fetchall()
    return rows

def select_all():
    cursor.execute("SELECT * FROM notifications ORDER BY category")
    rows = cursor.fetchall()
    c = ""
    for i in range(len(rows)):
        c += " \n "
        for j in range(len(rows[i])):
            c += rows[i][j]
            c += "  "
    return c


def select_all_date():
    cursor.execute("SELECT * FROM notifications ORDER BY date")
    rows = cursor.fetchall()
    c = ""
    for i in range(len(rows)):
        c += " \n "
        for j in range(len(rows[i])):
            c += rows[i][j]
            c += "  "
    return c


def clear_tasks():
    cursor.execute("DELETE  FROM notifications")
    conn.commit()

#print(select_task("(2018, 10, 3)"))
#clear_tasks()
#print(select_task("(2018, 10, 3)"))