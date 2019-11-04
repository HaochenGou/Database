import sqlite3
import time
import hashlib
from datetime import datetime

def payment():
    get_data = 0
    while get_data == 0:
        t_tno = input("Please input ticket number: ")
        get_data = self.cursor.execute('select * from tickets where tno =:tno limit 1', {"tno": t_tno}).fetchall()  
        self.conn.commit() 
        if get_data == 0 :
            print("invaild ticket number.")
    t_payment = 0
    while t_payment == 0:
        t_payment = input("Please input payment: ")
        if  t_payment  == 0:
            print('Invalid payment.')       
          
    while t_payment > get_data[0][2]:
        print('Invalid payment.')
        t_payment = input("Please input payment: ")
        
    get_pay = self.cursor.execute('select * from payments where tno =:tno', {"tno": t_tno}).fetchall()
    sum_pay = get_pay[0][2] +  t_payment
    if sum_pay > get_data[0][2]:
        raise Exception('Invalid payment.')
    pdate = datetime.date(datetime.now())
    payments = (t_tno, pdate,  t_payment)
    self.cursor.execute('insert into payments values(?,?,?);',payments)
   
    self.conn.commit()   
    choice = 0
    while choice != "r":
        choice = input("Input r to return menu:")
        if choice = "r":
        self.agent_oper()
   
