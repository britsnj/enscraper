import numpy as np
import pandas as pd
from tkinter import filedialog
from tkinter import *
import re
from os.path import exists

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
print(final_df)
for i in range(shape[1]):
    temp_df = df[i]
    temp_df = temp_df.dropna()
    final_df = pd.concat([final_df, temp_df])

final_df = final_df.drop_duplicates()

print(final_df)

def updateSpecificDatabase(std):
    #Create a true / false mask for standards beginning with the argument
    mask = final_df.str.contains(fr'^{std}\W', regex= True)
    #Apply the mask to the final_df dataframe
    masked_df=final_df.loc[mask]


    stdFileName = 'db_files'+'\\'+str.lower(std)+'_db.csv'
    #Check if database file exist and create if it does not. Write "0" into file. Pandas cannot parse empty csv file.
    #Then open database file.
    if exists(stdFileName):
        std_df = pd.read_csv(stdFileName, engine='python')
    else:
        with open(stdFileName, "w") as f:
            f.write("0")
        std_df = pd.read_csv(stdFileName, engine='python')
    #Squeeze colums to remove index column
    std_df = std_df.squeeze('columns')
    #Concatenate the masked dataframe to the bottom of the standard dataframe and remove all duplicate entries.
    std_df = pd.concat([std_df, masked_df])
    std_df = std_df.drop_duplicates()
    #Save the standard database.
    std_df.to_csv(stdFileName, index=False)

updateSpecificDatabase('EN')
updateSpecificDatabase('IS')
updateSpecificDatabase('ISO')
updateSpecificDatabase('IEC')
updateSpecificDatabase('IEEE')
updateSpecificDatabase('BS')
updateSpecificDatabase('NFPA')
updateSpecificDatabase('DIN')

#This saves the final dataframe. Should probably remove this and not concatenate this, or add a temp final dataframe. In the current
#format the final dataframe will be added to the standard dataframe every time. Sloppy.
final_df.to_csv(database_file, index=False)

