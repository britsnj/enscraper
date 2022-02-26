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

def searchStdName(stdName):
    #Search standard name based on standard format, ie EN 12345
    stdListRaw1 = re.findall(r''+stdName+'\s\d{3,8}', docstring)
    #Include standard name without space in name, ie EN12345
    stdListRaw2 = re.findall(r''+stdName+'\d{3,8}', docstring)
    #Include standard name from EN stanards, ie BS EN 12345, IS EN 12345 etc
    stdListRaw3 = re.findall(r'' + stdName + '\sEN\s\d{3,8}', docstring)
    #Include above iterarions including date ie, EN 12345:2020
    stdListRaw11 = re.findall(r''+stdName+'\s\d{3,8}:\d\d\d\d', docstring)
    stdListRaw12 = re.findall(r''+stdName+'\d{3,8}:\d\d\d\d', docstring)
    stdListRaw13 = re.findall(r'' + stdName + '\sEN\s\d{3,8}:\d\d\d\d', docstring)
    # Include Standard with amendments indicate i.e. EN1234:2020+A1:2021
    stdListRaw14 = re.findall(r'' + stdName + '\s\d{3,8}:\d\d\d\d\wA\d{1,2}:\d\d\d\d', docstring)
    stdListRaw15 = re.findall(r'' + stdName + '\d{3,8}:\d\d\d\d\wA\d{1,2}:\d\d\d\d', docstring)
    stdListRaw16 = re.findall(r'' + stdName + '\sEN\s\d{3,8}:\d\d\d\d\wA\d{1,2}:\d\d\d\d', docstring)

    stdListRaw = stdListRaw1 + stdListRaw2 + stdListRaw3 + stdListRaw11 + stdListRaw12 + stdListRaw13 + stdListRaw14 + stdListRaw15 + stdListRaw16
    print((stdListRaw))
    global stdNameList
    stdNameList = []
    for item in stdListRaw:
        stdNameList.append(item.strip())
        stdNameList = list(dict.fromkeys(stdNameList))
    #print(stdNameList)

searchStdName("BS")
globalStdNameList = stdNameList
searchStdName("EN")
globalStdNameList = globalStdNameList + stdNameList
searchStdName("IEC")
globalStdNameList = globalStdNameList + stdNameList
searchStdName("IS")
globalStdNameList = globalStdNameList + stdNameList
searchStdName("I.S.")
globalStdNameList = globalStdNameList + stdNameList
print(globalStdNameList)


#Function to search for standard name and title based on standard prefix, EN, IEC, IS etc
def searchStdNameTitle(stdName):
    stdListRaw = re.findall(r''+stdName+'\s\d{3,8}\s-[\s\w]+(?=[\s.?!])[^.?!]*[.?!]', docstring)
    stdDescriptionFinal =  []
    for item in stdListRaw:
        stdDescriptionFinal.append(item.strip())
        stdDescriptionFinal = list(dict.fromkeys(stdDescriptionFinal))
    print(stdDescriptionFinal)

#searchForStandard("EN")

#This section searches for the IS standard name and title
#std_list_raw = re.findall(r'IS\s\d{3,8}\s-[\s\w]', docstring)
#std_list_raw.append(re.findall(r'IS\s\d{3,8}:\d\d\d\d', docstring))
#print(std_list_raw)
#en_description_final =  []
#for item in std_list_raw:
#    en_description_final.append(item.strip())
#    en_description_final = list(dict.fromkeys(en_description_final))
#print(en_description_final)