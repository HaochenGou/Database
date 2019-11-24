from bsddb3 import db
import re

def main():
    records = db.DB()
    terms = db.DB()
    records.open('re.idx')
    terms.open('te.idx')
    curs_re = records.cursor()
    curs_te = terms.cursor()
    searching_subj(curs_re, curs_te)
    
def searching_subj(curs_re, curs_te):
    row = curs_te.set(b's-gas')
    print(row[1].decode('utf-8'))
    result = curs_re.set(row[1])
    print(result[1].decode('utf-8'))

main()