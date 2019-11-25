from bsddb3 import db
import re

def main():
    emails = db.DB()
    emails.open('em.idx')
    curs_em = emails.cursor()
    result = []
    Search_From(curs_em, result)

def Search_From(curs_em, result):
    first = curs_em.first()
    next_line = curs_em.next()
    while next_line != None:
        next_line = curs_em.next()
        if next_line != None:
                string = next_line[0].decode('utf-8')
                if string.startswith("to-kenneth.shulklapper@enron.com")or string.startswith( "to-keith.holst@enron.com"):
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
                    if not string.startswith("to-kenneth.shulklapper@enron.com")or string.startswith( "to-keith.holst@enron.com"):
                        print(next_line)

main()