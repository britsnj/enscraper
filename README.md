# enscraper
 Web scraper to get EU standards details. The idea is to search for a standard number and get the latest standard name with latest release date. This is used to update standard names and dates in specifications (separate project still WIP).

 The scraper uses the srandard.eu website. Currently the POST url is used to search for the relevant standard number. The call should be made as follows: "?q=IEC+60364-1%3A". The "?q=" is the query string. Should remain as is. Then "IEC", can be replaced with any standard issued by the European Standards website. These include BS, CSN, DIN, IEC, IEEE, ISO, UNE, VDA, CQI and QS. Spaces to be replaced with a "+". Then "60364-1" should be replaced with the standard number. The "%3A" is a ":" that is added to the end of the string. If a standard exists with a date appended, i.e. "IEC 60364-1:2005" this will be top of the search result.

 The top search result is parsed to the 'output' variable.

Work to still be completed:

1. Automate the search function to accept inputs from an array extracted from a document.
2. Save outputs as array to match the input array.
3. 
