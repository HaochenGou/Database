import sqlite3
import time
import hashlib
from datetime import datetime
connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return

def payment(data):
    t_tno = data[0]
    if data[1] == 0:
        raise Exception('Invalid payment.')
    cursor.execute('select * from tickets where tno =:tno limit 1', {"tno": t_tno})
    connection.commit() 
    get_data = cursor.fetchall()   
    if get_data is None:
        raise Exception('Invalid ticket number.')
    if data[0] > get_data[0][2]:
        raise Exception('Invalid payment.')
    cursor.execute('select * from payments where tno =:tno', {"tno": t_tno})
    connection.commit()   
    get_pay = cursor.fetchall()
    sum_pay = get_pay[0][2] + data[1]
    if sum_pay > get_data[0][2]:
        raise Exception('Invalid payment.')
    pdate = datetime.date(datetime.now())
    payments = (t_tno, pdate, data[1])
    cursor.execute('insert into payments values(?,?,?);',payments)
   
    connection.commit()     
    return
