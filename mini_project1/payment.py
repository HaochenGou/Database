import sqlite3
import time
import hashlib
from datetime import datetime
connection = None
cursor = None

def payment():
    t_tno = input("Please input ticket number: ")
    t_payment = 0
    while
    t_payment = input("Please input payment: ")
    if  t_payment  == 0:
        raise Exception('Invalid payment.')
    self.cursor.execute('select * from tickets where tno =:tno limit 1', {"tno": t_tno})
    self.conn.commit() 
    get_data = self.cursor.fetchall()   
    if get_data is None:
        raise Exception('Invalid ticket number.')
    if  t_payment > get_data[0][2]:
        raise Exception('Invalid payment.')
    self.cursor.execute('select * from payments where tno =:tno', {"tno": t_tno})
    self.conn.commit()   
    get_pay = self.cursor.fetchall()
    sum_pay = get_pay[0][2] +  t_payment
    if sum_pay > get_data[0][2]:
        raise Exception('Invalid payment.')
    pdate = datetime.date(datetime.now())
    payments = (t_tno, pdate,  t_payment)
    self.cursor.execute('insert into payments values(?,?,?);',payments)
   
    self.conn.commit()     
    return
