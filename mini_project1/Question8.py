import sqlite3
import random

connection = None
cursor = None
conn = sqlite3.connect('./a2.db')

def Check_info(regis_num, self):
    self.cursor.execute('''Select b.fname||b.lname, v.make, v.model, v.year, v.color
                 From births b, vehicles v, registrations r
                 Where b.regno = ? and b.regno = r.regno
                 and v.vin = r.vin
                 ''', (regis_num,))
    rows = self.cursor.fetchall()
    reg_result = ''
    for row in rows:
        for element in row:
            reg_result = reg_result + str(element) + '|'
    print(reg_result)

def random_num(self):
    while True:
        ticket_num = random.randint(450, 600)
        self.cursor.execute('Select * from tickets t Where t.tno = ?', (ticket_num,))
        check_num = self.cursor.fetchall()
        if (len(check_num)) != 0:
            ticket_num = ticket_num + 1
        else:
            return ticket_num
        
def Issue_ticket(regis_num, self):
    v_date = input('Provide the tickets date:')
    if v_date == 'null':
        self.cursor.execute("Select date('now');")
        date = self.cursor.fetchall()
        v_date = date[0][0]
        print(v_date)
    v_fine = int(input('Provide the tickets fine:'))
    v_violation = input('Provide the violation text:')
    ticket_num = random_num()
    ticket_info = (ticket_num, regis_num, v_fine, v_violation, v_date)
    self.cursor.execute('''Insert into tickets Values(?,?,?,?,?)''', (ticket_info))
    self.connection.commit()

def Question8(self):
    regis_num = input('Provide the registration number:')
    regis_num = int(regis_num)    
    self.Check_info(regis_num)
    self.Issue_ticket(regis_num)
