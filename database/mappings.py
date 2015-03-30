from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from settings import DI_DATABASE

Base = declarative_base()
metadata = Base.metadata 
engine = create_engine(URL(**DI_DATABASE), echo=True);
#engine = create_engine('postgresql://david:password@104.236.255.188:5432/pyscottdb', echo=True)
session = sessionmaker(bind=engine)()


class Movie(Base):
    __tablename__ = 'Movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Integer)
    review = Column(String)

    def __repr__(self):
        return "<Movie(id='%d', title='%s', rating='%d', review='%s')>" % (self.id, self.title, self.rating, self.review)


class Director(Base):
    __tablename__ = 'Directors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    #movie_id = Column(Integer, ForeignKey('Movie.id'))
    #movie = relationship("Movie", backref = backref('Director', order_by = id))

    def __repr__(self):
        return "<Director(id='%d', name='%s', movie_id='%d')>" % (self.id, self.name, self.movie_id)


class Actor(Base):
    __tablename__ = 'Actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    #movie_id = Column(Integer, ForeignKey('Movie.id'))
    #movie = relationship("Movie", backref = backref('Actor', order_by = id))

    def __repr__(self):
        return "<Actor(id='%d', name='%s', movie_id='%d')>" % (self.id, self.name, self.movie_id)


metadata.create_all(engine)

