from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Define the association table for many-to-many relationship
students_parents = Table(
    'students_parents',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('parent_id', Integer, ForeignKey('parents.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String(50))
    date_of_birth = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(50))

    # Define the many-to-many relationship with Parent
    parents = relationship('Parent', secondary=students_parents, back_populates='children')

class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    parent_name = Column(String(50))
    date_of_birth = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(50))

    # Define the many-to-many relationship with Student
    children = relationship('Student', secondary=students_parents, back_populates='parents')
