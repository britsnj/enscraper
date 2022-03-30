import numpy as np
import pandas as pd
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
file_selected = filedialog.askopenfilename(title="Select file to merge with database", filetypes=(("csv files", "*.csv"),))
print((file_selected))

# Delimiter
data_file_delimiter = ','

# The max column count a line in the file could have
largest_column_count = 0

# Loop the data lines
with open(file_selected, 'r') as temp_f:
    # Read the lines
    lines = temp_f.readlines()

    for l in lines:
        # Count the column count for the current line
        column_count = len(l.split(data_file_delimiter)) + 1

        # Set the new most column count
        largest_column_count = column_count if largest_column_count < column_count else largest_column_count

# Generate column names (will be 0, 1, 2, ..., largest_column_count - 1)
column_names = [i for i in range(0, largest_column_count)]
# Read csv
df = pd.read_csv(file_selected, header=None, delimiter=data_file_delimiter, names=column_names)
df = df.transpose()
df = df.drop(0)
print(df)
header_values = df.columns.values

new_df1 = df[0]
new_df1 = new_df1.dropna()
print(new_df1)
new_df2 = df[1]
new_df2 = new_df2.dropna()
print(new_df2)
final_list = pd.concat([new_df1, new_df2])
final_list.columns = ["name",]
final_list.head()
final_list = final_list.drop_duplicates()
#final_list = final_list.sort_values(['name'])
final_list.reset_index(drop=True, inplace=True)
print(final_list)

