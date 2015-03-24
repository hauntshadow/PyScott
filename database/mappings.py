from sqlalchemy import *
engine = create_engine('postgresql+psycopg2:///postgres:password@localhost:5432/pyscottdb', echo=True)
metadata = MetaData()
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.orm import relationship, backref, sessionmaker
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
    movie_id = Column(Integer, ForeignKey('Movie.id'))
    movie = relationship("Movie", backref = backref('Director', order_by = id))
    def __repr__(self):
       return "<Director(id='%d', name='%s', movie_id='%d')>" % (self.id, self.name, self.movie_id)
 
class Actor(Base):
    __tablename__ = 'Actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    movie_id = Column(Integer, ForeignKey('Movie.id'))
    movie = relationship("Movie", backref = backref('Actor', order_by = id))
    def __repr__(self):
       return "<Actor(id='%d', name='%s', movie_id='%d')>" % (self.id, self.name, self.movie_id)

Movie = Table('Movie', metadata,
            Column('id', Integer(), primary_key=True, nullable=False),
            Column('title', String(), nullable=False),
            Column('rating', Integer(), nullable=False),
            Column('review', String(),)
)

Director = Table('Director', metadata,
            Column('id', Integer(), primary_key=True, nullable=False),
            Column('movie', String(), nullable=False)
)

Actor = Table('Actor', metadata,
            Column('id', Integer(), primary_key=True, nullable=False),
            Column('movie', String(), nullable=False)
)

metadata.create_all(engine)

