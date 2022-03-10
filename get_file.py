import shutil
import os.path


#Ask user for filename.
#This section will be refactored for TKinter

# filepath = input("Enter filename (full path):")



def handle_file(filepath):

    if os.path.exists(filepath):
        #Split filename filepath and filename to create a new backup filename with .bak extension
        directory, filename = filepath.rsplit('\\', 1)
        name, ext = filename.rsplit('.', 1)
        backup_filename = '{}.{}'.format(name, 'sbak')
        print(directory)
        print(filename)
        print(name)
        print(ext)
        print(backup_filename)
        #Copy the file to data.docx in program directory (consider separate directory)
        shutil.copyfile(filepath, "data.docx")
        #Also copy file to backup file... for incase
        shutil.copyfile(filepath, directory + '\\' + backup_filename)
    else:
        no_file_msg = "That file does not exist. Please try again"
        print(no_file_msg)



# handle_file(filepath)