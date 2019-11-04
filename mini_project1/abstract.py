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

def getAbstract(data):
    fname = data[0]
    lname = data[1]
    name = (fname, lname)
    # count lifetime data
    countTicket_query = "select count(*) from tickets t left outer join registrations r on t.regno = r.regno where fname = ? and lname = ?;"
    get_data = cursor.execute(countTicket_query,name).fetchall()
    count_ticket = get_data[0][0]
    
    countNotice_query  =  "select count(*) from demeritNotices where fname = ? and lname = ?;" 
    get_data = cursor.execute(countNotice_query,name).fetchall()
    count_Notice = get_data[0][0]
    
    countPoints_query = "select sum(points) from demeritNotices where fname = ? and lname = ?;" 
    get_data = cursor.execute(countPoints_query,name).fetchall()
    count_points = get_data[0][0]  
    
    # count last two years data
    count2Ticket_query = "select count(*) from tickets t left outer join registrations r on t.regno = r.regno where fname = ? and lname = ? and vdate >= DATE('NOW', '-2 YEAR');"
    get_data = cursor.execute(count2Ticket_query,name).fetchall()
    count2_ticket = get_data[0][0]   
    
    count2Notice_query = "select count(*) from demeritNotices where fname = ? and lname = ? and ddate >= DATE('NOW', '-2 YEAR');"
    get_data = cursor.execute(count2Notice_query,name).fetchall()
    count2_Notice = get_data[0][0]
    
    count2Points_query = "select sum(points) from demeritNotices where fname = ? and lname = ? and ddate >= DATE('NOW', '-2 YEAR');"
    get_data = cursor.execute(count2Points_query,name).fetchall()
    count2_points = get_data[0][0]     
    connection.commit()
    print("Total tickets count: %d" % count_ticket)
    print("Total demerit notices count: %d" % count_Notice)
    print("Total demerit points: %d" %  count_points)
    print("Past two year tickets count: %d" % count2_ticket )
    print("Past two year demerit notices count: %d" % count2_Notice)
    print("Past two year demerit points count: %d" % count2_points)
    
    choice = input('Would you like to see the each tickets?(input y to see the detail)')
    if choice.lower() == 'y':
        display_query = "select tno, vdate, violation, fine, tickets, regno, make, model from tickets t left outer join registrations  r on t.regno = r.regno left outer join vehicles v on v.vin = r.vin where fname = ? and lname = ? order by vdate desc limit 5;"
        get_data = cursor.execute(display_query,name).fetchall()
        print(get_data)        
        choice = input('Would you like to see the all tickets?(input y to see the total list)')
        display_query = "select tno, vdate, violation, fine, tickets, regno, make, model from tickets t left outer join registrations  r on t.regno = r.regno left outer join vehicles v on v.vin = r.vin where fname = ? and lname = ? order by vdate desc;"
        get_data = cursor.execute(display_query,name).fetchall()
        print(get_data)  
        connection.commit()
     
    return
    
