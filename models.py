from sqlalchemy import \
    Column, Integer, String, ForeignKey
from database import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),nullable=False)
    age = Column(Integer)

class Registration():
    __tablename__ = 'registers'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    subject = Column(String(100), nullable=False)