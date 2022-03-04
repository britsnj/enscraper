import tkinter as tk
#import themed widgets
from tkinter import ttk
from tkinter import messagebox
#import file dialogue to be able to open file
from tkinter import filedialog as fd
# Create Window
root = tk.Tk()
#Rename window title
root.title('Document Standard Search')
#Change size and geometry
root.geometry('600x400+400+100')
root.minsize(300, 150)

#insert file open dialogue
def select_file():
    filetypes = (
        ('word document', '*.docx'),
        ('text files', '*.txt')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )

    messagebox.showinfo(
        title='Selected File',
        message=filename
    )

open_button = ttk.Button(
    root,
    text='Select File',
    command=select_file
)

open_button.pack()

#Format here is widget= WidgetName(container, **Options)

selectFile = ttk.Frame(root)
selectFile.pack(padx=10, pady=10, fill='x', expand=True)
filename_entry = ttk.Label(selectFile, text="Select File:")
filename_entry.pack(fill='x', expand=True)




message = ttk.Label(root, text="Hello World!")
#Place the widget on the window
message.pack()



#Keep window Open
root.mainloop()