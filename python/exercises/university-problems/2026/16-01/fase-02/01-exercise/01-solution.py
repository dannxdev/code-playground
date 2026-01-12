import tkinter as tk
import os
import datetime as dt


class TallerBicicletas:
    """Clase Taller"""

    def __init__(self, nombre_taller):
        self._nombre_taller = nombre_taller
        self._bicicletas = []


class Bicicleta:
    """Clase Taller de Bicicletas."""

    def __init__(self, serial):
        # Inicializando la instancia de la clase:
        self._serial = serial
        self._costo_hora = float(5000)
        self._hora_ingreso = None
        self._hora_salida = None

    def mostrar_info(self):
        """Muestra la informacion de la Bicicleta."""

        print(f"Serial: {self._serial}")
        print(f"Costo Hora: {self._costo_hora}")
        print(f"Hora Ingreso: {self._hora_ingreso}")
        print(f"Hora Salida: {self._hora_salida}")

    def registrar_ingreso(self, hora_ingreso):
        """Registra la hora de ingreso de una bicicleta."""
        self._hora_ingreso = hora_ingreso

    def registrar_salida(self, hora_salida):
        """Registra la hora de ingreso de la bicicleta."""
        self._hora_salida = hora_salida

    def calcular_total(self):
        """Calcula el coste final dependiendo de
        la hora de salida"""
        if not self._hora_ingreso is None and not self._hora_salida is None:
            df_horas = calc_dif_horas(self._hora_ingreso, self._hora_salida)
            minutos_totales = df_horas.convertir_a_minutos()
            costo_por_minuto = self._costo_hora / 60

            return round((costo_por_minuto * minutos_totales), 2)

        return None

    def obtener_serial(self):
        "Muestra el serial de la bicicleta en consola."
        print(f"SN: {self._serial}")


class Hora:
    """Clase Hora"""

    def __init__(self, horas, minutos) -> None:

        if self.validar_hora(horas, minutos):
            self.horas = horas
            self.minutos = minutos

        else:
            raise ValueError("Formato de hora no valido.")

    def validar_hora(self, horas, minutos):
        """Verifica si la hora ingresada es correcta"""
        hora_ok = isinstance(horas, int) and 0 <= horas <= 23
        minutos_ok = isinstance(minutos, int) and 0 <= minutos <= 59
        return hora_ok and minutos_ok

    def __repr__(self) -> str:
        horas = self.horas
        minutos = self.minutos

        if self.horas < 10:
            horas = "0" + str(self.horas)

        if self.minutos < 10:
            minutos = "0" + str(self.minutos)

        return f"{horas}:{minutos}"

    def convertir_a_minutos(self):
        """Convierte las horas a minutos totales."""
        return (self.horas * 60) + self.minutos


def calc_dif_horas(hora_ingreso, hora_salida):
    """
    Calcula la diferencia entre la hora de salida y la hora de ingreso.
    """
    if isinstance(hora_ingreso, Hora) and isinstance(hora_salida, Hora):

        if hora_salida.horas > hora_ingreso.horas:
            dif_horas = hora_salida.horas - hora_ingreso.horas
            dif_minutos = hora_salida.minutos - hora_ingreso.minutos

            hh = dif_horas
            mm = dif_minutos

            if dif_minutos < 0:
                hh -= 1
                mm = 60 + dif_minutos

            return Hora(hh, mm)

        if hora_salida.horas == hora_ingreso.horas:
            if hora_salida.minutos > hora_ingreso.minutos:
                mm = hora_salida.minutos - hora_ingreso.minutos

                return Hora(0, mm)

        raise ValueError(
            'La hora de salida debe ser mayor a la hora de ingreso.')

    raise ValueError('Formato de hora no valido.')


mi_taller = TallerBicicletas('BiciTaller')

mi_bicicleta = Bicicleta('B7363HJV9837')

mi_bicicleta.mostrar_info()

mi_bicicleta.registrar_ingreso(Hora(12, 40))
mi_bicicleta.registrar_salida(Hora(19, 57))

mi_bicicleta.mostrar_info()

print(mi_bicicleta.calcular_total())
