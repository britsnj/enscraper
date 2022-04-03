# enscraper
 Web scraper to get EU standards details. The idea is to search for a standard number and get the latest standard name with latest release date. This is used to update standard names and dates in specifications (separate project still WIP).

 The scraper uses the srandard.eu website. Currently the POST url is used to search for the relevant standard number. The call should be made as follows: "?q=IEC+60364-1%3A". The "?q=" is the query string. Should remain as is. Then "IEC", can be replaced with any standard issued by the European Standards website. These include BS, CSN, DIN, IEC, IEEE, ISO, UNE, VDA, CQI and QS. Spaces to be replaced with a "+". Then "60364-1" should be replaced with the standard number. The "%3A" is a ":" that is added to the end of the string. If a standard exists with a date appended, i.e. "IEC 60364-1:2005" this will be top of the search result.

 The top search result is parsed to the 'output' variable.




Went off on a tangent here. Now also including a scan directory function where the function searches all doc files located in a directory

Adding in a csv file to store the output reports for future database. Note to self - learn how to use pandas or numpy.

Done now. Still need to colate the data into a single file, i.e. get the name from a row and add it to a master row if not there already

Have to add in an overall gui to give access to all the different components.



