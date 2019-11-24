from bsddb3 import db
import re

#########   Not have confidential in the 10.xml ############
#########   NNED FOR LOOP  ################

def main():
    records = db.DB()
    terms = db.DB()
    records.open('re.idx')
    terms.open('te.idx')
    curs_re = records.cursor()
    curs_te = terms.cursor()
    Search_confident(curs_re, curs_te)
    
def Search_confident(curs_re, curs_te):
    first = curs_te.first()
    dup = curs_te.next()
    while dup != None:
        dup = curs_te.next()
        if dup != None:
            string = dup[0].decode('utf-8')
            if string.startswith('b-here') or string.startswith('s-here'):
                clue = dup[1].decode('utf-8')
                result = curs_re.set(dup[1])
                print(clue)
                print(result[1].decode('utf-8'))     
main()