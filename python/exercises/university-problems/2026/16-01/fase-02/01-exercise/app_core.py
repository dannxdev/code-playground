import os
os.system('cls')


# ===========================================================================
# CLASE USUARIO
# ===========================================================================

class User:
    """Clase Usuario"""

    def __init__(self):
        self._username = ''
        self._password = ''

    def validate_user(self, username, password):
        """Valida si las credenciales ingresadas son correctas."""
        return self._username == username and self._password == password


# ===========================================================================
# CLASE TALLER DE BICICLETAS
# ===========================================================================
class BikeWorkShop:
    """
    Clase Taller de Bicicletas.
    """

    def __init__(self):
        # Constructor que crea un diciionario vacio
        # que almacenara las bicicletas registradas con el formato
        # {serial: bicileta}
        self._hour_price = None
        self._registered_bikes = {}

    def registered_bikes(self):
        """
        Muestra el diccionario de Bicicletas
        registradas en el Taller.
        """

        return self._registered_bikes

    def register_bike(self, bike):
        """
        Agrega una bicicleta al registro.
        """
        if isinstance(bike, Bike):
            sn_bike = bike.get_serial()
            if not self.serial_in_workshop(sn_bike):
                # Si el serial de la bicicleta no esta en el Taller:
                if not self._hour_price is None:
                    # Si el precio por hora no esta definido.
                    bike.reg_hour_price(self._hour_price)
                # Guarda la bicicleta en el diccionario de registro.
                self._registered_bikes[sn_bike] = bike
                return True
        return False

    def set_hour_price(self, hour_price):
        """
        Coloca el precio por Hora de permanencia 
        en el taller.
        """

        if isinstance(hour_price, (float, int)):
            if isinstance(hour_price, int):
                hour_price = float(hour_price)
            self._hour_price = hour_price
            return True
        return False

    def serial_in_workshop(self, serial):
        """Valida si un serial existe en el Taller"""
        return serial in self._registered_bikes

    def validate_bike_input(self, serial, entry_time):
        """
        Hace el proceso de registro solo si los datos
        son correctos.
        """

        # Validando que las entradas no contengan espacios.
        if validate_input(serial) and validate_input(entry_time):
            if len(serial) >= 8:
                serial = serial.upper()

                if not self.serial_in_workshop(serial):
                    entry_time = text_to_hour(entry_time)

                    if not entry_time is None:
                        new_bike = Bike(serial)
                        if new_bike.reg_entry_time(entry_time):
                            return self.register_bike(new_bike)

        return False

    def validate_reg_bike_exit(self, serial, exit_time):
        """
        Hace el proceso de registro solo si los datos
        son correctos.
        """

        # Validando que las entradas no contengan espacios.
        if validate_input(serial) and validate_input(exit_time):
            if len(serial) >= 8:
                serial = serial.upper()
                if self.serial_in_workshop(serial):
                    found_bike = self._registered_bikes[serial]
                    exit_time = text_to_hour(exit_time)

                    if not exit_time is None:
                        if found_bike.reg_exit_time(exit_time):
                            self._registered_bikes[serial] = found_bike
                            total_price = found_bike.calc_total_price()

                            if not total_price is None:
                                return total_price

        return False


class Bike:
    """
    Clase Bicicleta
    """

    def __init__(self, serial_number):
        # Constructor de la instancia Bicicleta
        self._serial_number = serial_number
        self._hour_price = None
        self._entry_time = None
        self._exit_time = None

    def __repr__(self) -> str:
        # Representacion del objeto Bicicleta
        return f"Bicicleta(SN={self._serial_number}, precio_hora={self._hour_price}, hora_entrada={self._entry_time}, hora_salida={self._exit_time})"

    def bike_info(self):
        """Retorna la informacion de la Bicicleta."""

        return f"""
    Informacion de la bicicleta:
    
    - SN: {self._serial_number}
    - Precio por hora: {self._hour_price}
    - Hora de ingreso: {self._entry_time}
    - Hora de salida: {self._exit_time}
    """

    def reg_hour_price(self, hour_price):
        """
        Coloca el precio por hora de permanencia 
        en el taller a la bicicleta.
        """
        if isinstance(hour_price, float):
            self._hour_price = hour_price
            return True
        return False

    def reg_entry_time(self, entry_time):
        """
        Registra la hora de ingreso de la Bicicleta.
        """
        if isinstance(entry_time, Hour):
            self._entry_time = entry_time
            return True
        return False

    def reg_exit_time(self, exit_time):
        """
        Registra la hora de salida de la Bicicleta.
        """
        if isinstance(exit_time, Hour):
            if self.is_greater_exit_time(exit_time):
                self._exit_time = exit_time
                return True
        return False

    def get_serial(self):
        """
        Retorna el serial de la Bicicleta.
        """
        return self._serial_number

    def is_greater_exit_time(self, exit_time):
        """
        Verifica que la hora de salida sea mayor a
        la hora de ingreso de la bicicleta.
        """
        if not self._entry_time is None:
            if isinstance(exit_time, Hour):
                if exit_time.hours > self._entry_time.hours:
                    return True
                if exit_time.hours == self._entry_time.hours:
                    if exit_time.minutes > self._entry_time.minutes:
                        return True
        return False

    def calc_time_diference(self):
        """
        Calcula la diferencia entre la hora de salida y la hora de ingreso.
        """

        if not self._entry_time is None and not self._exit_time is None:
            if self._exit_time.hours > self._entry_time.hours:
                hours_dif = self._exit_time.hours - self._entry_time.hours
                minutes_dif = self._exit_time.minutes - self._entry_time.minutes

                if minutes_dif < 0:
                    hours_dif -= 1
                    minutes_dif = 60 + minutes_dif

                return Hour(hours_dif, minutes_dif)

            if self._exit_time.hours == self._entry_time.hours:
                minutes_dif = self._exit_time.minutes - self._entry_time.minutes

                return Hour(0, minutes_dif)

        return None

    def calc_total_price(self):
        """
        Calcula el precio total.
        """

        time_diference = self.calc_time_diference()

        if not time_diference is None and not self._hour_price is None:
            minute_price = self._hour_price / 60

            return round(time_diference.conv_total_minutes() * minute_price)

        return None


class Hour:
    """
    Clase Hora
    """

    def __init__(self, hours, minutes):
        # Constructor de la instancia Hora
        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        # Representacion de la instancia Hora
        hours = self.hours
        minutes = self.minutes

        if hours < 10:
            hours = "0" + str(hours)
        if minutes < 10:
            minutes = "0" + str(minutes)

        return f"{hours}:{minutes}"

    def conv_total_minutes(self):
        """
        Convierte la hora en minutos totales.
        """

        return (self.hours * 60) + self.minutes


# ===========================================================================
# FUNCIONES DE HERRAMIENTAS
# ===========================================================================

def validate_input(text):
    """
    Valida que una entrada de usuario sea un text valido.
    """
    # Verificar que el text sea una cadena de texto válida:
    if not isinstance(text, str):
        return False
    # Verificar que no esté vacía
    if len(text) == 0:
        return False
    # Eliminar todos los tipos de espacios en blanco (espacios, tabs, saltos de línea, espacios Unicode)
    clean_text = text.strip()
    # Verificar que después de eliminar espacios al inicio y final, aún tenga contenido
    if len(clean_text) == 0:
        return False
    # Verificar que NO contenga ningún espacio en blanco en el texto
    for char in clean_text:
        if char.isspace():
            return False
    # Si pasó todas las validaciones, la entrada es válida
    return True


def text_to_hour(hour_text):
    """
    Convierte una texto del tipo 'HH:MM' a instancia
    de la clase Hora.
    """

    if isinstance(hour_text, str):
        if validate_input(hour_text):
            if len(hour_text) == 5 and ":" in hour_text:
                hours_sep, minutes_sep = hour_text.split(":")

                try:
                    hours_sep = int(hours_sep)
                    minutes_sep = int(minutes_sep)
                except ValueError:
                    return None

                hours_ok = 0 <= hours_sep <= 23
                minutes_ok = 0 <= minutes_sep <= 59

                if hours_ok and minutes_ok:
                    return Hour(hours_sep, minutes_sep)

    return None
