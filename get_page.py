from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.en-standard.eu/search/?q=IEC+31010%3A" ##This needs to be replaced with automated search call

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

title = result.contents[0] ##The first child in the result variable is the title of the standard.
print(title)

output = result.span.get_text(" ") ## The name of the standard is located in a span tag.

print (output)