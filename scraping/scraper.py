import urllib2
from bs4 import BeautifulSoup

'''Opens the selected URL and stores the html in the html variable'''
req = urllib2.Request('http://www.imdb.com/title/tt0114709/?ref_=chttp_tt_102')
response = urllib2.urlopen(req)
html = (response.read())

'''If we decide to store the html page locally'''
#print(html)
#with open("test.html", "w") as myfile:
#    myfile.write(html)

'''Creates a BeautifulSoup object on the html variable and stores it in soup'''
soup = BeautifulSoup(html)
'''Just prints the page to the console'''
print soup.prettify()

''''Searches the soup variable for the tag titlePageSprite star-box-giga-star''''
result = soup.find_all("div", "titlePageSprite star-box-giga-star")[0]

'''Prints the full result and then prints just the contents which is the rating '''
print str(result)
print(result.renderContents())