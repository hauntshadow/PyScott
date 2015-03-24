from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Movie(Base):
    __tablename__ = 'Movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Integer)
    review = Column(String)
    def __repr__(self):
       return "<Movie(id='%d', title='%s', rating='%s', review='%s')>" % (self.id, self.title, self.rating, self.review)

class Director(Base):
    __tablename__ = 'Directors'
    id = Column(Integer, primary_key=True)
    movie = Column(Movie)
    
class Actor(Base):
    __tablename__ = 'Actors'
    id = Column(Integer, primary_key=True)
    movie = Column(Movie)

#Table('users', MetaData(bind=None),
#            Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
#            Column('name', String(), table=<users>),
#            Column('fullname', String(), table=<users>),
#            Column('password', String(), table=<users>), schema=None)

