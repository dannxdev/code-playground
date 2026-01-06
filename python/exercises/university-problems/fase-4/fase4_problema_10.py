# Problema 10: La universidad UNAD desea llevar un registro de 100
# estudiantes deportistas vinculados a las selecciones de la universidad.
# Existen 3 selecciones(Código-Nombre) 1015-Futbol, 1030-
# Basketball, 1045-Ciclismo.
# De cada estudiante se conoce la: cédula, sexo(1. Mujer, 2.
# Hombre), Edad, código de la selección a la que pertenece.
# Realice las siguientes funciones:
# Llenado de la matriz
# Mostrar la matriz
# Determine el porcentaje de hombres y mujeres de toda la matriz.
# Determine el número de deportistas por cada selección.
# NOTA:
# • Para los ejercicios en los cuales no se coloca de forma explícita
# que función debe ser implementada el estudiante tendrá
# libertad de codificar al menos una función(el estudiante debe
# revisar si la función retorna o no valores como también si se
# debe enviar parámetros o no).
# • Si el estudiante desea o cree que se debe utilizar más de una
# función lo puede hacer.
# • Se deben realizar las validaciones pertinentes para asegurar el
# correcto funcionamiento de los programas teniendo en cuenta
# aspectos como: que el usuario no pueda ingresar una letra
# donde se esperan números, validar que el usuario solo pueda
# ingresar valores positivos donde sea necesario, que el usuario
# solo pueda ingresar números que se encuentren en
# determinado rango, etc.

import os
import re
os.system('cls')


class TeamsDatabase:
    def __init__(self) -> None:
        self.teams = {}

    def add_team(self, team: Team):
        if not team.team_code in self.teams:
            self.teams[team.team_code] = team
            return True
        return False

    def show_statistics(self):
        print("\nEstadísticas Inscritos:")
        males = 0
        females = 0
        for id in self.teams:
            students_linked_list = self.teams[id].students_linked

            print(
                f"- Selección: {self.teams[id].team_name} - Inscritos: {len(students_linked_list)}")
            for student in students_linked_list:
                if student.gender == "M":
                    males += 1
                else:
                    females += 1

        total_genders = males + females

        percent_males = round((males*100)/total_genders, 2)
        percent_females = round((females*100)/total_genders, 2)

        print(
            f"Total Inscritos: {total_genders}\nMujeres: {females} - {percent_females}%\nHombres: {males} - {percent_males}%\n")


class Team:

    def __init__(self, team_code: int, team_name: str) -> None:
        self.team_code = team_code
        self.team_name = team_name
        self.students_linked = []

    def add_student(self, student: Student):
        if student not in self.students_linked:
            self.students_linked.append(student)
            return True
        return False

    def delete_student(self, student):
        if student in self.students_linked:
            self.students_linked.remove(student)
            return True
        return False


class Student:

    def __init__(self, document: int, gender: str, age: int) -> None:
        self.document = document
        self.gender = gender
        self.age = age


# Creando los equipos (selecciones)
team_football = Team(1015, "Futbol")
team_basketball = Team(1030, "Basketball")
team_cycling = Team(1045, "Ciclismo")

teams_db = TeamsDatabase()
teams_db.add_team(team_football)
teams_db.add_team(team_basketball)
teams_db.add_team(team_cycling)


def validate_age(age):
    if isinstance(age, int):
        return age >= 14
    return False


def validate_gender(gender):
    return gender.upper() in ("M", "F")


def validate_student_id(id):
    return isinstance(id, int) and id > 9999999


def registration_students():
    while True:
        try:
            id_student = int(input("Documento: "))
            break
        except Exception as e:
            print("Error: ", e)

    while True:
        gender_student = input("Genero (M/F): ").upper()
        if validate_gender(gender_student):
            break

    while True:
        try:
            age_student = int(input("Edad: "))
            if validate_age(age_student):
                break
        except Exception as e:
            print("Error: ", e)

    print("\nEQUIPOS")

    for t in teams_db.teams:
        print(f"Codigo: {t} - {teams_db.teams[t].team_name}")
    print("\n")

    while True:
        try:
            code_team = int(input("Código Equipo: "))
            if code_team in teams_db.teams:
                break
        except Exception as e:
            print("Error: ", e)

    new_student = Student(id_student, gender_student, age_student)

    if teams_db.teams[code_team].add_student(new_student):
        print("\nRegistro Completado Exitosamente")
        return True
    return False


def main():

    def menu():
        print("REGISTRO DE SELECCIONES\n\n1. Registrar Estudiante a un equipo.\n2. Ver Estadísticas Equipos.")
