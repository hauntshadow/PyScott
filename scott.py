__author__ = 'Owner'
from scraping import scraper as s


newGen = s.ratingGenerator()
for x in newGen:
    print(x)