import docx
import re
from docx import Document

document = docx.Document('data.docx')

docdata = []
for docpara in document.paragraphs:
    docdata.append(docpara.text)

docstring = ' ' .join(docdata)
#print(docstring)


std_list_raw = re.findall(r'[E][N]\s\d{3,8}\s-[\s\w]+(?=[\s.?!])[^.?!]*[.?!]', docstring)
en_description_final =  []
for item in std_list_raw:
    en_description_final.append(item.strip())
en_description_final = list(dict.fromkeys(en_description_final))
print(en_description_final)

std_list_raw = re.findall(r'[^.?!]*(?<=[.?\s!])IEC(?=[\s.?!])[^.?!]*[.?!]', docstring)
iec_description_final = []
for item in std_list_raw:
    iec_description_final.append(item.strip())
print(iec_description_final)