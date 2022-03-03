import tkinter as tk
#import themed widgets
from tkinter import ttk
# Create Window
root = tk.Tk()
#Rename window title
root.title('Document Standard Search')
#Change size and geometry
root.geometry('600x400+400+100')
root.minsize(300, 150)


#Format here is widget= WidgetName(container, **Options)
message = ttk.Label(root, text="Hello World!")
#Place the widget on the window
message.pack()



#Keep window Open
root.mainloop()