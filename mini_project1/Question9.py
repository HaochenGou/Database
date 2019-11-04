import sqlite3

connection = None
cursor = None
conn = sqlite3.connect('./a2.db')
part_sql = ''
part_sql_2 = ''
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
        
def search_info(self, part_sql):
    car_make = input('Provide the make of car:')
    car_model = input('Provide the model of car:')
    car_color = input('Provide the color of car:')
    car_year = input('Provide the year of car:')
    car_plate = input('Provide the plate of car:')
    Full_sql, part_sql = Null_check(car_make, car_model, car_color, car_year, car_plate, part_sql)
    self.cursor.execute(Full_sql)
    rows = self.cursor.fetchall()
    Results(rows, part_sql, part_sql_2)
    
def Results(self, rows, part_sql, part_sql_2):
    full_sql_2 = 'Select distinct v.make, v.model, v.color, v.year, r.plate, r.regdate, r.expiry, r.fname||r.lname From registrations r, vehicles v Where r.vin = v.vin ' 
    
    if len(rows) >= 4:
        for row in rows:
            print(row)
        selected_num = input('Provide the num you want to selected:')
        selected_info = rows[int(selected_num) - 1]
        select_list = []
        for info in selected_info:
            select_list.append(info)
        Full_sql, part_sql_2 = Null_check(select_list[0], select_list[1], select_list[2], select_list[3], select_list[4], part_sql_2)
        full_sql_2 = full_sql_2 + part_sql_2
        self.cursor.execute(full_sql_2)
        result = self.cursor.fetchall()
        print(result)
        
    if len(rows) < 4:
        c = conn.cursor()
        full_sql_2 = full_sql_2 + part_sql
        self.cursor.execute(full_sql_2)
        result = self.cursor.fetchall()
        print(result)
        
def Question9(self):
    self.search_info(part_sql)
main()
