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
		self.connection = None 
		self.conn = None #sqlite3.connect('./test.db')
		self.app_continue = True
		self.valid_login = False
		self.run()

	def run(self):
		while self.app_continue:
			self.login()
			while self.valid_login:
				if self.utype == 'a':
					self.agent_oper()
				elif self.utype == 'o':
					self.officer_oper()
				# exception invalid input
			print('\n''Logged Out')
		print('\n''Exited')

	def login(self):
		while self.app_continue and self.valid_login = False:
			print('\n''Please enter the valid user id and password to login.')
			uid = input('User Id: ')
			pwd = imput('Password: ')
			#password 

	def exit(self):
		pass

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
        elif option.upper() = 'L':
        	self.valid_login = False
        elif option.upper() = 'E':
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
        elif option.upper() = 'L':
        	self.valid_login = False
        elif option.upper() = 'E':
        	self.valid_login = False
        	self.app_continue = False
        else:
        	print('\n''Invalid Input. Please try again.') 
        	self.officer_oper()

	def regbirth(self):
		valid_entry = False
        while valid_entry = False:
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
		         self.connection.commit()

		    except:
		    	print('Invalid Entry.Please try again')
		    	decide_continue = input('Entry B to return back to menu OR Press Entry to retry')
                if decide_continue.upper() = 'B':
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
        if bool(val) = False:
            return(ran_num)

    def addPerson(self,f_name,l_name):
    	print(f_name + ' ' + l_name + 'is not found. Please fill out the related inforation to complete')
	    birthdate = str(input('Birth Date (mmddyyyy): '))
	    if birthdate = '':
	    	birthdate = None
	    else:
	    	birthdate = datetime.strptime(birthdate, '%m%d%Y')
	    birthpalce = input('Birth Place: ')
	    if birthplace = '':
	    	birthplace = None
	    address = input('Address: ')
	    if address = '':
	    	address = None
	    telnum = input('Phone Number: ')
	    if telnum = '':
	    	telnum = None
	    self.cursor.execute('INSERT INTO persons VALUES (:fname,:lname,:bdate,:bplace,:add,:phone)',
	              {"fname":f_name,"lname":l_name,"bdate":birthdate,"bplace":birthplace,"add":address, "phone":telnum})
	    connection.commit()
	    print('Succesfully Added')

	def regimarriage(self):
		valid_entry = False
        while valid_entry = False:
            try:
				for lname, fname, partner in ([p1_lname, p1_fname, 'first'],
		                                      [p2_lname, p2_fname, 'second']):
					print("Enter the %s partner's information" % (partner))
				    fname = input('First Name: ')
				    lname = input('Last Name: ')
				 
			    #check the person whether or not in the datebase
			    self.cursor.execute('''SELECT * FROM persons
		                                     WHERE lname = ? AND fname = ?;''', (lname, fname))

			    if self.__cursor.fetchone() == 0: # not in database
			    	self.addPerson(fname,lname)

			    #create marriage info
				marr_regno = self.getMarrNo()
				marr_ragdate = date.today()
				marr_regplace = self.user_info[5]
				marriages_info = (marr_regno, marr_regdate, marr_regplace,
		                            p1_fname, p1_lname, p2_fname, p2_lname)
		        self.__cursor.execute(''' INSERT INTO marriages VALUES
		                                (?,?,?,?,?,?); ''', marriages_info)
		        self.__conn.commit()
		    except:
		    	print('Invalid Entry.Please try again')
		    	decide_continue = input('Entry B to return back to menu OR Press Entry to retry')
                if decide_continue.upper() = 'B':
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
        if bool(val) = False:
            return(ran_num)


	def renew_vehreg(self):
		valid_entry = False
        while valid_entry = False:
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
                if decide_continue.upper() = 'B':
                    break
                else:
                    print('Retry inputs.')

		    else:
		    	print('Vehicle registration renewed.')
		    	valid_entry = True
		    	self.agent_oper()

main()