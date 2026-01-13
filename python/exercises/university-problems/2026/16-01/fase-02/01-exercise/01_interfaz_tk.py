import tkinter as tk
import app_data

# TALLER DE BICICLETAS:
BIKE_WORKSHOP = app_data.TallerBicicletas()


# Clase Usuario con atributos predefinidos:
class User:
    """Clase Usuario"""

    def __init__(self):
        self._username = "programacion"
        self._password = "programacion"

    def validate(self, username, password):
        "Valida si el usuario y contraseña son correctos."
        return username == self._username and password == self._password


def check_user_login():
    """Valida el usuario."""
    new_user = User()

    # Capturando los datos del Login:
    lgn_user = username_input.get()
    lgn_pwd = password_input.get()

    if new_user.validate(lgn_user, lgn_pwd):
        # Si el usuario y contraseña son correctos
        output_text.set("Login...")
        return True
    # Si no muestra un texto de error en la ventana.
    output_text.set("Incorrect username or password")
    return False


def capture_input(object_input: tk.Entry):
    return object_input.get()


# =============================
# VENTANA DE LOGIN
# =============================

# Creando la ventana de login:
login_window = tk.Tk("loginWindow")
login_window.title("Login")
login_window.geometry("300x200")
login_window_label = tk.Label(master=login_window, text="LOGIN", font='Arial')
login_window_label.pack()

# DATOS DEL USUARIO:

data_user_frame = tk.Frame(master=login_window)

# Username:
username_input_label = tk.Label(
    master=data_user_frame,
    text="Username:")
username_input = tk.Entry(master=data_user_frame)

# Password:
password_input_label = tk.Label(
    master=data_user_frame,
    text="Password:")

password_input = tk.Entry(master=data_user_frame)

data_user_frame.pack()
username_input_label.pack()
username_input.pack()
password_input_label.pack()
password_input.pack()

# boton de login
login_button = tk.Button(
    master=login_window,
    text="Login",
    command=check_user_login)
login_button.pack(pady=10)

# MENSAJES DE SALIDA:

output_text = tk.StringVar()
output_label = tk.Label(
    master=login_window,
    text="Output",
    textvariable=output_text,
    fg='blue2')

output_label.pack(pady=5)

# Ejecutando la ventana de login:
login_window.mainloop()

# =============================
# VENTANA DE REGISTRO BICICLETA
# =============================


def add_bike():
    serial_user = capture_input(serial_input).upper()
    if len(serial_user) == 10:
        entry_time_user = capture_input(entry_time_input)
        entry_time_user = app_data.conv_texto_hora(entry_time_user)

        # Creando la bicicleta:
        new_bike = app_data.Bicicleta(serial_user)
        new_bike.registrar_ingreso(entry_time_user)
        new_bike.mostrar_info()
        BIKE_WORKSHOP.agregar_bicicleta(new_bike)
        BIKE_WORKSHOP.mostrar_bicicletas()

    else:
        reg_output_text.set("Algo salio mal.")


reg_bike_window = tk.Tk("regBicycleWindow")
reg_bike_window.title("Register Bike")
reg_bike_window.geometry("300x200")
reg_bike_window_label = tk.Label(
    master=reg_bike_window,
    text="REGISTER BIKE",
    font='Arial')
reg_bike_window_label.pack()

# INPUTS PARA DATOS DE LA BICICLETA:

bike_data_frame = tk.Frame()
# Serial:
serial_input_label = tk.Label(
    master=bike_data_frame,
    text="Serial:")
serial_input = tk.Entry(master=bike_data_frame)
# Hora ingreso:
entry_time_input_label = tk.Label(
    master=bike_data_frame,
    text="Entry Time:")
entry_time_input = tk.Entry(master=bike_data_frame)

bike_data_frame.pack()
serial_input_label.pack()
serial_input.pack()
entry_time_input_label.pack()
entry_time_input.pack()

# Boton de confirmar registro
reg_bike_button = tk.Button(
    master=reg_bike_window,
    text="Register",
    command=add_bike)
reg_bike_button.pack(pady=10)

# Mensajes de salida:
reg_output_text = tk.StringVar()
reg_output_label = tk.Label(
    master=reg_bike_window,
    text="Output",
    textvariable=reg_output_text,
    fg='blue2')

reg_output_label.pack(pady=5)

# Ejecutando la ventana de registro:
reg_bike_window.mainloop()
