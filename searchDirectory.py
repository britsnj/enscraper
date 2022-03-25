from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import time
import os
import docx
import re
from docx import Document
from pathlib import Path
import csv

def stdSearch(stdName):
    stdListFull = []
    stdListNames = []
    if stdName == "EN":
        #Find all standard names, including dates and appendixes and save to list.
        stdListFull = re.findall(r''+stdName+'\s*I*E*C*\s*\d{2,8}-*\d*-*\d*-*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*', docstring)
        stdListFull = stdListFull + re.findall(r''+stdName+'\s*I*S*O*\s*\d{2,8}-*\d*-*\d*-*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*', docstring)
        #Find only the standard names, excluding dates etc. and save to list.
        stdListNames = re.findall(r''+stdName+'\s*I*E*C*\s*\d{2,8}-*\d*-*\d*', docstring)
    elif stdName == "IEEE":
        stdListFull = re.findall(r''+stdName+'\s*\w*\d{2,5}[.]*\d*[.]*\d*-*:*\d*', docstring)
        stdListNames = re.findall(r'' + stdName + '\s*\w*\d{2,5}[.]*\d*[.]*\d*', docstring)
    else:
        stdListFull = stdListFull + re.findall(r'' + stdName + '\s*E*N*\s*\d{2,8}-*\d*-*\d*-*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*', docstring)
        stdListNames = re.findall(r''+stdName+'\s*E*N*\s*\d{2,8}-*\d*-*\d*', docstring)
    return stdListFull

def searchAll():
    globalStdFullDesc = []
    globalStdFullDesc = globalStdFullDesc + stdSearch("EN")
    globalStdFullDesc = globalStdFullDesc + stdSearch("IEC")
    globalStdFullDesc = globalStdFullDesc + stdSearch("IS")
    globalStdFullDesc = globalStdFullDesc + stdSearch("I.S.")
    globalStdFullDesc = globalStdFullDesc + stdSearch("ISO")
    globalStdFullDesc = globalStdFullDesc + stdSearch("IEEE")
    tempList = []
    for item in globalStdFullDesc:
        tempList.append(item.strip())
        tempList = list(dict.fromkeys(globalStdFullDesc))
    globalStdFullDesc = tempList
    return globalStdFullDesc


root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
timestr = time.strftime("%Y%m%d-%H%M%S")
dbFolder = Path("db_files")
dbFile = timestr+'.csv'
db = open(dbFolder / dbFile, 'x')
db.close()
dir_list = os.listdir(folder_selected)
print(dir_list)
for file in dir_list:
    if file.endswith(".docx"):
        filename, ext = file.rsplit('.', 1)

        document = docx.Document(folder_selected + '/' +file)
        # Create a file with the contents of the object by iterating through each paragraph and appending it to the docdata variable
        docdata = []
        for docpara in document.paragraphs:
            docdata.append(docpara.text)
        # Extract the text from the variable and save as a string.
        docstring = ' '.join(docdata)
        docSearchResults = searchAll()
        docSearchResults.insert(0, filename)
        with open(dbFolder / dbFile, "a", newline='') as output:
            # use csv.writer method to write output to csv package
            writer = csv.writer(output)
            writer.writerow(docSearchResults)
            output.close()

messagebox.showinfo(
    title='Success',
    message="Directory scanned. Database Saved"
)






