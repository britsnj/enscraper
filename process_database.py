import numpy as np
import pandas as pd
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
database_file = filedialog.askopenfilename(title="Select database file", filetypes=(("csv files", "*.csv"),))
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
df = pd.read_csv(file_selected, header=None, delimiter=data_file_delimiter, names=column_names, engine='python')
df = df.transpose()
df = df.drop(0)
print(df)
header_values = df.columns.values
shape = df.shape
print(shape[1])
final_df = pd.read_csv(database_file, engine ='python')
final_df = final_df.squeeze('columns')
for i in range(shape[1]):
    temp_df = df[i]
    temp_df = temp_df.dropna()
    final_df = pd.concat([final_df, temp_df])

final_df = final_df.drop_duplicates()
final_df.reset_index(drop=True, inplace=True)
print(final_df)
final_df.to_csv(database_file)

