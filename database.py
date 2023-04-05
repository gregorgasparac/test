from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///forum.db")

Base = declarative_base()

class Forum(Base):
    __tablename__ = "zapisi"
    id = Column(Integer, primary_key=True)
    text = Column(String(50))

class Topics(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    topic = Column(String(50), nullable=False)