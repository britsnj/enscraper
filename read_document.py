from xml.dom.minidom import Document
import docx
import re

document = docx.Document('data.docx')
document.save('docdata.docx')

f = open('docdata.docx', 'rb')
document = Document(f)
f.close()

print(document)


# std_list_raw = re.findall(r'[E][N]\s\d{3,5}\s\-\s\w.+[^.]', document)
# en_description_final =  []
# for item in std_list_raw:
#     en_description_final.append(item.strip())
# print(en_description_final)

# std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}\s\-\s\w.+[^.]', document)
# iec_description_final = []
# for item in std_list_raw:
#     iec_description_final.append(item.strip())
# print(iec_description_final)

# std_list_raw = re.findall(r'[E][N]\s\d{3,5}', document)
# en_list_final =  []
# for item in std_list_raw:
#     en_list_final.append(item.strip())
# print(en_list_final)

# std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}', document)
# iec_list_final = []
# for item in std_list_raw:
#     iec_list_final.append(item.strip())
# print(iec_list_final)

