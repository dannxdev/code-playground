import os

os.system('cls')


# ===============================================
# Clase Biblioteca
# ===============================================
class LibraryAdmin:
    """Clase Biblioteca"""

    def __init__(self):
        self._reservations = []

    def add_reservation(self, room_rsv):
        """Agrega una reservacion a la Biblioteca."""

        if self.validate_reserv(room_rsv):
            self._reservations.append(room_rsv)
            return True
        return False

    def validate_reserv(self, room_rsv):
        """Valida si un objeto es de la Clase RoomReservation"""

        return isinstance(room_rsv, RoomReservation)

    def show_reservations(self):
        """Muestra las reservaciones."""
        return self._reservations


# ===============================================
# Clase Reservar Sala
# ===============================================
class RoomReservation:
    """Clase Reservacion Sala."""

    def __init__(self):
        self._user = None
        self._start_time = None
        self._end_time = None
        self._hourly_rate = 12000

    def __repr__(self) -> str:
        return f"RoomReservation(user={self._user}, start_time={self._start_time}, end_time={self._end_time})"

    def reg_init_time(self, start_time):
        """Registra la ora de inicio."""
        if self.validate_time(start_time):
            self._start_time = start_time
            return True
        return False

    def reg_end_time(self, end_time):
        """Registra la hora de fin."""
        if self.validate_time(end_time):
            self._end_time = end_time
            return True
        return False

    def calc_payment(self):
        """Calcula el coste total."""
        diference_time = self.calc_time_diference()

        if not diference_time is None:
            total_minutes = diference_time.conv_to_minutes()

            if not total_minutes is None:
                mts_rate = self._hourly_rate / 60
                return round((total_minutes * mts_rate), 2)

        return None

    def get_user(self):
        """Obtiene el usuario."""
        return self._user

    # --- HERRAMIENTAS ---

    def validate_time(self, time):
        """Valida que la hora tenga el formato correcto."""
        if isinstance(time, Time):
            return time.validate_time()
        return False

    def arent_times_nonetype(self):
        """Valida si se han registrado horas."""
        return not self._start_time is None and not self._end_time is None

    def is_end_time_greater(self):
        """
        Valida si la hora de fin es mas grande
        que la hora de inicio
        """
        if self.arent_times_nonetype():
            init_hours = self._start_time.hours
            init_minutes = self._start_time.minutes
            end_hours = self._end_time.hours
            end_minutes = self._end_time.minutes

            if end_hours > init_hours:
                return True
            if end_hours == init_hours:
                if end_minutes > init_minutes:
                    return True
        return False

    def calc_time_diference(self):
        """
        Calcula la diferencia entre la hora de salida y la hora de ingreso.
        """

        if self.is_end_time_greater():
            if self._end_time.hours > self._start_time.hours:
                hours_dif = self._end_time.hours - self._start_time.hours
                minutes_dif = self._end_time.minutes - self._start_time.minutes

                if minutes_dif < 0:
                    hours_dif -= 1
                    minutes_dif = 60 + minutes_dif

                return Time(hours_dif, minutes_dif)

            if self._end_time.hours == self._start_time.hours:
                minutes_dif = self._end_time.minutes - self._start_time.minutes

                return Time(0, minutes_dif)

        return None


class Time:
    """Clase Hora"""

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        return f"Time(hh={self.hours}, mm={self.minutes})"

    def validate_time(self):
        """Valida si la hora cumple el formato."""
        return self.check_hours() and self.check_minutes()

    def check_hours(self):
        """Valida una hora"""

        if isinstance(self.hours, int):
            if 0 <= self.hours < 24:
                return True
        return False

    def check_minutes(self):
        """Valida los minutos"""

        if isinstance(self.minutes, int):
            if 0 <= self.minutes <= 59:
                return True
        return False

    def conv_to_minutes(self):
        """Convierte una hora a minutos totales"""
        if self.validate_time():
            return (self.hours * 60) + self.minutes
        return None


my_library = LibraryAdmin()

my_rsv = RoomReservation()
init_time = Time(12, 30)
end_time = Time(21, 0)

my_rsv.reg_init_time(init_time)
my_rsv.reg_end_time(end_time)

my_library.add_reservation(my_rsv)
my_library.show_reservations()
