from tkinter import filedialog
from tkinter import *
import os
import docx
import re
from docx import Document

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
dir_list = os.listdir(folder_selected)
print(dir_list)
for file in dir_list:
    if file.endswith(".docx"):
        filename, ext = file.rsplit('.', 1)

        document = docx.Document(''+folder_selected+'/'+file+'')
        # Create a file with the contents of the object by iterating through each paragraph and appending it to the docdata variable
        docdata = []
        for docpara in document.paragraphs:
            docdata.append(docpara.text)
        # Extract the text from the variable and save as a string.
        docstring = ' '.join(docdata)
        print(docstring)

