import urllib2
from bs4 import BeautifulSoup
import time
'''Opens the selected URL and stores the html in the html variable'''
#req = urllib2.Request('http://www.imdb.com/title/tt0114709')
#response = urllib2.urlopen(req)
#html = (response.read())

'''If we decide to store the html page locally'''
#print(html)
#with open("test.html", "w") as myfile:
#    myfile.write(html)

'''Creates a BeautifulSoup object on the html variable and stores it in soup'''
#soup = BeautifulSoup(html)
'''Just prints the page to the console'''
#print soup.prettify()

''''Searches the soup variable for the tag titlePageSprite star-box-giga-star'''
#rating = soup.find_all("div", "titlePageSprite star-box-giga-star")[0]
#title = soup.find_all("span","itemprop")[0]

#print(str(title))
#print str(rating)
'''prints the title and rating'''
#print(title.renderContents())
#print(rating.renderContents())
count = 0.0
avg = 0.0
sum = 0.0
for x in range(1,2381941):

    req = urllib2.Request('http://www.imdb.com/title/tt'+str(x))
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError:
        print 'Connection timed out.'
    html = (response.read())
    soup = BeautifulSoup(html)


    if ( soup.find_all("span","itemprop")):
        title = soup.find_all("span","itemprop")[0]
        print(title.renderContents())

    if ( soup.find_all("div", "titlePageSprite star-box-giga-star")):
        rating = soup.find_all("div", "titlePageSprite star-box-giga-star")[0]
        print(rating.renderContents())
        sum = sum + float(rating.renderContents())
    else:
        print "No rating"
    count = count + 1
    print x
    if ((x % 300) == 0):
        time.sleep(10)

avg = sum / count
print avg

