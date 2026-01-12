import os

os.system('cls')

# CLASSES:


class School:
    """Clase Escuela"""

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

    def add_student(self, student):
        """Agrega un estudiante a la escuela."""

        if isinstance(student, Student):
            if not student.student_id in self.school_courses:
                # Si el estudiante no existe en la escuela aun:
                self.school_students[student.student_id] = student
                print(
                    f"✅ Student '{student.student_name}' added to the '{self.school_name}' school.")
                return True
            # Si el estudiante ya se encuentra inscrito:
            print(
                f"⚠️ Student '{student.student_name}' already exists in the '{self.school_name}' school")
            return False

        # Si el argumento no es de la instancia Student:
        raise ValueError('arg: student must be Student class instance.')

    def show_all_school_courses(self):
        """Muestra todos los cursos de la escuela."""

        if len(self.school_courses) > 0:

            print("CURSOS OFERTADOS:\n")

            for crs in self.school_courses.values():
                crs.show_course_info()
                print("\n")

    def generate_student_id(self):
        """Genera un ID unico nuevo para un estudiante."""

        new_id = 100

        while 'E' + str(new_id) in self.school_students:
            new_id += 1

        return 'E' + str(new_id)

    # Método que valida y registra a los estudiantes:
    def register_students(self):
        """
        Pide los datos del estudiante a registrar
        y hace el registro
        """

        print("REGISTRO DE ESTUDIANTES")

        while True:
            print("Ingrese los datos del estudiante:")

            reg_student_id = self.generate_student_id()
            print(f"ID Estudiante asignado: {reg_student_id}")

            reg_student_name = input("Nombre del estudiante: ")

            # Mostrando los cursos para eleccion:
            print("\n")
            self.show_all_school_courses()

            while True:
                reg_student_course_id = input(
                    "ID del curso a registrar: ").upper()
                if reg_student_course_id in self.school_courses:
                    break
                print("ID de curso desconocido. Intente de nuevo.")

            while True:
                reg_student_payment_method = input("ID Metodo de pago: ")
                if reg_student_payment_method in self.school_payment_methods:
                    break
                print("ID de método de pago desconocido. Intente de nuevo.")

            new_student = Student(
                reg_student_id, reg_student_name, reg_student_course_id, reg_student_payment_method)

            # Mostrando la info del estudiante a registrar:
            print("\n")
            new_student.show_student_info()


class Course:
    """Clase Curso"""

    def __init__(self, course_id, course_name, course_monthly_price, course_duration, course_fp_discount) -> None:
        self.course_id = course_id
        self.course_name = course_name
        self.course_monthly_price = course_monthly_price
        self.course_duration = course_duration
        self.course_fp_discount = course_fp_discount

    def show_course_info(self):
        """Muestra la informacion del curso."""

        print(f"ID Curso: {self.course_id}")
        print(f"- Nombre: {self.course_name}")
        print(f"- Costo mensual: {self.course_monthly_price}")
        print(f"- Duración (meses): {self.course_duration}")
        print(f"- Descuento Pago Completo: {self.course_fp_discount}%")


class Student:
    """Clase Estudiante"""

    def __init__(self, student_id, student_name, student_course_id, student_payment_method) -> None:
        self.student_id = student_id
        self.student_name = student_name
        self.student_course_id = student_course_id
        self.student_payment_method = student_payment_method

    def show_student_info(self):
        """Muestra la informacion del estudiante."""

        print(f"ID Estudiante: {self.student_id}")
        print(f"- Nombre: {self.student_name}")
        print(f"- ID Curso: {self.student_course_id}")
        print(f"- Metodo de pago: {self.student_payment_method}")


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


my_school.register_students()
