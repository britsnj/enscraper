import docx
import re
from docx import Document

document = docx.Document('data.docx')

docdata = []
for docpara in document.paragraphs:
    docdata.append(docpara.text)

docstring = ' ' .join(docdata)

print(docstring)

stdName = "IS"

stdListRaw1 = re.findall(r''+stdName+'\s*E*N*\s*\d{2,8}:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*[+]*[A]*\d*:*\d*', docstring)
stdListRaw = re.findall(r''+stdName+'\s*E*N*\s*\d{2,8}', docstring)
print(stdListRaw1)
print(stdListRaw)