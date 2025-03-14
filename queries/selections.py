import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from models import Student, Grade, Subject, Teacher, Group

load_dotenv()

engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()

# 1. 5 студентів із найвищим середнім балом
def select_1():
    result = session.query(Student.fullname, func.avg(Grade.grade).label('avg_grade'))\
        .join(Grade).group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

# 2. Студент із найвищим середнім балом з певного предмета
def select_2(subject_id):
    result = session.query(Student.fullname, func.avg(Grade.grade).label('avg_grade'))\
        .join(Grade).filter(Grade.subject_id == subject_id)\
        .group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    return result

# 3. Середній бал у групах з певного предмета
def select_3(subject_id):
    result = session.query(Group.name, func.avg(Grade.grade))\
        .join(Group.students).join(Student.grades)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Group.id).all()
    return result

# 4. Середній бал по всьому потоку
def select_4():
    result = session.query(func.avg(Grade.grade)).scalar()
    return result

# 5. Курси певного викладача
def select_5(teacher_id):
    result = session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
    return result

# 6. Список студентів у групі
def select_6(group_id):
    result = session.query(Student.fullname).filter(Student.group_id == group_id).all()
    return result

# 7. Оцінки студентів у групі з предмета
def select_7(group_id, subject_id):
    result = session.query(Student.fullname, Grade.grade)\
        .join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
    return result

# 8. Середній бал, який ставить викладач
def select_8(teacher_id):
    result = session.query(func.avg(Grade.grade))\
        .join(Subject).filter(Subject.teacher_id == teacher_id).scalar()
    return result

# 9. Курси, які відвідує студент
def select_9(student_id):
    result = session.query(Subject.name).join(Grade)\
        .filter(Grade.student_id == student_id).distinct().all()
    return result

# 10. Курси, які студенту читає певний викладач
def select_10(student_id, teacher_id):
    result = session.query(Subject.name).join(Grade)\
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)\
        .distinct().all()
    return result

if __name__ == '__main__':
    print(select_1())
    print(select_2(1))
    print(select_3(1))
    print(select_4())
    print(select_5(1))
    print(select_6(1))
    print(select_7(1, 1))
    print(select_8(1))
    print(select_9(1))
    print(select_10(1, 1))
