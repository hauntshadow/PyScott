import urllib2
from bs4 import BeautifulSoup
import pprint


req = urllib2.Request('http://www.imdb.com/title/tt0114709/?ref_=chttp_tt_102')
response = urllib2.urlopen(req)
html = (response.read())


#print(html)
#with open("test.html", "w") as myfile:
#    myfile.write(html)

soup = BeautifulSoup(html)

print soup.prettify()


result = soup.find_all("div", "titlePageSprite star-box-giga-star")[0]
print str(result)
print(result.renderContents())

#print len(soup.find_all('<div class="titlePageSprite star-box-giga-star"> 8.3 </div>'))