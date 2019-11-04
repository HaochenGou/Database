import sqlite3
import random

connection = None
cursor = None
conn = sqlite3.connect('./a2.db')

def Check_info(regis_num):
    c = conn.cursor()
    c.execute('''Select b.fname||b.lname, v.make, v.model, v.year, v.color
                 From births b, vehicles v, registrations r
                 Where b.regno = ? and b.regno = r.regno
                 and v.vin = r.vin
                 ''', (regis_num,))
    rows = c.fetchall()
    reg_result = ''
    for row in rows:
        for element in row:
            reg_result = reg_result + str(element) + '|'
    print(reg_result)

def random_num():
    c = conn.cursor()
    while True:
        ticket_num = random.randint(450, 600)
        c.execute('Select * from tickets t Where t.tno = ?', (ticket_num,))
        check_num = c.fetchall()
        if (len(check_num)) != 0:
            ticket_num = ticket_num + 1
        else:
            return ticket_num
        
def Issue_ticket(regis_num):
    c = conn.cursor()
    v_date = input('Provide the tickets date:')
    if v_date == 'null':
        c.execute("Select date('now');")
        date = c.fetchall()
        v_date = date[0][0]
        print(v_date)
    v_fine = int(input('Provide the tickets fine:'))
    v_violation = input('Provide the violation text:')
    ticket_num = random_num()
    ticket_info = (ticket_num, regis_num, v_fine, v_violation, v_date)
    c.execute('''Insert into tickets Values(?,?,?,?,?)''', (ticket_info))
    conn.commit()

def main():
    while True:
        c = conn.cursor()
        try:   
            regis_num = input('Provide the registration number:')
            regis_num = int(regis_num)
        except:
            print('Registration number is integer!')
        c.execute("select * from registrations where regno = ?",(regis_num,))
        finding = c.fetchall()
        if len(finding) == 0:
            print('Wrong registration number!')
            main()
        Check_info(regis_num)
        Issue_ticket(regis_num)
        quit_string = input('Would you like to return to the menu(Y/N):')
        if quit_string.upper() == 'Y':
            print('Returning to the menu...')
            break
        if quit_string.upper() == 'N':
            pass
        else:
            print('Wrong input!')
    
main()