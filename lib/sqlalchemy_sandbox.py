
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db', echo=False) 

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    students_to_add = [
        Student(name="Victor"),
        Student(name="Faith"),
        Student(name="Winny"),
        Student(name="David"),
    ]

    session.add_all(students_to_add)
    session.commit()

    all_students = session.query(Student).all()
    print("Students in database:")
    for student in all_students:
        print(f"ID: {student.id}, Name: {student.name}")
