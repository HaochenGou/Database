from bsddb3 import db
import re

def main():
    te = db.DB()
    da = db.DB()
    re = db.DB()
    em = db.DB()
    te.open("te.idx")
    da.open("da.idx")
    re.open("re.idx")
    em.open("em.idx")
    quit = False
    query = ''
    while not quit and query == '':
        query= input("please input the query(body for 'b-', subject for 's-', from for 'from-',date for 'd-',):")
        query = query.lower()
        #query = bytes(query,'utf-8')
        if query == 'exit':
            quit = True
        else:
            c = command(query,te,da,re,em)   
            c.check()
  
    
class command:
    def __init__(self,query,te,da,re,em):
        self.query = query
        self.curs_re = re.cursor()
        self.curs_te = te.cursor()
        self.curs_da = da.cursor()
        self.curs_em = em.cursor()  
        self.result = []    
    def opt(self):   
        if re.match("output=full",self.query):
            full_print(query,curs_re, curs_te)
        elif re.match("output=brief",query):
            brief_print(query,curs_re, curs_te)
    def check(self):
        compare = ''
        query = self.query.split(' ')
        for a in query:
            b = a.split(':')    
            if re.match("sub",b[0]):
                clue = bytes(b[1], 'utf-8')
                self.searching_subj(clue)                
            elif re.match("body", b[0]):
                self.search_subj_body()
            elif re.match("from",b[0])or re.match("to",b[0]):    
                info = b[1]
                self.Search_address(info)
            elif re.match("to",b[0]):
                pass
            elif re.match("bcc",b[0]) or re.match("cc",b[0]):
                clue = b[1]
                self.emails_with_bcc_or_cc(clue)
            elif re.match("cc",b[0]):
                pass
                
            elif re.match("date",b[0]):
                date = bytes(b[1],'utf-8')
                self.emails_on_date(date)
            else:
                info = b[0]
                self.search_confident(info)
                            
    def searching_subj(self,clue):
        row = self.curs_te.set(clue)
        print(row)
        result = self.curs_re.set(row[1])
        print(result[1].decode('utf-8'))
                
    def search_subj_body(self):
        gas_sear = self.curs_te.set(b's-gas')
        if gas_sear != None:
            earning_sear = self.curs_te.set(b'b-expiration')
            print(earning_sear[1].decode('utf-8'))
            result = self.curs_re.set(earning_sear[1])
            print(result[1].decode('utf-8'))
            
    def search_confident(self,info):
        first = self.curs_te.first()
        dup = self.curs_te.next()
        while dup != None:
            dup = self.curs_te.next()
            if dup != None:
                string = dup[0].decode('utf-8')
                if string.startswith('s-'+ info) or string.startswith('b-' + info):
                    clue = dup[1].decode('utf-8')
                    result = self.curs_re.set(dup[1])
                    print(clue)
                    print(result[1].decode('utf-8')) 
                    
    def Search_address(self,info):
        first = self.curs_em.first()
        next_line = self.curs_em.next()
        while next_line != None:
            next_line = self.curs_em.next()
            if next_line != None:
                    string = next_line[0].decode('utf-8')
                    if string.startswith(info):
                        self.result.append(next_line)
        self.Match_email(info)
                        
    def Match_email(self,info):
        for line in self.result:
            row = line[1].decode('utf-8')
            first = self.curs_em.first()
            next_line = self.curs_em.next()
            while next_line != None:
                next_line = self.curs_em.next()
                if next_line != None:
                    if next_line[1].decode('utf-8') == row:
                        string = next_line[0].decode('utf-8')
                        if not string.startswith(info):
                            print(next_line)
                            
    def emails_on_date(self,date): #7 exact search
        result = self.curs_da.set(date)
        first = self.curs_em.first()
        next_line = self.curs_em.next()
        while next_line != None:
            next_line = self.curs_em.next()
            if next_line != None:
                if next_line[1].decode('utf-8') == result[1].decode('utf-8'):
                    print(next_line[0])
        
        
    '''def emails_after_date(self,date): #8 range search
        while True:
            result = curs.set_range(start_date.encode('utf-8'))
            
            if result != None:
                print('Found dates: ')
                while result != None:
                    print('Date: ' + str(result[0].decode('utf-8')))
                    result = curs.next()
            else:
                print('No date was found')'''
        
    def emails_with_bcc_or_cc(self,clue): #9 multiple condition
        first = self.curs_em.first()
        next_line = self.curs_em.next()
        while next_line != None:
            next_line = self.curs_em.next()
            if next_line != None:
                    string = next_line[0].decode('utf-8')
                    if string.startswith(clue):
                        self.result.append(next_line)
        self.Match_email(clue)
                        
                
#2,6,8,9,10 unfinished
#quit unfinished
main()
