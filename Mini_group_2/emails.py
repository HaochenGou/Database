from bsddb3 import db
import xml.sax
import re

class p_data(xml.sax.ContentHandler):
	def __init__(self):
		self.data = ''
		self.row = ''
		self.e_from = ''
		self.e_to = ''
		self.cc = ''
		self.bcc = ''
		
	def startElement(self,name,attrs):
		self.data = name	

	def characters(self,content):
		if self.data == 'row':
			self.row = content
			
		elif self.data == 'from':
			self.e_from = content	
			file = open('emails.txt','a')
			if len(self.e_from) != 0:
				file.write('from-')
				file.write(self.e_from.lower())
				file.write(':')
				file.write(self.row +'\n')
				self.e_from = ''			
			
		elif self.data == 'to':
			self.e_to = content
			file = open('emails.txt','a')
			if len(self.e_to) != 0:
				file.write('to-')
				file.write(self.e_to.lower())
				file.write(':')
				file.write(self.row +'\n')
				self.e_to = ''	
				
		elif self.data == 'cc':	
			self.cc = content
			file = open('emails.txt','a')
			if len(self.cc) != 0:
				file.write('cc-')
				file.write(self.cc.lower())
				file.write(':')
				file.write(self.row +'\n')
				self.cc = ''	
					
		elif self.data == 'bcc':
			self.bcc = content
			file = open('emails.txt','a')
			if len(self.bcc) != 0:
				file.write('bcc-')
				file.write(self.bcc.lower())
				file.write(':')
				file.write(self.row +'\n')
				self.bcc = ''		
	
				
	def endElement(self,name):	
		
		self.data = ''
			
						
						
					
		


file_name =  input("Please in input correct file name: ")
get_file = xml.sax.make_parser()
get_file.setFeature(xml.sax.handler.feature_namespaces,0)
handler = p_data()
get_file.setContentHandler(handler)
get_file.parse(file_name)