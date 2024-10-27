from sqlalchemy import Column, Integer, String, Float 
from app.database.db import Base


class Gesture(Base):
    __tablename__ = 'gestures'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    meaning = Column(String)
    video_Path = Column(String)
    confidence = Column(Float)