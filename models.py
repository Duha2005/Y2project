from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key = True)
  Name = Column(String)
  password = Column(String(8))

class Quiz(Base):
  __tablename__ = "quiz"
  id = Column(Integer, primary_key = True)
  gender = Column(String)
  social = Column(String)
  salary = Column(Integer)
  family = Column(String)

class Second_Quiz(Base):
  __tablename__ = "sec_quiz"
  id = Column(Integer, primary_key = True)
  house = Column(Integer)
  wife = Column(Integer)
  kids = Column(Integer)
  yourself = Column(Integer)
  
  
  
