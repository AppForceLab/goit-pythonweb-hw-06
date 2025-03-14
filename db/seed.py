from faker import Faker
import random
from models import Student, Group, Teacher, Subject, Grade
from db.database import SessionLocal

fake = Faker()

def seed():
    session = SessionLocal()

    groups = [Group(name=f'Group-{fake.unique.word()}') for _ in range(3)]
    session.add_all(groups)
    session.commit()

    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    subjects = [Subject(name=fake.unique.job(), teacher=random.choice(teachers)) for _ in range(8)]
    session.add_all(subjects)
    session.commit()

    students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(50)]
    session.add_all(students)
    session.commit()

    for student in students:
        for _ in range(random.randint(10, 20)):
            grade = Grade(
                student=student,
                subject=random.choice(subjects),
                grade=round(random.uniform(2, 5), 2),
                grade_date=fake.date_this_year()
            )
            session.add(grade)

    session.commit()
    session.close()

if __name__ == '__main__':
    seed()
