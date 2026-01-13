# CLASE TALLER:
class TallerBicicletas:
    """Clase Taller"""

    def __init__(self):
        # Diccionario que almacenara las bicicletas respecto al serial.
        self._bicicletas = {}

    def agregar_bicicleta(self, bicicleta):
        """Agrega una bicicleta al taller."""

        if isinstance(bicicleta, Bicicleta):
            if not bicicleta in self._bicicletas:
                self._bicicletas[bicicleta.obtener_serial()] = bicicleta
                print("Bicicleta añadida exitosamente.")
                return True
            print("La bicicleta ya existe en el taller.")

    def buscar_bicicleta(self, serial):
        """Busca una bicicleta en el taller."""

        if len(self._bicicletas) > 0:
            if serial in self._bicicletas:
                return self._bicicletas[serial]

        return None

    def registrar_salida_taller(self, serial, hora):
        """Registra la salida."""

        if isinstance(hora, Hora):
            bicicleta = self.buscar_bicicleta(serial)

            if not bicicleta is None:
                bicicleta.registrar_salida(hora)
                self._bicicletas[serial] = bicicleta
                return True
        return False

    def mostrar_bicicletas(self):
        if len(self._bicicletas) > 0:
            print(self._bicicletas)


# CLASE BICICLETA:
class Bicicleta:
    """Clase Taller de Bicicletas."""

    def __init__(self, serial):
        # Inicializando la instancia de la clase:
        self._serial = serial
        self._costo_hora = float(5000)
        self._hora_ingreso = None
        self._hora_salida = None

    def mostrar_info(self):
        """Muestra la information de la Bicicleta."""

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
        "Obtiene el serial de la bicicleta."
        return self._serial


# CLASE HORA:
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


def conv_texto_hora(hora_texto):
    """Valida si un texto es hora."""

    if isinstance(hora_texto, str):
        if ":" in hora_texto:
            hora, minutos = hora_texto.split(":")
            try:
                f_hora = Hora(int(hora), int(minutos))
                return f_hora
            except Exception as e:
                print(f"Error al convertir la hora: {e}")
    return None
