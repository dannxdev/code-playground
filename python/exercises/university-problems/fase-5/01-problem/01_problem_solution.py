import os

os.system('cls')

# CLASSES:


class School:

    def __init__(self, school_nit, school_name):
        self.school_nit = school_nit
        self.school_name = school_name
        # Students:
        self.school_students = {}
        # Courses:
        self.school_courses = {}
        self.school_payment_methods = {}

    def add_course(self, course):
        """Agrega un curso a la escuela."""

        if isinstance(course, Course):
            if not course.course_id in self.school_courses:
                # Si el curso no existe en la escuela aun:
                self.school_courses[course.course_id] = course
                print(
                    f"✅ Course '{course.course_name}' added to the '{self.school_name}' school.")
                return True
            print(
                f"⚠️ Course '{course.course_name}' already exists in the '{self.school_name}' school")
            return False

        # Si el argumento no es de la instancia Course:
        raise ValueError('arg: course_instance must be Course class instance.')

    def add_student(self, student_instance):
        """Agrega un curso estudiante a la escuela."""


class Course:

    def __init__(self, course_id, course_name, course_monthly_price, course_duration, course_fp_discount) -> None:
        self.course_id = course_id
        self.course_name = course_name
        self.course_monthly_price = course_monthly_price
        self.course_duration = course_duration
        self.course_fp_discount = course_fp_discount


# class PaymentMethod:

#     def __init__(self, pay_method_id, pay_method_name, )


# PRUEBA DE CODIGO:

my_school = School('73648064', 'DannxAcademy')

# CURSOS:

course_01 = Course('C1', "Programación", 300000, 6, 20)
course_02 = Course('C2', "Diseño Gráfico", 250000, 4, 15)
course_03 = Course('C3', "Redes", 200000, 5, 10)

# Anadiendo los cursos a la escuela:

my_school.add_course(course_01)
my_school.add_course(course_02)
my_school.add_course(course_03)
my_school.add_course(course_03)
