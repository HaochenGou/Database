from bsddb3 import db
import xml.sax.handler
import re

class p_data(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.data = ''
		self.row = ''
		self.subj = ''
		self.body = ''
		self.recs = ''
		
	
		
	def startElement(self,name,attrs):
		self.data = name		
		
	def characters(self,content):
		if self.data == 'row':
			self.row = content
		elif self.data == 'subj':
			self.subj = content
		elif self.data == 'body':
			self.body = content
				
	def endElement(self,name):
		if self.subj == '':
			if self.data == 'body':
				new_list = self.body.split(' ')
				file = open('terms.txt','a')
				for a in new_list:
					b = re.findall(r'[0-9a-zA-Z_-]+',a)
					if len(b) > 0:
						for c in b:
							if len(c) > 2:
								file.write('b-')
								file.write(c.lower())
								file.write(':')
								file.write(self.row +'\n')
								self.body = ''	
		else:						
			if self.data == 'subj':
				new_list = self.subj.split(' ')
				file = open('terms.txt','a')
				for i in new_list:
					h = re.findall(r'[0-9a-zA-Z_-]+',i)
					if len(h) > 0:
						for f in h:
							if len(f) > 2:
								file.write('s-')
								file.write(f.lower())
								file.write(':')
								file.write(self.row +'\n')
								self.subj = ''
			elif self.data == 'body':
				new_list = self.body.split(' ')
				file = open('terms.txt','a')
				for a in new_list:
					b = re.findall(r'[0-9a-zA-Z_-]+',a)
					if len(b) > 0:
						for c in b:
							if len(c) > 2:
								file.write('b-')
								file.write(c.lower())
								file.write(':')
								file.write(self.row +'\n')
								self.body = ''	
		
		self.data = ''
		
						
						
					
		


file_name =  input("Please in input correct file name: ")
get_file = xml.sax.make_parser()
handler = p_data()
get_file.setContentHandler(handler)
get_file.parse(file_name)