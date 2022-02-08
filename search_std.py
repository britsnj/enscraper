import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()

url = "https://www.en-standard.eu"

page = browser.get(url)

page