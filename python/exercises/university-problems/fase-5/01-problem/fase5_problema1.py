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

        print("ESTUDIANTES MATRICULADOS:\n")
        for student in self.students:
            student.show_info()


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


unad_school = School()

# Cursos:
programacion = Course('C1', "Programación", 300000, 6, 20)
diseno_grafico = Course('C2', "Diseño Gráfico", 250000, 4, 15)
redes = Course('C3', "Redes", 200000, 5, 10)

# Añadiendo los cursos:
unad_school.add_courses(programacion)
unad_school.add_courses(diseno_grafico)
unad_school.add_courses(redes)


def registration(school: School):

    while True:
        try:
            reg_num = int(input('Numero de estudiantes a inscribir: '))
            if reg_num > 0:
                break
            print('Debe ingresar un valor mayor a cero.')
        except ValueError:
            print("Ha ingresado un valor no valido")

    for reg in range(1, reg_num + 1):
        print(f'Registro {reg}:')

        while True:
            reg_student_id = input('ID del Estudiante: ').upper()
            if not school.validate_student_id(reg_student_id):
                break
            print('El ID ingresado ya esta registrado, ingrese uno diferente.')

        reg_student_name = input('Nombre del Estudiante: ').capitalize()

        school.show_courses()

        while True:
            reg_course_id = input(
                'Código del curso al que se inscribe: ').upper()
            if not school.search_course(reg_course_id) is None:
                break
            print(f"No se encontró el curso con el código '{reg_course_id}'")

        reg_selected_course = school.search_course(reg_course_id)
        reg_selected_course.show_payment_method()  # type: ignore

        while True:
            try:
                reg_payment_method = int(
                    input("Elija un método de pago (1-2): "))
                if reg_payment_method in school.payment_methods:
                    break
                print('Ha elegido una opción no valida')
            except ValueError:
                print('Ha elegido una opción no valida')

        new_student = Student(reg_student_id, reg_student_name,
                              reg_course_id, reg_payment_method)

        if school.add_student(new_student):
            print('El estudiante se ha registrado exitosamente')

        else:
            print("Ha ocurrido un error al realizar el registro.")


registration(unad_school)


unad_school.show_students()
