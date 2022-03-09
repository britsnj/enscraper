import tkinter as tk
#import themed widgets
from tkinter import ttk
from tkinter import messagebox
#import file dialogue to be able to open file
from tkinter import filedialog as fd

#import local assets
from get_file import handle_file


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
    handle_file(filepath)


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






#Keep window Open
root.mainloop()