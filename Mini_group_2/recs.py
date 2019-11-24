import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
tree = ET.parse('10.xml')
root = tree.getroot()

list_infor = []
body = ''
for i in root[0]:
    start = '<' + str(i.tag) + '>'
    if i.text == None:
        i.text = ''
    result = escape(str(i.text),{"\n":"$#10;"})
    end = '<' + str(i.tag) + '/>'
    body = body + str(start + result + end)
full_information = '<mail>' + str(body) + '<mail/>'
print(full_information)

file = open('111.txt','w')
file.write(full_information)
    

