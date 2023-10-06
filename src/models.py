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


# Define your existing Student, Parent, and other models here

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(50))
    date_of_birth = Column(String(50))  # Add this line for date of birth
    email = Column(String(50), unique=True)
    phone_number = Column(String(15))

    # Define a one-to-many relationship with Course
    courses_taught = relationship('Course', back_populates='teacher')


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_code = Column(String(20), unique=True, nullable=False)
    course_name = Column(String(100), nullable=False)
    description = Column(String(255))

    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    # Define the many-to-one relationship with Teacher
    teacher = relationship('Teacher', back_populates='courses')

    # Define a one-to-many relationship with Assignment
    assignments = relationship('Assignment', back_populates='course')

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True)
    assignment_name = Column(String(100), nullable=False)
    maximum_marks = Column(Integer)
    assignment_details = Column(String(255))

    course_id = Column(Integer, ForeignKey('courses.id'))

    # Define the many-to-one relationship with Course
    course = relationship('Course', back_populates='assignments')

    # Define a one-to-many relationship with Grade
    grades = relationship('Grade', back_populates='assignment')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    grade = Column(Integer)

    # Define the many-to-one relationship with Student
    student = relationship('Student', back_populates='grades')

    # Define the many-to-one relationship with Assignment
    assignment = relationship('Assignment', back_populates='grades')
