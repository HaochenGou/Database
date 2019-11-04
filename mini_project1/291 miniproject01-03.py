import sys
import sqlite3
import datetime
from random import randint

 def __register_birth(self):
        valid_inputs = False
        while not valid_inputs:
            try:
                # Gather mother's info
                m_f_name = input("Mother's first name: ")
                m_l_name = input("Mother's last name: ")
                self.__cursor.execute('SELECT * FROM persons WHERE fname like :mfname and lname like :mlname',
                                      {'mfname': m_f_name, 'mlname': m_l_name})
                mother_info = self.__cursor.fetchall()
                if len(mother_info) > 0:
                    assert len(mother_info) == 1
                    print("Found mother's info in system.")
                    address = mother_info[0][4]
                    phone = mother_info[0][5]
                else:
                    # registering mother's info into persons table
                    print("Must add mother's info into system: ")
                    mbdate_str = input("Mother's birthdate (MMDDYYYY): ")
                    if mbdate_str == '':
                        mbdate = None
                    else:
                        mbdate = datetime.strptime(mbdate_str, '%m%d%Y')
                    mbplace = input("Mother's birth city: ")
                    if mbplace == '':
                        mbplace = None
                    maddress = input("Mother's Address: ")
                    if maddress == '':
                        maddress = None
                    address = maddress
                    mphone = input("Mother's Phone Number: ")
                    if mphone == '':
                        mphone = None
                    phone = mphone
                    m_person_reg = (m_f_name, m_l_name, mbdate, mbplace, maddress, mphone)
                    self.__cursor.execute('INSERT INTO persons values (?,?,?,?,?,?)', m_person_reg)
                    self.__conn.commit()
                    print("Successfully added mother's info into system.")
                    print("Continuing to gather info to register birth.")

                # Gather father's info
                f_f_name = input("Father's first name: ")
                f_l_name = input("Father's last name: ")
                self.__cursor.execute('SELECT * FROM persons WHERE fname like :ffname and lname like :flname',
                                      {'ffname': f_f_name, 'flname': f_l_name})
                father_info = self.__cursor.fetchall()
                if len(father_info) > 0:
                    assert len(father_info) == 1
                    print("Found fathers's info in system.")
                else:
                    # Registering father's info into persons table
                    print("Must add fathers's info into system: ")
                    fbdate_str = input("Fathers's birthdate (MMDDYYYY): ")
                    if fbdate_str == '':
                        fbdate= None
                    else:
                        fbdate = datetime.strptime(fbdate_str, '%m%d%Y')
                    fbplace = input("Fathers's birth city: ")
                    if fbplace == '':
                        fbplace = None
                    faddress = input("Fathers's Address: ")
                    if faddress == '':
                        faddress = None
                    fphone = input("Fathers's Phone Number: ")
                    if fphone == '':
                        fphone = None
                    f_person_reg = (f_f_name, f_l_name, fbdate, fbplace, faddress, fphone)
                    self.__cursor.execute('INSERT INTO persons values (?,?,?,?,?,?)', f_person_reg)
                    self.__conn.commit()
                    print("Successfully added fathers's info into system.")
                    print("Continuing to gather info to register birth.")

                # Gather birth information
                f_name = input('First Name: ')
                assert len(f_name) > 0
                l_name = input('Last Name: ')
                assert len(l_name) > 0
                gender = input('Gender (m/f): ')
                assert len(gender) == 1
                assert gender.upper() == 'M' or gender.upper() == "F"
                # NEED TO CONFIRM DATE INPUT CONVERSION TO SQLITE DATE OBJECT
                birthdate_str = input('Birthdate (MMDDYYYY): ')
                birthdate = datetime.strptime(birthdate_str, '%m%d%Y')
                birthplace = input('Birth Place: ')
                reg_location = self.__user_info[5]
                reg_date = date.today()

                self.__cursor.execute('SELECT max(regno) FROM births')
                new_regno = self.__cursor.fetchall()[0][0] + 1

                birth = (new_regno, f_name, l_name, reg_date, reg_location,
                         gender, f_f_name, f_l_name, m_f_name, m_l_name)
                person = (f_name, l_name, birthdate,
                          birthplace, address, phone)
                self.__cursor.execute(
                    'insert into persons values (?,?,?,?,?,?)', person)
                self.__cursor.execute(
                    'insert into births values (?,?,?,?,?,?,?,?,?,?)', birth)
                self.__conn.commit()

            except:
                print('Invalid Entry.')
                next_step = input("Type 'C' to cancel, or any other key to retry: ")
                if next_step.upper() = 'C':
                    print('Returning to user menu.')
                    break
                else:
                    print('Retry inputs.')

            else:
                print('Successfully registered birth/person.')
                print('Returning to user menu.')
                valid_inputs = True

        return None

    def __register_marriage(self):
        print("Registering a marriage...")

        p1_fname, p1_lname = "", ""
        p2_fname, p2_lname = "", ""

        for lname, fname, partner in ([p1_lname, p1_fname, "first"],
                                      [p2_lname, p2_fname, "second"]):
            print("Enter the %s partner's information" % (partner))
            lname = input("\tLast Name: ")
            fname = input("\tFirst Name: ")

            fname, lname = self.__enter_valid_name()

            # check if the person exists in the database.
            self.__cursor.execute('''SELECT * FROM persons
                                     WHERE lname=? AND fname=?;''', (lname, fname))

            if self.__cursor.fetchone() == 0:
                # person not in database; enter the info required.
                # currently creates a new row in the persons table. **Should it?**
                print("Person not found! Create a new entry...")
                bdate = input("Birthdate (MMDDYYYY): ")
                bplace = input("Birth Place: ")
                address = input("Address: ")
                phone = input("Phone Number: ")
                persons_insert = (lname, fname, bdate, bplace, address, phone)
                self.__cursor.execute(''' INSERT INTO persons VALUES
                                            (?,?,?,?,?,?); ''', persons_insert)

        # Create a marriage entry for the two partners.
        self.__cursor.execute('SELECT max(regno) FROM marriages')
        regno = self.__cursor.fetchone() + 1

        # inserted valus: (regno, regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname)
        marriages_insert = (regno, date.today(), self.__user_info[5],
                            p1_fname, p1_lname, p2_fname, p2_lname)
        self.__cursor.execute(''' INSERT INTO marriages VALUES
                                (?,?,?,?,?,?); ''', marriages_insert)

        self.__conn.commit()

        print("Marriage successfully registered!")


    def __renew_registration(self):
        valid_inputs = False
        while not valid_inputs:
            try:
                print('Renewing Registration...')
                regno = int(input('Registration number: '))
                self.__cursor.execute('SELECT * FROM registrations where regno= :regno', {'regno':regno})
                current_reg = self.__cursor.fetchone()
                current_expiry = current_reg[2]
                print('Current expiration date: ', current_expiry)
                if current_expiry <= date.today():
                    new_expiry = date.today()
                    new_expiry = new_expiry.replace(new_expiry.year + 1)
                elif current_expiry > date.today():
                    new_expiry = current_expiry.replace(current_expiry.year + 1)
                self.__cursor.execute('UPDATE registrations SET expiry=:new_exp WHERE regno=:reg',
                                      {'new_exp':new_expiry, 'reg':regno})
                self.__conn.commit()
            except:
                print('Invalid registration number. Registration not renewed.')
                retry_entry = input("Type 'C' to cancel task. Enter any other key to retry: ")
                if retry_entry.upper() = 'C':
                    print('Returning to user menu.')
                    break
                else:
                    print('Retry input.')
            else:
                print('Successfully renewed registration.')
                print('Returning to user menu.')
                valid_inputs = True