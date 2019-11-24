from bsddb3 import db
import re

def main():
    emails = db.DB()
    emails.open('em.idx')
    curs_em = emails.cursor()
    Search_From(curs_em)

def Search_From(curs_em):
    first = curs_em.first()
    next_line = curs_em.next()
    while next_line != None:
        next_line = curs_em.next()
        if next_line != None:
                string = next_line[0].decode('utf-8')
                if string.startswith('from-phillip.allen@enron.com'):
                    result = curs_em.set(next_line[1])
                    
main()