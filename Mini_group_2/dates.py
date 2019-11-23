from bsddb3 import db
import xml.sax
import re

class p_data(xml.sax.ContentHandler):
	def __init__(self):
		self.data = ''
		self.row = ''
		self.date = ''
		
	def startElement(self,name,attrs):
		self.data = name	

	def characters(self,content):
		if self.data == 'row':
			self.row = content
			
		elif self.data == 'date':
			self.date = re.findall(r'[0-9/]+',content)
			file = open('dates.txt','a')
			if len(self.date) != 0:
				for a in self.date:
					file.write('d-')
					file.write(a)
					file.write(':')
					file.write(self.row +'\n')
					self.date = ''			
			
		
	
				
	def endElement(self,name):	
		
		self.data = ''
			
						
						
					

file_name =  input("Please in input correct file name: ")
get_file = xml.sax.make_parser()
get_file.setFeature(xml.sax.handler.feature_namespaces,0)
handler = p_data()
get_file.setContentHandler(handler)
get_file.parse(file_name)