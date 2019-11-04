import sqlite3
import random
import time
import hashlib
import sys
import re
from datetime import datetime

def main():
	interface = Interface()

class Interface:

	def __init__(self):
		self.cursor = None
		self.conn = sqlite3.connect('./test.db')
		self.utype = None
		self.app_continue = True
		self.valid_login = False
		self.run()

	def run(self):
		while self.app_continue:
			self.login()
			while self.valid_login:
				if self.utype[2] == 'a':
					self.agent_oper()
				elif self.utype[2] == 'o':
					self.officer_oper()
				# exception invalid input
			print('\n''Logged Out')
		print('\n''Exited')
		

	def login(self):
		while self.app_continue == False and self.valid_login == False:
			print('\n''Please enter the valid user id and password to login.')
			#uid = input('User Id: ')
			#pwd = input('Password: ')
	                #password 
			username = input("Please input uid: ")
			password = input("Please input password: ")
			if re.match("^[A-Za-z0-9_]*$", username) and re.match("^[A-Za-z0-9_]*$", password):
				encrypt(password)
				self.conn.create_function("hash", 1, encrypt)
				data = (username, password)
				self.cursor.execute(" INSERT INTO users (uid, pwd) VALUES (?, hash(?)) ", data )
				data = (password, )
				uid = self.cursor.execute(" SELECT uid FROM member WHERE pedd LIKE hash(?) ", data).fetchall()
				user_uid = self.cursor.execute('SELECT * FROM users WHERE uid=?;' , (uid,)).fetchall()
				if username != user_uid:
					print('Invalid uid or password.')
				else:
					self.valid_login = True
	def encrypt(self,password):
		alg = hashlib.sha256()
		alg.update(password.encode("utf-8"))
		return alg.hexdigest()	
			
			

	
	def agent_oper(self):
		print('1 - Register a birth',
              '2 - Register a marriage',
              '3 - Renew a vehicle registration',
              '4 - Process a bill of sale',
              '5 - Process a payment',
              '6 - Get a driver abstract',
              'L - Logout',
              'E - Exit', sep='\n')
		option = input('\n''Choose one option to continue:')
		if option == '1':
			self.regbirth()
		elif option == '2':
			self.regimarriage()
		elif option == '3':
			self.renew_vehreg()
		elif option == '4':
			self.process_sale()
		elif option == '5':
			self.payment(data)
		elif option == '6':
			self.getAbstract(data)
		elif option.upper() == 'L':
			self.valid_login = False
		elif option.upper() == 'E':
			self.valid_login = False
			self.app_continue = False
		else:
			print('\n''Invalid Input. Please try again.') 
			self.agent_oper()

	def officer_oper(self):
		print('1 - Issue a ticket',
		      '2 - Find a car owner',
		      'L - Logout',
		      'E - Exit', sep='\n')

		option = input('\n''Choose one option to continue:')
		if option == '1':
			self.Issure_ticket(regis_num)
		elif option == '2':
			self.find_car_owner()
		elif option.upper() == 'L':
			self.valid_login = False
		elif option.upper() == 'E':
			self.valid_login = False
			self.app_continue = False
		else:
			print('\n''Invalid Input. Please try again.') 
			self.officer_oper()

	def regbirth(self):
		valid_entry = False
		while valid_entry == False:
			try:
				print('\n''Pleas fill out the following information to complete the registration.')
	
				#mother
				m_f_name = input("Mother's first name: ")
				m_f_name = input("Mother's last name: ")
				self.cursor.execute('SELECT * FROM persons WHERE fname like :mfname and lname like :mlname',
					                      {'mfname': m_f_name, 'mlname': m_l_name})
				mother_info = self.cursor.fetchall()
				if len(mother_info) > 0:
					print("Found mother's info in system.")
					address = mother_info[0][4]
					phone = mother_info[0][5]
				else:
					self.addPerson(m_f_name, m_f_name)
				
				
				#father
				f_f_name = input("Father's first name: ")
				f_f_name = input("Father's last name: ")
				self.cursor.execute('SELECT * FROM persons WHERE fname like :ffname and lname like :flname',
					                      {'ffname': f_f_name, 'flname': f_l_name})
				father_info = self.cursor.fetchall()
				if len(father_info) > 0:
					print("Found fathers's info in system.")
				else:
					self.addPerson(f_f_name, f_f_name)
	
				#create_random_regno
				ran_regno = self.getRegno()  
	
				#newborn
				f_name = input('First Name: ')
				l_name = input('Last Name: ')
				gender = input('Gender (M/F): ')
				bdate_answer = input('Birth Date (mmddyyyy): ')
				bir_date = datetime.strptime(bdate_answer, '%m%d%Y')
				bir_place = input('Birth Place: ')
				reg_place = self.__user_info[5]
				reg_date = date.today()
	
	
				#update the table
				birth = (ran_regno, f_name, l_name, reg_date, reg_place,
					         gender, f_f_name, f_l_name, m_f_name, m_l_name)
				person = (f_name, l_name, bir_date,
					          bir_place, address, phone)
				self.cursor.execute(
					    'INSERT INTO persons VALUES (?,?,?,?,?,?)', person)
				self.cursor.execute(
					    'INSERT INTO births VALUES (?,?,?,?,?,?,?,?,?,?)', birth)
				self.conn.commit()
	
			except:
				print('Invalid Entry.Please try again')
				decide_continue = input('Entry B to return back to menu OR Press Entry to retry')
				if decide_continue.upper() == 'B':
					break
				else:
					print('Retry inputs.')
	
			else:
				print('Completed registration.')
				valid_entry = True
				self.agent_oper()


	def getRegno(self):
		#create_random_regno
		while True:
			ran_num = random.randint(0,1000000)
			self.cursor.execute('SELECT * FROM births WHERE regno =:num',{"num":ran_num})
			val = self.cursor.fetchone()
			if bool(val) == False:
				return(ran_num)
			
	def addPerson(self,f_name,l_name):
		print(f_name + ' ' + l_name + 'is not found. Please fill out the related inforation to complete')
		birthdate = str(input('Birth Date (mmddyyyy): '))
		if birthdate == '':
			birthdate = None
		else:
			birthdate = datetime.strptime(birthdate, '%m%d%Y')
		birthpalce = input('Birth Place: ')
		if birthplace == '':
			birthplace = None
		address = input('Address: ')
		if address == '':
			address = None
		telnum = input('Phone Number: ')
		if telnum == '':
			telnum = None
		self.cursor.execute('INSERT INTO persons VALUES (:fname,:lname,:bdate,:bplace,:add,:phone)',
	              {"fname":f_name,"lname":l_name,"bdate":birthdate,"bplace":birthplace,"add":address, "phone":telnum})
		self.conn.commit()
		print('Succesfully Added')

	def regimarriage(self):
		valid_entry = False
		while valid_entry == False:
			try:
				for lname, fname, partner in ([p1_lname, p1_fname, 'first'],
						              [p2_lname, p2_fname, 'second']):
					print("Enter the %s partner's information" % (partner))
					fname = input('First Name: ')
					lname = input('Last Name: ')
					 
				#check the person whether or not in the datebase
				self.cursor.execute('''SELECT * FROM persons
				                       WHERE lname = ? AND fname = ?;''', (lname, fname))
	
				if self.cursor.fetchone() == 0: # not in database
					self.addPerson(fname,lname)
	
				#create marriage info
				marr_regno = self.getMarrNo()
				marr_ragdate = date.today()
				marr_regplace = self.user_info[5]
				marriages_info = (marr_regno, marr_regdate, marr_regplace,
						    p1_fname, p1_lname, p2_fname, p2_lname)
				self.cursor.execute(''' INSERT INTO marriages VALUES
					                (?,?,?,?,?,?); ''', marriages_info)
				self.conn.commit()
			except:
				print('Invalid Entry.Please try again')
				decide_continue = input('Entry B to return back to menu OR Press Entry to retry')
				if decide_continue.upper() == 'B':
					break
				else:
					print('Retry inputs.')
	
			else:
				print('Marriage registration completed.')
				valid_entry = True
				self.agent_oper()


		       


	def getMarrNo(self):
    	#create_random_regno
		while True:
			ran_num = random.randint(0,1000000)
			self.cursor.execute('SELECT * FROM marriages WHERE regno =:num',{"num":ran_num})
			val = self.cursor.fetchone()
			if bool(val) == False:
				return(ran_num)


	def renew_vehreg(self):
		valid_entry = False
		while valid_entry == False:
			try:
				regno = int(input('Registration Number: '))
				self.cursor.execute('SELECT * FROM registrations where regno= :regno', {'regno':regno})
				
				old_reg = self.cursor.fetchone()
				expiryDate = old_reg[2]
				old_expiry = datetime.strptime(expiryDate, '%m%d%Y')
				print('Current expiration date: ', old_expiry)
				today = date.today()
				if old_expiry <= today:
					month = today.month
					day = today.day
					year = today.year +1
					new_expiry = date(month,day,year)
		
				elif old_expiry > today:
					month = old_expiry.month
					day = old_expiry.day
					year = old_expiry.year +1
					new_expiry = date(month,day,year)
				    
				#update registration
				self.cursor.execute('UPDATE registrations SET expiry=:new_exp WHERE regno=:reg',
					              {'new_exp':new_expiry, 'reg':regno})
				self.conn.commit()
			except:
				print('Invalid Entry.Please try again')
				decide_continue = input('Entry B to return back to menu OR Press Entry to retry')
				if decide_continue.upper() == 'B':
					break
				else:
					print('Retry inputs.')
	
			else:
				print('Vehicle registration renewed.')
				valid_entry = True
				self.agent_oper()
	def process_sale():
	    car_vin = input("Please input vin of car: ")
	    cur_fn = input("Please input first name of current onwer: ")
	    cur_ln = input("Please input last name of current onwer: ")
	    new_fn = input("Please input first name of new onwer: ")
	    new_ln = input("Please input last name of new onwer: ")
	    get_data = self.cursor.execute('select * from registrations where vin =:vin limit 1', {"vin": car_vin}).fetchall()
	    self.conn.commit() 
	    while  cur_fn.lower() != getdata[0][5].lower:
		print ('Wrong name.')
		cur_fn = input("Please input first name of current onwer: ")
	    while  cur_ln.lower() != getdata[0][6].lower:
		print ('Wrong name.')  # check name
		cur_ln = input("Please input last name of current onwer: ")
	    exp_date = datetime.date(datetime.now())
	    new_date = exp_date.replace(exp_date.year + 1)
	    new_regno= random.randint(100, 9999) # get new regno
	    regno_data = self.cursor.execute('select * from registrations where regno =:regno limit 1', {"regno": new_regno}).fetchall()
	    while regno_data != NUll:
		new_regno= random.randint(100, 9999) # get new regno
		regno_data = cursor.execute('select * from registrations where regno =:regno limit 1', {"regno": new_regno}).fetchall()        
	    old_data = (exp_date, get_data[0][4])
	    self.cursor.execute('update registrations set expiry = ? where vin = ?;', old_date)
	    self.conn.commit() 
	    new_data = (new_regno, exp_date, new_date, get_data[0][3], get_data[0][4], new_fn, new_ln)
	    self.cursor.execute('insert into registrations values(?,?,?,?,?,?);',new_data)
	    self.conn.commit() 
	    choice = 0
		 while choice != "r":
				choice = input("Input r to return menu:")
				if choice = "r":
					self.agent_oper()	
	def process_sale(self):
		car_vin = input("Please input vin of car: ")
		cur_fn = input("Please input first name of current onwer: ")
		cur_ln = input("Please input last name of current onwer: ")
		new_fn = input("Please input first name of new onwer: ")
		new_ln = input("Please input last name of new onwer: ")
		get_data = self.cursor.execute('select * from registrations where vin =:vin limit 1', {"vin": car_vin}).fetchall()
		self.conn.commit() 
		while  cur_fn.lower() != getdata[0][5].lower:
			print ('Wrong name.')
			cur_fn = input("Please input first name of current onwer: ")
		while  cur_ln.lower() != getdata[0][6].lower:
			print ('Wrong name.')  # check name
			cur_ln = input("Please input last name of current onwer: ")
		exp_date = datetime.date(datetime.now())
		new_date = exp_date.replace(exp_date.year + 1)
		new_regno= random.randint(100, 9999) # get new regno
		regno_data = self.cursor.execute('select * from registrations where regno =:regno limit 1', {"regno": new_regno}).fetchall()
		while regno_data != NUll:
			new_regno= random.randint(100, 9999) # get new regno
			regno_data = cursor.execute('select * from registrations where regno =:regno limit 1', {"regno": new_regno}).fetchall()        
			old_data = (exp_date, get_data[0][4])
			self.cursor.execute('update registrations set expiry = ? where vin = ?;', old_date)
			self.conn.commit() 
			new_data = (new_regno, exp_date, new_date, get_data[0][3], get_data[0][4], new_fn, new_ln)
			self.cursor.execute('insert into registrations values(?,?,?,?,?,?);',new_data)
			self.conn.commit() 
		 choice = 0
		 while choice != "r":
				choice = input("Input r to return menu:")
				if choice = "r":
					self.agent_oper()	
	def getAbstract():
	    fname = input("Please input first name: ")
	    lname = input("Please input first name: ")
	    name = (fname, lname)
	    # count lifetime data
	    countTicket_query = "select count(*) from tickets t left outer join registrations r on t.regno = r.regno where fname = ? and lname = ?;"
	    get_data = self.cursor.execute(countTicket_query,name).fetchall()
	    count_ticket = get_data[0][0]

	    countNotice_query  =  "select count(*) from demeritNotices where fname = ? and lname = ?;" 
	    get_data = self.cursor.execute(countNotice_query,name).fetchall()
	    count_Notice = get_data[0][0]

	    countPoints_query = "select sum(points) from demeritNotices where fname = ? and lname = ?;" 
	    get_data = self.cursor.execute(countPoints_query,name).fetchall()
	    count_points = get_data[0][0]  

	    # count last two years data
	    count2Ticket_query = "select count(*) from tickets t left outer join registrations r on t.regno = r.regno where fname = ? and lname = ? and vdate >= DATE('NOW', '-2 YEAR');"
	    get_data = self.cursor.execute(count2Ticket_query,name).fetchall()
	    count2_ticket = get_data[0][0]   

	    count2Notice_query = "select count(*) from demeritNotices where fname = ? and lname = ? and ddate >= DATE('NOW', '-2 YEAR');"
	    get_data = self.cursor.execute(count2Notice_query,name).fetchall()
	    count2_Notice = get_data[0][0]

	    count2Points_query = "select sum(points) from demeritNotices where fname = ? and lname = ? and ddate >= DATE('NOW', '-2 YEAR');"
	    get_data = self.cursor.execute(count2Points_query,name).fetchall()
	    count2_points = get_data[0][0]     
	    self.conn.commit()
	    print("Total tickets count: %d" % count_ticket)
	    print("Total demerit notices count: %d" % count_Notice)
	    print("Total demerit points: %d" %  count_points)
	    print("Past two year tickets count: %d" % count2_ticket )
	    print("Past two year demerit notices count: %d" % count2_Notice)
	    print("Past two year demerit points count: %d" % count2_points)

	    choice = input('Would you like to see the each tickets?(input y to see the detail)')
	    if choice.lower() == 'y':
		display_query = "select tno, vdate, violation, fine, tickets, regno, make, model from tickets t left outer join registrations  r on t.regno = r.regno left outer join vehicles v on v.vin = r.vin where fname = ? and lname = ? order by vdate desc limit 5;"
		get_data = self.cursor.execute(display_query,name).fetchall()
		print(get_data)        
		choice = input('Would you like to see the all tickets?(input y to see the total list)')
		display_query = "select tno, vdate, violation, fine, tickets, regno, make, model from tickets t left outer join registrations  r on t.regno = r.regno left outer join vehicles v on v.vin = r.vin where fname = ? and lname = ? order by vdate desc;"
		get_data = self.cursor.execute(display_query,name).fetchall()
		print(get_data)  
		self.conn.commit()
	   choice = 0
		 while choice != "r":
				choice = input("Input r to return menu:")
				if choice = "r":
					self.agent_oper()

	def Check_info(self, regis_num):
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
		    
	def Issue_ticket(self, regis_num):
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
		self.conn.commit()
	    
	def Question8(self):
		while True:
			try:   
				regis_num = input('Provide the registration number:')
				regis_num = int(regis_num)
			except:
				print('Registration number is integer!')
				self.cursor.execute("select * from registrations where regno = ?",(regis_num,))
				finding = self.cursor.fetchall()
				if len(finding) == 0:
					print('Wrong registration number!')
					self.Question8()
					self.Check_info(regis_num)
					self.Issue_ticket(regis_num)
					quit_string = input('Would you like to return to the menu(Y/N):')
					if quit_string.upper() == 'Y':
						print('Returning to the menu...')
						break
					if quit_string.upper() == 'N':
						pass
					else:
						print('Wrong input!')
						
						
	def Null_check(self, car_make, car_model, car_color, car_year, car_plate, part_sql):
		Full_sql = "Select distinct v.make, v.model, v.color, v.year, r.plate From registrations r, vehicles v Where r.vin = v.vin "
		if car_make != 'null':
			part_sql = part_sql + 'and v.make = ' + '"' + str(car_make) + '"'
		if car_model != 'null':
			part_sql = part_sql + 'and v.model = ' + '"' + str(car_model) + '"'
		if car_color != 'null':
			part_sql = part_sql + 'and v.color = ' + '"' + str(car_color) + '"'
		if car_year != 'null':
			part_sql = part_sql + 'and v.year = ' + '"' + str(car_year) + '"'
		if car_plate != 'null':
			part_sql = part_sql + 'and r.plate = ' + '"' + str(car_plate) + '"'
		Full_sql = Full_sql + part_sql + ";"
		return Full_sql, part_sql
		
	def search_info(part_sql):
		while True:
			car_make = input('Provide the make of car:')
			car_model = input('Provide the model of car:')
			car_color = input('Provide the color of car:')
			car_year = input('Provide the year of car:')
			car_plate = input('Provide the plate of car:')
			Full_sql, part_sql = self.Null_check(car_make, car_model, car_color, car_year, car_plate, part_sql)
			self.cursor.execute(Full_sql)
			rows = self.cursor.fetchall()
			if len(rows) == 0:
				print('Can not find the information!')
				break
			self.Results(rows, part_sql, part_sql_2)
		    
	def Results(self, rows, part_sql, part_sql_2):
		full_sql_2 = 'Select distinct v.make, v.model, v.color, v.year, r.plate, r.regdate, r.expiry, r.fname||r.lname From registrations r, vehicles v Where r.vin = v.vin ' 
	    
		if len(rows) >= 4:
			for row in rows:
				print(row)
			select_list.append(info)
			Full_sql, part_sql_2 = Null_check(select_list[0], select_list[1], select_list[2], select_list[3], select_list[4], part_sql_2)
			full_sql_2 = full_sql_2 + part_sql_2
			self.cursor.execute(full_sql_2)
			result = self.cursor.fetchall()
			print(result)
		
		if len(rows) < 4 and len(rows) > 0:
			full_sql_2 = full_sql_2 + part_sql
			self.cursor.execute(full_sql_2)
			result = self.cursor.fetchall()
			print(result)
		
	def Question9():
		while True:
			search_info(part_sql)
			quit_string = input('Whould yuu like to return to the menu?(Y/N):')
			if quit_string.upper() == 'Y':
				break
			if quit_string.upper() == 'N':
				pass
			else:
				print('Wrong Input!')

main()
