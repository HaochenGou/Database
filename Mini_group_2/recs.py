from bsddb3 import db
import xml.sax
import re

class p_data(xml.sax.ContentHandler):
	def __init__(self):
		self.data = ''
		self.row = ''
		self.subj = ''
		self.body = ''
		self.mail = ''
		self.email = ''
	
		
	def startElement(self,name,attrs):
		self.data = name
		#if name == 'emails':
			#self.email = attrs['type']
		if self.data == 'mail':
			self.mail = content
			file = open('recs.txt','a')
			file.write(self.mail)
			self.mail = ''		
			
	def characters(self,content):
		if self.data == 'mail':
			self.mail = content
			file = open('recs.txt','a')
			file.write(self.mail)
			self.mail = ''			
			
		
	
				
	def endElement(self,name):	
		
		self.data = ''
			
						
						
					
		


file_name =  input("Please in input correct file name: ")
get_file = xml.sax.make_parser()
get_file.setFeature(xml.sax.handler.feature_namespaces,0)
handler = p_data()
get_file.setContentHandler(handler)
get_file.parse(file_name)