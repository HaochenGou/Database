from bsddb3 import db
import re

#########   Not have earnings in the 10.xml ############

def main():
    records = db.DB()
    terms = db.DB()
    records.open('re.idx')
    terms.open('te.idx')
    curs_re = records.cursor()
    curs_te = terms.cursor()
    Search_subj_body(curs_re, curs_te)
    
def Search_subj_body(curs_re, curs_te):
    gas_sear = curs_te.set(b's-gas')
    if gas_sear != None:
        earning_sear = curs_te.set(b'b-expiration')
        print(earning_sear[1].decode('utf-8'))
        result = curs_re.set(earning_sear[1])
        print(result[1].decode('utf-8'))
    
main()