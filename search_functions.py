import docx
import re
from docx import Document

document = docx.Document('data.docx')

docdata = []
for docpara in document.paragraphs:
    docdata.append(docpara.text)

docstring = ' ' .join(docdata)
#print(docstring)


#This section searches for the EN standard name and title
#std_list_raw = re.findall(r'IS\s\d{3,8}\s-[\s\w]+(?=[\s.?!])[^.?!]*[.?!]', docstring)
#en_description_final =  []
#for item in std_list_raw:
#    en_description_final.append(item.strip())
#en_description_final = list(dict.fromkeys(en_description_final))
#print(en_description_final)


#This section searches for any sentence containgin the word IEC
#std_list_raw = re.findall(r'[^.?!]*(?<=[.?\s!])IEC(?=[\s.?!])[^.?!]*[.?!]', docstring)
#iec_description_final = []
#for item in std_list_raw:
#    iec_description_final.append(item.strip())
#print(iec_description_final)


#Function to search for standard based on standard prefix , EN, IEC, IS etc.

def searchForStandard(stdName):
    stdListRaw = re.findall(r''+stdName+'\s\d{3,8}\s-[\s\w]+(?=[\s.?!])[^.?!]*[.?!]', docstring)
    stdDescriptionFinal =  []
    for item in stdListRaw:
        stdDescriptionFinal.append(item.strip())
        stdDescriptionFinal = list(dict.fromkeys(stdDescriptionFinal))
    print(stdDescriptionFinal)

searchForStandard("EN")

#This section searches for the IS standard name and title
std_list_raw = re.findall(r'IS\s\d{3,8}\s-[\s\w]', docstring)
std_list_raw.append(re.findall(r'IS\s\d{3,8}:\d\d\d\d', docstring))
print(std_list_raw)
en_description_final =  []
for item in std_list_raw:
    en_description_final.append(item.strip())
    en_description_final = list(dict.fromkeys(en_description_final))
print(en_description_final)