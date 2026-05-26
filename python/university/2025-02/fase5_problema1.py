import os
os.system('cls')


class School:

    def __init__(self) -> None:
        self.courses = []
        self.students = []
        self.payment_methods = {1: "Completo", 2: "Mensual"}

    def search_course(self, course_id):

        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def show_courses(self):

        print("OFERTA DE CURSOS:\n")
        for course in self.courses:
            course.show_info()

    def add_courses(self, course):
        if not course in self.courses:
            self.courses.append(course)
            return True
        return False

    def add_student(self, student):
        if not student in self.students:
            self.students.append(student)
            return True
        return False

    def validate_student_id(self, student_id):

        id_found = False
        for student in self.students:
            if student_id == student.student_id:
                id_found = True

        return id_found

    def show_students(self):
        if len(self.students) > 0:
            print("ESTUDIANTES MATRICULADOS:\n")
            for student in self.students:
                student.show_info()
        else:
            print("Ningun estudiante registrado.")


class Course:

    def __init__(self, course_id, course_name, monthly_price, duration, discount) -> None:
        self.course_id = course_id
        self.course_name = course_name
        self.monthly_price = Payment(monthly_price)
        self.duration = duration
        self.discount = discount

    def show_info(self):
        print(
            f"ID Curso: {self.course_id}\n- Nombre: {self.course_name}\n- Precio por mes: ${self.monthly_price.price}\n- Duración (Meses): {self.duration}\n- Descuento (Pago Completo): {self.discount}%\n")

    def show_payment_method(self):
        print(
            f"\nModalidades de pago:\n\nCurso: {self.course_name}\n1. Pago completo ({self.discount}% de descuento): ${self.calc_full_payment()}\n2. Pago mensual (por {self.duration} meses): ${self.monthly_price.price}")

    def calc_full_payment(self):
        return self.monthly_price.calc_discount(self.discount)


class Student:

    def __init__(self, student_id, student_name, course_id, payment_method) -> None:
        self.student_id = student_id
        self.student_name = student_name
        self.course_id = course_id
        self.payment_method = payment_method

    def show_info(self):
        print(
            f"ID Estudiante: {self.student_id}\n- Nombre: {self.student_name}\n- ID Curso Matriculado: {self.course_id}\n- Método de pago Elegido: {self.payment_method}\n")


class Payment:

    def __init__(self, price) -> None:
        self.price = price

    def calc_increase(self, percent):
        if percent > 0:
            sub_price = self.price * (percent/100)
            return self.price + sub_price
        return float(0)

    def calc_discount(self, percent):
        if percent > 0:
            sub_price = self.price * (percent/100)
            return self.price - sub_price
        return float(0)


def registration(school: School):
    """Registra a los estudiantes en la escuela."""


if __name__ == "__main__":

    # Creando la escuela:
    unad_school = School()

    # Cursos:
    programacion = Course('C1', "Programación", 300000, 6, 20)
    diseno_grafico = Course('C2', "Diseño Gráfico", 250000, 4, 15)
    redes = Course('C3', "Redes", 200000, 5, 10)

    # Añadiendo los cursos:
    unad_school.add_courses(programacion)
    unad_school.add_courses(diseno_grafico)
    unad_school.add_courses(redes)

    registration(unad_school)

    unad_school.show_students()
