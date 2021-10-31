from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_user(Name, password):
  the_user = User(Name = Name, password = password)
  session.add(the_user)
  session.commit()

def find_user(Name):
  exic_user = session.query(User).filter_by(Name = Name).first()
  return exic_user


def add_quiz(gender, social, salary, family):
  the_quiz = Quiz(gender = gender, social = social, salary = salary, famil = family)

#def query_by_quiz(Gender, Social, Salary, Family):
  #the_quiz = session.query(Quiz).filter_by(gender = Gender, social = Social, family = Family)


