import tkinter as tk
#import themed widgets
from tkinter import ttk
from tkinter import messagebox
#import file dialogue to be able to open file
from tkinter import filedialog as fd
import os
#Import docx2 library to manipulate word documents
import docx
import re
from docx import Document
#import local assets
from get_file import handle_file
from ultimate_search import stdSearch



# Create Window
root = tk.Tk()
#Rename window title
root.title('Document Standard Search')
#Change size and geometry
root.geometry('600x400+400+100')
root.minsize(300, 150)

selectfile = ttk.Frame(root)
selectfile.pack(pady=10, padx=10, fill='x', expand=True)

#Format here is widget= WidgetName(container, **Options)


def submit_clicked():
    filepath = filename_entry.get()
    filepath = filepath.replace('"', '')
    temp_name, file_ext = filepath.rsplit('.', 1)
    filename = filepath.rsplit('\\', 1)
    print(filename)
    print(file_ext)
    if (file_ext != 'txt') and (file_ext != 'docx'):
        messagebox.showinfo(
            title='File Error',
            message="Unknown file type. Only txt or docx files accepted"
        )
    elif os.path.exists(filepath):
        handle_file(filepath)
        filename_entry.delete(0, 'end')
        readDocx()
        searchAll()
        results = tk.Tk()
        results.title("Standards Found")
        results.geometry('500x300+450+150')
        results.minsize(250, 100)

        results_label = ttk.Label(results, text="The standards found in "+filename+ " is:")
        results_label.pack(fill='x', expand=True)

        filename_entry = ttk.Entry(selectfile)
        filename_entry.pack(fill='x', expand=True, )

        results.mainloop()



    else:
        messagebox.showinfo(
            title='File Error',
            message="That file does not exist. Please try again"
        )



#Filename

filename_label = ttk.Label(selectfile, text="File to be scanned (complete path):")
filename_label.pack(fill='x', expand=True)

filename_entry = ttk.Entry(selectfile)
filename_entry.pack(fill='x', expand=True,)

#Submit button
submit_button = ttk.Button(selectfile, text="Submit", command=submit_clicked)
submit_button.pack(fill='x', expand=True, pady=10)

text1 = ttk.Label(selectfile, text='Or click below to select a file')
text1.pack(ipady=10, ipadx=10)

#Output Label

#insert file open dialogue

def select_file():
    filetypes = (
        ('word document', '*.docx'),
        ('text files', '*.txt')
    )

    filepath = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )

    messagebox.showinfo(
        title='Selected File',
        message=filepath
    )

    filepath = filepath.replace('/', "\\")
    print(filepath)
    handle_file(filepath)




open_button = ttk.Button(
    selectfile,
    text='Select File',
    command=select_file
)




open_button.pack()

#print(filepath)

#Search Functions

#Function to search for standard names based on standard input (i.e. EN, IEC, IEEE etc.
def stdSearch(stdName):
    global stdListFull
    global stdListNames
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
    #print(stdListFull)
    #print(stdListNames)

def searchAll():
    global globalStdNameList
    globalStdNameList = []
    stdSearch("EN")
    globalStdNameList = globalStdNameList + stdListNames
    stdSearch("IEC")
    globalStdNameList = globalStdNameList + stdListNames
    stdSearch("IS")
    globalStdNameList = globalStdNameList + stdListNames
    stdSearch("I.S.")
    globalStdNameList = globalStdNameList + stdListNames
    stdSearch("ISO")
    globalStdNameList = globalStdNameList + stdListNames
    stdSearch("IEEE")
    globalStdNameList = globalStdNameList + stdListNames
    print(globalStdNameList)

def readDocx():
    global docstring
    docstring = []
    #Open the document as an object
    document = docx.Document('data.docx')
    #Create a file with the contents of the object by iterating through each paragraph and appending it to the docdata variable
    docdata = []
    for docpara in document.paragraphs:
        docdata.append(docpara.text)
    #Extract the text from the variable and save as a string.
    docstring = ' ' .join(docdata)
    #print(docstring)





#Keep window Open
root.mainloop()