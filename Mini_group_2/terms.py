from bsddb3 import db
import xml.sax
import re

class p_data(xml.sax.ContentHandler):
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
			content.split(' ')
			self.subj = re.findall(r'[0-9a-zA-Z_-]+',content)
			file = open('terms.txt','a')
			if len(self.subj) != 0:
				for a in self.subj:
					if len(a) > 2:
						file.write('s-')
						file.write(a.lower())
						file.write(':')
						file.write(self.row +'\n')
						self.subj = ''			
			
		elif self.data == 'body':
			content.split(' ')
			self.body = re.findall(r'[0-9a-zA-Z_-]+',content)
			file = open('terms.txt','a')
			if len(self.body) != 0:
				for a in self.body:
					if len(a) > 2:
						file.write('b-')
						file.write(a.lower())
						file.write(':')
						file.write(self.row +'\n')
						self.body = ''			
	
				
	def endElement(self,name):	
		
		self.data = ''
			
						
						
					
		


file_name =  input("Please in input correct file name: ")
get_file = xml.sax.make_parser()
get_file.setFeature(xml.sax.handler.feature_namespaces,0)
handler = p_data()
get_file.setContentHandler(handler)
get_file.parse(file_name)