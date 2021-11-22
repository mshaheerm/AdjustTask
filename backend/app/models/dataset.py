from sqlalchemy import Column, Date, Float, Integer, String
from db.database import Base

class DataSet(Base):
    __tablename__ = 'DataSet'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    channel = Column(String)
    country = Column(String)
    os = Column(String)
    impressions = Column(Integer)
    clicks = Column(Integer)
    installs = Column(Integer)
    spend = Column(Float)
    revenue = Column(Float)
