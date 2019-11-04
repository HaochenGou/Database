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

def process_sale():
    car_vin = input("Please input vin of car: ")
    cur_fn = input("Please input first name of current onwer: ")
    cur_ln = input("Please input last name of current onwer: ")
    new_fn = input("Please input first name of new onwer: ")
    new_ln = input("Please input last name of new onwer: ")
    cursor.execute('select * from registrations where vin =:vin limit 1', {"vin": car_vin})
    connection.commit() 
    get_data = cursor.fetchall() # get data from database
    if cur_fn.lower() != getdata[0][5].lower:
        raise Exception('Wrong name.')
    if cur_ln.lower() != getdata[0][6].lower:
        raise Exception('Wrong name.')  # check name
    
    exp_date = datetime.date(datetime.now())
    new_date = exp_date.replace(exp_date.year + 1)
    new_regno= random.randint(100, 9999) # get new regno
    regno_data = cursor.execute('select * from registrations where regno =:regno limit 1', {"regno": new_regno}).fetchall()
    while regno_data != NUll:
        new_regno= random.randint(100, 9999) # get new regno
        regno_data = cursor.execute('select * from registrations where regno =:regno limit 1', {"regno": new_regno}).fetchall()        
    old_data = (exp_date, get_data[0][4])
    cursor.execute('update registrations set expiry = ? where vin = ?;', old_date)
    connection.commit() 
    new_data = (new_regno, exp_date, new_date, get_data[0][3], get_data[0][4], new_fn, new_ln)
    cursor.execute('insert into registrations values(?,?,?,?,?,?);',new_data)
    connection.commit() 
    return
