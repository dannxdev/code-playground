import os

os.system('cls')


class University:

    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.def_cant_notes = None

    def add_student(self, student):
        """Anade un estudiante al registro"""

        if isinstance(student, Student):
            if not student in self.students:
                self.students.append(student)
                return True
        return False

    def ranking_students(self):
        """Genera un ranking de estudiantes respecto
        a sus promedios."""

        if len(self.students) > 0:
            name_avg = {}
            for student in self.students:
                name_avg[student.name] = student.calc_avg()

            only_avgs = list(name_avg.values())
            sort_avgs = sorted(only_avgs, reverse=True)
            max_avg = max(sort_avgs)
            global_avg = sum(sort_avgs) / len(sort_avgs)

            ranking = {}
            sort_names = []

            for note_avg in sort_avgs:
                for name, avg in name_avg.items():
                    if avg == max_avg:
                        ranking['best_avg'] = name

                    if note_avg == avg:
                        if not name in sort_names:
                            sort_names.append(name)

            ranking['sorted_names'] = sort_names
            ranking['global_avg'] = global_avg

            print(name_avg)
            print(ranking)
            return ranking

        print("No se ha registrado ningun estudiante.")
        return None

    def set_empty_register(self):
        """Vacia los registros de la univeridad."""
        self.students = []
        self.def_cant_notes = None

        return True


class Student:

    def __init__(self, name: str):
        self.name = name
        self.notes = []

    def info_student(self):
        """Muestra la info del estudiante"""

        print(f"Nombre: {self.name}, Notas: {self.notes}")

    def add_notes(self, cant_notes):
        """Anade notas del estudiante"""

        if isinstance(cant_notes, int) and cant_notes > 0:
            print(f"Notas de {self.name}:")
            for index in range(1, cant_notes + 1):
                while True:
                    try:
                        note = float(input(f"Nota {index}: "))
                        if 0 <= note <= 100:
                            break
                        print("Debe ingresar una nota en el rango de 0 y 100.")
                    except ValueError:
                        print("Ha escrito una nota no valida.")

                # agrega cada nota ingresada a la lista.
                self.notes.append(note)

            return True

        raise ValueError(
            f"La cantidad de notas ingresada {cant_notes, type(cant_notes)} debe ser entero.")

    def calc_avg(self):
        """Calcula el promedio de notas."""

        return sum(self.notes) / len(self.notes)


def students_register(university):
    """Registra los estudiantes y sus datos."""

    if isinstance(university, University):
        if university.def_cant_notes is None:
            while True:
                try:
                    cant = int(input("Cantidad Notas Predefinido (1-5): "))
                    if 0 < cant <= 5:
                        university.def_cant_notes = cant  # type: ignore
                        break
                    print('Debe ser una cantidad mayor a 0 y menor que 10.')
                except ValueError:
                    print("Ingrese solo numeros por favor.")

        while True:
            print("Ingrese los datos del estudiante:")

            student_name = input("Nombre: ").capitalize()
            new_student = Student(student_name)
            new_student.add_notes(university.def_cant_notes)

            if university.add_student(new_student):
                new_student.info_student()
                print("Estudiante registrado exitosamente.")

            while True:
                user_option = input(
                    "\nRegistrar otro estudiante? (s/n): ").lower()
                if user_option in ('s', 'n'):
                    break
                print(f"Opcion '{user_option}' no valida.")

            if user_option == 'n':
                print('Volviendo al menu principal.\n')
                break

    else:
        raise ValueError(
            f"Instancia de universidad {university, type(university)} no valida.")


def menu():
    """
    Muestra las opciones del menu principal, y recibe la opción
    escogida por el usuario y la retorna.
    """

    print("REGISTRO DE NOTAS\n")
    print("1. Registrar Notas\n2. Generar Ranking\n3. Vaciar registros.\n4. Salir")

    while True:
        opcion = input("\nSeleccione una opción (1-3): ")
        if opcion in ("1", "2", "3", "4"):
            return int(opcion)

        print("Ingrese una opción valida.")


def execute_program():
    """Ejecuta el programa"""

    unad = University('UNAD')

    while True:
        op_user = menu()

        if op_user == 1:
            students_register(unad)

        elif op_user == 2:
            unad.ranking_students()

        elif op_user == 3:
            unad.set_empty_register()

        elif op_user == 4:
            print("Abandonando el programa.")
            break


execute_program()
