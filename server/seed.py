from app import app 
from models import db, Student, Class 


if __name__ == '__main__':
    with app.app_context():

        
        print("Clearing out tables....")

        Student.query.delete()
        Class.query.delete()

        print("Seeding class table...")

        new_class_1 = Class(
            name = "Homeroom 1",
            teacher_name = "Antonella DiLillo"
        )

        db.session.add(new_class_1)
        db.session.commit()


        new_class_2 = Class(
            name = "Homeroom 2",
            teacher_name = "Mitch Mcccoo"
        )

        db.session.add(new_class_2)
        db.session.commit()

        print("Seeding students table...")

        new_student = Student(
            name = "Eliza",
            homeroom_id = new_class_1.id
        )

        db.session.add(new_student)
        db.session.commit()

        new_student_2 = Student(
            name = "Mollie",
            homeroom_id = Class.query.first().id
        )
        db.session.add(new_student_2)
        db.session.commit()

        new_students = [
            Student(
                name = "Melody",
                homeroom_id = new_class_2.id
            ),
            Student(
                name = "Ron",
                homeroom_id = new_class_2.id
            ),
            Student(
                name = "Cody",
                homeroom_id = new_class_1.id
            ),
        ]
        db.session.add_all(new_students)
        db.session.commit()

        new_class_name = input("Enter a class name: ")
        new_class_teacher = input("Enter a teacher name: ")

        new_class = Class(
            name = new_class_name,
            teacher_name = new_class_teacher
        )

        db.session.add_all(new_class)
        db.session.commit()
