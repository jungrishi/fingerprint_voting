import os
import sys
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Binary, Boolean, ForeignKey, Date
import json
import datetime

# Create an engine that stores data in the local directory's

try:
    with open('config', 'r') as f:
        config = json.load(f)
except IOError as err:
    print("Cannot open configuration: {} Exiting".format(str(err)))
    sys.exit(1)
engine = create_engine(
    '{sql}:///{db}+.db'.format(**config))
Base = declarative_base(engine)
metadata = Base.metadata
Session = sessionmaker(bind=engine)
metadata.create_all(engine)

session = Session()


class registerDB(Base):
    __tablename__ = 'users'
    sid = Column(Integer, primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    nationality = Column(String(120))
    DOB = Column(Date)
    fingerprinted = Column(Boolean, default=0)
    vote = Column(Integer)

    def __init__(self, firstname, lastname, nationality, DOB):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        Y, M, D = DOB.split('/')
        self.DOB = datetime.datetime(int(Y), int(M), int(D))
        self.nationality = nationality.lower()
