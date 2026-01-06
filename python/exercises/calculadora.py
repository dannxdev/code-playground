from abc import ABC, abstractmethod
import os

os.system('cls')


# CLASE OPERACION
class Operacion(ABC):

    @abstractmethod
    def ejecutar(self, a, b):
        pass


# TIPOS DE OPERACION
class Suma(Operacion):

    def ejecutar(self, a, b):
        return a + b


class Resta(Operacion):

    def ejecutar(self, a, b):
        return a - b


class Multiplicacion(Operacion):

    def ejecutar(self, a, b):
        return a * b


class Division(Operacion):

    def ejecutar(self, a, b):
        return a / b


class Potenciacion(Operacion):
    def ejecutar(self, a, b):
        return pow(a, b)


# CLASE CALCULADORA
class Calculadora:
    def __init__(self) -> None:
        self.operaciones = {}

    def anadir_operacion(self, nombre, operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, operacion, a, b):
        if operacion not in self.operaciones:
            raise ValueError(f"La operacion '{operacion}' no esta disponible.")
        return self.operaciones[operacion].ejecutar(a, b)


# ADICION DE OPERACIONES A LA CALCULADORA:
mi_calculadora = Calculadora()
mi_calculadora.anadir_operacion("suma", Suma())
mi_calculadora.anadir_operacion("resta", Resta())
mi_calculadora.anadir_operacion("multiplicacion", Multiplicacion())
mi_calculadora.anadir_operacion("division", Division())
mi_calculadora.anadir_operacion("potenciacion", Potenciacion())

print(mi_calculadora.calcular("suma", 12, 3))
print(mi_calculadora.calcular("resta", 12, 3))
print(mi_calculadora.calcular("multiplicacion", 12, 3))
print(mi_calculadora.calcular("division", 12, 3))
print(mi_calculadora.calcular("potenciacion", 12, 3))
