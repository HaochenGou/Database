from bsddb3 import db
import re


def main():
records = db.DB()
emails = db.DB()
dates = db.DB()
terms = db.DB()
records.open('re.idx')
emails.open('em.idx')
dates.open('da.idx')
terms.open('te.idx')
result = []

curs_re = records.cursor()
curs_te = terms.cursor()
curs_em = emails.cursor()
curs_da = dates.cursor()

emails_on_date(curs_da)
emails_after_date(curs_da)
emails_with_bcc_cc(curs_em, result)
emails_with_terms_and_date(curs_re, curs_te, curs_da)


def emails_on_date(curs_da): #7 exact search
    date = input('Please enter the date: ')
    result = curs_da.set(str(date))
    print(result[1].decode('utf-8'))
    
    

def emails_after_date(curs_da): #8 range search
    while True:
        start_date = input('Please enter the date: ')
        result = curs.set_range(start_date.encode('utf-8'))
        
        if result != None:
            print('Found dates: ')
            while result != None:
                print('Date: ' + str(result[0].decode('utf-8'))')
                result = curs.next()
        else:
            print('No date was found')
            
            
def emails_with_bcc_cc(curs_em, result):  #9 multiple condition
    bcc_add = input('Enter the bcc address:(example:bcc-derryl.cleaveland@enron.com) ')
    cc_add = input('Enter the cc address:(example:cc-jennifer.medcalf@enron.com')
    first = curs_em.first()
    next_line = curs_em.next()
    while next_line != None:
        next_line = curs_em.next()
        if next_line != None:
                string = next_line[0].decode('utf-8')
                if string.startswith(str(bcc_add)) and string.startswith(str(cc_add)):
                    result.append(next_line)
    Match_email(result, curs_em)
    
def Match_email(result, curs_em):
    for line in result:
        row = line[1].decode('utf-8')
        first = curs_em.first()
        next_line = curs_em.next()
        while next_line != None:
            next_line = curs_em.next()
            if next_line != None:
                if next_line[1].decode('utf-8') == row:
                    string = next_line[0].decode('utf-8')
                    if not  string.startswith(str(bcc_add)) and string.startswith(str(cc_add)):
                        print(next_line)

    

def emails_with_terms_and_date(curs_re, curs_te, curs_da): #10 range search + multiple condition
   
    


def display_options():
    print("Select one of the following queries to proccess (0 to exit)")
    print("1 Email with subject")
    print("2 email with subject and body")
    print("3 email with prefix")
    print("4 email from")
    print("5 email to")
    print("6 email with two recipients")
    print("7 email on date")
    print("8 email after date")
    print("9 email with bcc and cc")
    print("10 email with term and before date")

queries = {1:emails_with_subject, 2:emails_with_subject_and_body, 3:emails_with_prefix, 4:emails_from, 5:emails_to, 
           6:emails_with_to_and_to, 7:emails_on_date, 8:emails_after_date, 9:emails_with_bcc_cc, 10:emails_with_terms_and_date}


