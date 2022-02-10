import docx
import re
from docx import Document

document = docx.Document('data.docx')

docdata = []
for docpara in document.paragraphs:
    docdata.append(docpara.text)

docstring = ' ' .join(docdata)
#print(docstring)


#std_list_raw = re.findall(r'[E][N]\s\d{3,5}\s\-\s\w.+[^.]', docstring)
#en_description_final =  []
#for item in std_list_raw:
#    en_description_final.append(item.strip())
#en_description_final = list(dict.fromkeys(en_description_final))
#print(en_description_final)

#std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}\s\-\s\w.+[^.]', docstring)
#iec_description_final = []
#for item in std_list_raw:
#    iec_description_final.append(item.strip())
#print(iec_description_final)

std_list_raw = re.findall(r'[E][N]\s\d{3,5}', docstring)
en_list_final =  []
for item in std_list_raw:
    en_list_final.append(item.strip())
en_list_final = list(dict.fromkeys(en_list_final))
print(en_list_final)

std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}', docstring)
iec_list_final = []
for item in std_list_raw:
    iec_list_final.append(item.strip())
iec_list_final = list(dict.fromkeys(iec_list_final))
print(iec_list_final)

