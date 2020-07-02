from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query =db_session.query_property()

class Urls(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    shortUrl = Column(String(100), unique = True)
    longUrl = Column(String(400))

    def __init__(self, shortUrl, longUrl):
        self.shortUrl = shortUrl
        self.longUrl = longUrl

    def __repr__(self):
        return '<Url {}> {} {}'.format(self.id, self.shortUrl, self.longUrl)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)