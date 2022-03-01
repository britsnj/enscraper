import shutil

directory = "C:\projects\enscraper\\"

filepath = directory + input("Enter filename:")

shutil.copyfile(filepath, directory+"data.docx")