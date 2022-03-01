import docx
import re
from docx import Document
#Open the document as an object
document = docx.Document('data.docx')
#Create a file with the contents of the object by iterating through each paragraph and appending it to the docdata variable
docdata = []
for docpara in document.paragraphs:
    docdata.append(docpara.text)
#Extract the text from the variable and save as a string.
docstring = ' ' .join(docdata)

print(docstring)

#Declare global variables
stdListFull = []
stdListNames = []

#Function to search for standard names based on standard input (i.e. EN, IEC, IEEE etc.
def stdSearch(stdName):
    #Find all standard names, including dates and appendixes and save to list.
    stdListFull = re.findall(r''+stdName+'\s*E*N*\s*\d{2,8}:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*', docstring)
    #Find only the standard names, excluding dates etc. and save to list.
    stdListNames = re.findall(r''+stdName+'\s*E*N*\s*\d{2,8}', docstring)

print(stdListFull)
print(stdListNames)

stdSearch("BS")
globalStdNameList = stdListNames
stdSearch("EN")
globalStdNameList = globalStdNameList + stdListNames
stdSearch("IEC")
globalStdNameList = globalStdNameList + stdListNames
stdSearch("IS")
globalStdNameList = globalStdNameList + stdListNames
stdSearch("I.S.")
globalStdNameList = globalStdNameList + stdListNames
print(globalStdNameList)