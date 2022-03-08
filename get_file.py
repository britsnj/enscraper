import shutil
import os.path


#Ask user for filename.
#This section will be refactored for TKinter
directory = "C:\projects\enscraper\\"
filename = input("Enter filename:")
filepath = directory + filename


if os.path.exists(filepath):
    #Split filename and create a new backup filename with .bak extension
    name, ext = filename.rsplit('.', 1)
    backup_filename = '{}.{}'.format(name, 'bak')
    #Copy the file to data.docx
    filepath = directory + filename
    shutil.copyfile(filepath, directory+"data.docx")
    #Also copy file to backup file... for incase
    shutil.copyfile(filepath, directory + backup_filename)
else:
    no_file_msg = "That file does not exist. Please try again"
    print(no_file_msg)
