# https://www.youtube.com/watch?v=6eVj33l5e9M&t=2909s&ab_channel=FaztCode
# https://www.youtube.com/watch?v=AKQ3XEDI9Mw&t=41s&ab_channel=NeuralNine

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float, CHAR, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from readingCSV.py import *



Base = declarative_base()

class Bay(Base):
    __tablename__ = "fridgesdb"

    bayId = Column("bayId", Integer, primary_key=True)
    time = Column("time", String)
    chillerStatus = Column("chillerStatus", Integer)
    temp = Column("temp", Float)
    hum = Column("hum", Float)
    pwr = Column("pwr", Float)

    def __init__(self, bayId, time, chillerStatus, temp, hum, pwr):
        self.bayId = bayId
        self.time = time
        self.chillerStatus = chillerStatus
        self.temp = temp
        self.hum = hum
        self.pwr = pwr

    def __repr__(self):
        return f"Bay {self.bayId} at {self.time} has a temperature of {self.temp}, a humidity of {self.hum} and a power draw of {self.pwr}"


# engine = create_engine("sqlite:///fridges.db", echo=True)
engine = create_engine("mysql+pymysql://root:root@localhost:3306/fridgesdb", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# bay1table = Bay(bay1.time, bay1.chillerStatus, bay1.temp, bay1.hum, bay1.pwr)