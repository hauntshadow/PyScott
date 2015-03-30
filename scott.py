__author__ = 'Owner'
from scraping import scraper as s
from database.mappings import Movie as d
from database.mappings import Actor as a
from sqlalchemy.orm import sessionmaker
from database.settings import DI_DATABASE
from sqlalchemy.engine.url import URL


from sqlalchemy import create_engine ,Table, Column, Integer, String, MetaData, ForeignKey, Sequence
#engine = create_engine('postgresql://david:password@104.236.255.188:5432/pyscottdb',echo=True)
engine = create_engine(URL(**DI_DATABASE), echo=True);
newGen = s.ratingGenerator()
Session = sessionmaker(bind=engine)
session = Session()
session.close_all()

#actor = a(id=1,name="asdf",movie_id=1)

#session.add(actor)
session.close_all()
for x in newGen:
    print(x)
    movie = d(id=x[2], title=x[0], rating=int(float(x[1])), review="N/A")
    session.add(movie)
    session.commit()

