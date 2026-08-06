from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from faker import Faker
import random

DATABASE_URL = "postgresql://teacher:super_password@localhost:5432/education_platform"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
f = Faker()

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)

    courses = relationship(
        "Educations", secondary="student_courses", back_populates="students"
    )

class Educations(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    description = Column(String)

    students = relationship(
        "Students", secondary="student_courses", back_populates="courses"
    )

    def __repr__(self):
        return f"<Course: {self.course_name}>"

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

all_courses = [
    Educations(course_name=f.catch_phrase(), description=f.sentence())
    for _ in range(5)
]

for _ in range(20):
    session.add(
        Students(
            name=f.name_male(),
            age=random.randint(18, 45),
            address=f.address(),
            courses=random.sample(all_courses, k=random.randint(1, 2)),
        )
    )

session.commit()

student = session.query(Students).filter(Students.id == 1).first()

students = (
    session.query(Students)
    .join(Students.courses)
    .filter(Educations.id == 1)
    .all()
)

for student in students:
    print(f"- {student.name}")

student = session.query(Students).filter_by(id=5).first()
student.age = 33

course = session.query(Educations).filter_by(id=3).first()
course.course_name = 'Course name updated'

student_to_delete = session.query(Students).filter_by(id=6).first()
if student_to_delete:
    session.delete(student_to_delete)
session.commit()
session.close()
