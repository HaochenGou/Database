import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
file_name =  input("Please in input correct file name: ")
tree = ET.parse(file_name)
root = tree.getroot()

list_infor = []
body = ''
for h in root:
    for i in h:
        row = h[0].text
        start = '<' + str(i.tag) + '>'
        if i.text == None:
            i.text = ''
        result = escape(str(i.text),{"&":"&amp;","\n":"&#10;","<":"&lt;",">":"&gt;","'":"&apos;",'"': "&quot;"})
        end = '<' + str(i.tag) + '/>'
        body = body + str(start + result + end)
    full_information = str(row)+':'+'<mail>' + str(body) + '<mail/>'
    file = open('recs.txt','a')
    file.write(full_information)
    file.write("\n")
    file.close()       

