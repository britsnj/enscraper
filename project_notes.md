# Project Notes

# 220210 
- VS Environment setup not working for me. Had to revert to PyCharm. Unable to commit. VS Code output window not working. Added the get_document module that finds document and extracts the standard names from the document. Unable to test as VS output and VS terminal does not work. Need to examine how to work with virtual environment in PyCharm. Try again tomorrow.

Additional note. Evening now. Got PyCharm set up for virtual environment. get_page and read_document working like a charm now. 

# 220212
- Combined the read_document and get_page modules into a single function. Refactored code to add a "+" between the standard title and name before submitting to the website.
- Added dictionary with output from website.

Next Actions. Need to work on the regex to extract correct text (name) from document to be able to replace the correct text. ????

# 220227
- Over the past two weeks I worked on the regex functions. Wanted to get to a single expression that searches for all possible iterations of standard names
- Think I cracked it today. ``` +stdName+'\s*E*N*\s*\d{2,8}:*\d*[+]*[A]*\d*:*\d[+]*[A]*\d*:*\d[+]*[A]*\d*:*\d'   ``` with stdName being the standard we are looking for.
# 220305
- The search functions has been completed.
- Added in a feature to open a file based on user input name.
- Original docx file now saved as a backup file as well... just for incase
- Started working on the GUI
- In paralel with the GUI I need to explore the options of saving the output list to a usable excell or word table.
- Create a saved file on network to document all search results
#220324
- Expanded the project to scan an entire folder at a time and write the standards found to a csv file for later use
- Need to create a database folder in the project to save the csv files there for now. This will end up being a network location (I think)
#220325
- Database folder created.
- Messagebox created to indicate process is complete.
- Look into creating progress bar
#220331
- Worked on a section to process the database. 
- Steep learning curve with Pandas, trying to manipulate the csv files. Getting there slowly but surely
#220402
- Got the dataframe to cycle through all the columns and then add it to a single column, then drop the duplicates.
- Save the new dataframe to a csv file.
- Problem is, when I retrieve the dataframe and add to it again, it adds the data as a new column, and does not concatenate to the existing column. I need to look into this.
- Also an issue with the encoding. Pandas not picking up UTF-08 encoding on the database csv. Need to change the save function in the gui file to encode to UTF-08 when saving to csv. Work for tomorrow.
#220405
-Fixed the encoding and managed to sort out the concatenation. Note to self, use Index=False to make sure the file is not saved with an index every time.
#220407
- Struggling trying to extract data based on string from a series. 
#220409
- Mask sorted. Now need to apply the mask to the dataframe.
#220412
- Mask applied. Works like a charm. Now need to find a way to save into a usable format.
#220421
- Apended the above info to a separate csv file for each of the data types.
- Also started to iterate through the values using the get_page module to find the latest version of the standard.
#220423
- Stepping off this one for a while. Need to look at it with fresh eyes. Going to move over to the availability calculator.