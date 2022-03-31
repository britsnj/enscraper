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
