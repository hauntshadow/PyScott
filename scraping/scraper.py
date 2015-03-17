import urllib2
from bs4 import BeautifulSoup
import socket
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


def ratingGenerator():
    timeout = 30
    socket.setdefaulttimeout(timeout)
    mylist = range(1,2908446)
    for x in mylist:
        req = urllib2.Request('http://www.imdb.com/title/tt'+str(x))
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError:
            print 'Connection timed out.'
        html = (response.read())
        soup = BeautifulSoup(html)

        if ( soup.find_all("span","itemprop")):
            title = soup.find_all("span","itemprop")[0]
            '''print(title.renderContents())'''
            title = (title.renderContents())
            if ( soup.find_all("div", "titlePageSprite star-box-giga-star")):
                rating = soup.find_all("div", "titlePageSprite star-box-giga-star")[0]
                '''print(rating.renderContents())'''
                rating = rating.renderContents()
                rating = rating.replace(' ', '')
                yield (title,rating,x)
            else:
                '''print "No rating"'''
                rating = '-1'
                yield (title, rating,x)
        else:
            '''print"No Movie"'''
            yield ('-1','-1',x)

