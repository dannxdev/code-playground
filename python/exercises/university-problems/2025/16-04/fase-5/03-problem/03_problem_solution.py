# 03 Problem Solution
import os

os.system('cls')


class Company:
    """Clase empresa"""

    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.employees = []
        self.year_bonus = {1: 0.0, 2: 0.05, 3: 0.1, 4: 0.15, 5: 0.2}

    def add_employee(self, employee):
        """Anade un empleado a la empresa"""

        if isinstance(employee, Employee):
            if not employee in self.employees:
                self.employees.append(employee)
                return True

        return False

    def verify_rating(self, punt_num):
        """Valida si la calificacion es valida."""
        return punt_num in self.year_bonus

    def individual_detail(self):
        """El salario anual total para cada empleado (sumando el salario base y el bono)."""

        if len(self.employees) > 0:

            for empl in self.employees:
                empl_total_pay = empl.calc_year_bonus(
                    self.year_bonus[empl.employee_rating])
                print(
                    f"Empleado: {empl.employee_name}\n- Valor bono: {(self.year_bonus[empl.employee_rating]) * 100}%\n- Total Anual: ${empl_total_pay}\n")

        else:
            print('No hay ningun empleado registrado.')

    def count_summary(self):
        """Muestra la suma total de todos los salarios."""

        if len(self.employees) > 0:

            count_total = 0

            for employee in self.employees:
                empl_rating = employee.employee_rating
                empl_percent = self.year_bonus[empl_rating]
                empl_pay = employee.calc_year_bonus(empl_percent)
                count_total += empl_pay

            print(f"Resumen Contable: ${count_total}")

        else:
            print('No hay ningun empleado registrado.')


class Employee:
    """Clase empleado"""

    def __init__(self, employee_id, employee_name, employee_dept, employee_pay, employee_rating) -> None:
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_dept = employee_dept
        self.employee_pay = employee_pay
        self.employee_rating = employee_rating

    def calc_year_bonus(self, percent_value):
        """Calcula el bono anual segun rating."""

        total_year_pay = self.employee_pay * 12

        if percent_value > 0.0:
            bonus_pay = total_year_pay * percent_value
            total_year_pay += bonus_pay

        return total_year_pay


emssanar = Company('Emssanar')

employee1 = Employee('1234', 'Juancito', 'Finanzas', 1500000, 3)
employee2 = Employee('1235', 'Maria', 'Talento Humano', 1500000, 4)
employee3 = Employee('1236', 'Pedrito', 'Marketing', 1500000, 5)
employee4 = Employee('1237', 'Pablito', 'Produccion', 1500000, 2)

emssanar.add_employee(employee1)
emssanar.add_employee(employee2)
emssanar.add_employee(employee3)
emssanar.add_employee(employee4)

emssanar.individual_detail()
emssanar.count_summary()
