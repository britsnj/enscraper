from urllib.request import urlopen
from bs4 import BeautifulSoup

import docx
import re
from docx import Document

updatedStandard = {} ##Declare Dictionary to save updated  Standard values

document = docx.Document('data.docx')

docdata = []
for docpara in document.paragraphs:
    docdata.append(docpara.text)

docstring = ' ' .join(docdata)
#print(docstring)


#std_list_raw = re.findall(r'[E][N]\s\d{3,5}\s\-\s\w.+[^.]', docstring)
#en_description_final =  []
#for item in std_list_raw:
#    en_description_final.append(item.strip())
#en_description_final = list(dict.fromkeys(en_description_final))
#print(en_description_final)

#std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}\s\-\s\w.+[^.]', docstring)
#iec_description_final = []
#for item in std_list_raw:
#    iec_description_final.append(item.strip())
#print(iec_description_final)

std_list_raw = re.findall(r'[E][N]\s\d{3,5}', docstring)
en_list_final =  []
for item in std_list_raw:
    en_list_final.append(item.strip())
en_list_final = list(dict.fromkeys(en_list_final))
print(en_list_final)

std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}', docstring)
iec_list_final = []
for item in std_list_raw:
    iec_list_final.append(item.strip().replace(" ","+"))
iec_list_final = list(dict.fromkeys(iec_list_final))
print(iec_list_final)

for enstd in en_list_final:

    searchstring = enstd.replace(" ","+")

    url = "https://www.en-standard.eu/search/?q="+searchstring+"%3A"

    ##To open the page pass the url to urlopen

    page = urlopen(url)

    ## Unencode and save the page
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    ## Parse the page

    soup = BeautifulSoup(html, 'html.parser')

    ##Search for the first catalogue product name from the results field. This is the first container with this class name
    ##Most probably also the item that may change the easiest on the website. If the scraper breaks, start looking here.

    result = soup.find("a", class_="katalogProduct__name")

    title = result.contents[0]  ##The first child in the result variable is the title of the standard.
    print(title)

    output = result.span.get_text(" ") ##The name is located inside a span tag.

    print(output)

    updatedStandard[title] = output


print(updatedStandard)
