import tkinter as tk
from tkinter import ttk
import app_core


class BikeWorkShopApp:
    """
    Clase Interfaz del Taller.
    """

    def __init__(self, root, bike_workshop):
        """
        Constructor de la aplicación.

        Args:
            root: La ventana principal de Tkinter (Tk())
        """

        # Guardamos la referencia a la ventana principal
        self.root = root

        # Configuración inicial de la ventana
        self.root.title("Bike WorkShop")

        # Definimos el tamaño de la ventana (ancho x alto)
        self.window_width = 500
        self.window_height = 400

        # Centramos la ventana en la pantalla usando nuestra función personalizada
        self.center_window(self.window_width, self.window_height)

        # Configuramos el color de fondo de la ventana
        self.root.config(bg="#f0f0f0")

        # Definimos el taller donde se guardaran los datos:
        self.bike_workshop = bike_workshop

        # Iniciamos mostrando la pantalla de Login
        self.show_login_window()

    def center_window(self, width, height):
        """
        Centra la ventana en el medio de la pantalla.

        Args:
            width: Ancho deseado de la ventana en píxeles
            height: Alto deseado de la ventana en píxeles
        """
        # Obtener el width total de la pantalla del usuario
        screen_width = self.root.winfo_screenwidth()

        # Obtener el height total de la pantalla del usuario
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición X (horizontal) para centrar
        # Dividimos entre 2 para obtener el punto medio
        x = (screen_width - width) // 2

        # Calcular la posición Y (vertical) para centrar
        y = (screen_height - height) // 2

        # Aplicar la geometría: "ANCHOxALTO+POSICION_X+POSICION_Y"
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def show_login_window(self):
        """Muestra la pantalla principal de menu."""

        # Limpiamos la ventana:
        self.clean_window()

        # Definiendo el nuevo tiulo de la venana:
        self.root.title("Bike WorkShop | Login")

        # --- TITULO ---
        title = tk.Label(
            master=self.root,
            text="LOGIN",
            font=('Arial', 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title.pack(pady=40)

        # --- DATOS DE USUARIO ---
        user_frame = tk.Frame(master=self.root)
        user_frame.pack(pady=10)

        # --- ENTRADA DE USUARIO ---
        username_label = tk.Label(
            master=user_frame,
            text="Username:",
            font=('Arial', 10, "bold"),
            bg="#f0f0f0"
        )

        username_label.grid(row=0, column=1, sticky="w", padx=5, pady=10)

        self.username_entry = ttk.Entry(master=user_frame, width=20)
        self.username_entry.grid(row=0, column=2, padx=5, pady=10)

        # --- ENTRADA DE CONTRASENA ---
        password_label = tk.Label(
            master=user_frame,
            text="Password:",
            font=('Arial', 10, "bold"),
            bg="#f0f0f0"
        )

        password_label.grid(row=1, column=1, sticky="w", padx=5, pady=10)

        self.password_entry = ttk.Entry(master=user_frame, width=20)
        self.password_entry.grid(row=1, column=2, padx=5, pady=10)

        # --- LABEL PARA MENSAJES DE ERROR ---
        # Lo creamos vacío, lo usaremos para mostrar errores de validación
        self.label_error = tk.Label(
            self.root,
            text="",  # Inicialmente vacío
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="red"  # Color rojo para errores
        )
        self.label_error.pack()

        # --- FRAME PARA BOTONES ---
        frame_buttons = tk.Frame(self.root, bg="#f0f0f0")
        frame_buttons.pack(pady=20)

        # Botón para iniciar sesion.
        btn_login = ttk.Button(
            frame_buttons,
            text="Log in",
            command=self.validate_login_user,
            width=15
        )
        btn_login.pack(padx=10)

    def show_menu_window(self):
        """Muestra el menu principal."""

        # Limpiamos la ventana:
        self.clean_window()

        # Definiendo el nuevo tiulo de la venana:
        self.root.title("Bike WorkShop | Home")

        # --- TITULO ---
        title = tk.Label(
            master=self.root,
            text="BIKE WORKSHOP | Home",
            font=('Arial', 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title.pack(pady=20)

        # --- SUBTÍTULO ---
        subtitulo = tk.Label(
            self.root,
            text="Welcome! Select a option:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitulo.pack()

        # --- OPCIONES ---
        # Frame para botones
        options_buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        options_buttons_frame.pack(pady=20)

        # Boton registrar bicicleta:
        btn_reg_bike = ttk.Button(
            options_buttons_frame,
            text="Register Bike",
            command=self.show_reg_bike_window,
            width=30)

        btn_reg_bike.pack(pady=10)

        # Boton registrar salida bicicleta:
        btn_reg_bike_out = ttk.Button(
            options_buttons_frame,
            text="Register Bike Exit",
            width=30)

        btn_reg_bike_out.pack(pady=10)

        # Boton cerrar la sesion:
        btn_log_out = ttk.Button(
            options_buttons_frame,
            text="Log out",
            command=self.show_login_window,
            width=15)

        btn_log_out.pack(pady=50)

    def show_reg_bike_window(self):
        """Muestra la ventana de registro de Bicicletas"""

        # Limpiamos la ventana:
        self.clean_window()

        # Definiendo el nuevo tiulo de la venana:
        self.root.title("Bike WorkShop | Register Bike")

        # --- TITULO ---
        title = tk.Label(
            master=self.root,
            text="REGISTER BIKE",
            font=('Arial', 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title.pack(pady=40)

        # --- DATOS DE LA BICICLETA ---
        bike_frame = tk.Frame(master=self.root)
        bike_frame.pack(pady=10)

        # --- ENTRADA DE SERIAL ---
        serial_label = tk.Label(
            master=bike_frame,
            text="Serial:",
            font=('Arial', 10, "bold"),
            bg="#f0f0f0"
        )

        serial_label.grid(row=0, column=1, sticky="w", padx=5, pady=10)

        self.serial_entry = ttk.Entry(master=bike_frame, width=20)
        self.serial_entry.grid(row=0, column=2, padx=5, pady=10)

        # --- ENTRADA DE CONTRASENA ---
        entry_time_label = tk.Label(
            master=bike_frame,
            text="Entry Time (e. 09:30):",
            font=('Arial', 10, "bold"),
            bg="#f0f0f0"
        )

        entry_time_label.grid(row=1, column=1, sticky="w", padx=5, pady=10)

        self.time_entry = ttk.Entry(
            master=bike_frame,
            width=20)

        self.time_entry.grid(row=1, column=2, padx=5, pady=10)

        # --- LABEL PARA MENSAJES DE ERROR ---
        # Lo creamos vacío, lo usaremos para mostrar errores de validación
        self.label_reg_error = tk.Label(
            self.root,
            text="",  # Inicialmente vacío
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="red"
        )
        self.label_reg_error.pack()

        # --- FRAME PARA BOTONES ---
        frame_buttons = tk.Frame(self.root, bg="#f0f0f0")
        frame_buttons.pack(pady=20)

        # Botón para volver atrás
        btn_volver = ttk.Button(
            frame_buttons,
            text="Go back",
            command=self.show_menu_window,  # Regresa a la pantalla anterior
            width=15
        )
        # pack con side="left" coloca los widgets horizontalmente
        btn_volver.pack(side="left", padx=5)

        # Botón para Registrar la bicicleta.
        btn_register = ttk.Button(
            frame_buttons,
            text="Register",
            command=self.validate_reg_bike,
            width=15
        )
        btn_register.pack(side="left", padx=5)

    def validate_login_user(self):
        """Valida los datos del Inicio de sesion."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        admin_user = app_core.User()
        if admin_user.validate_user(username, password):
            self.show_menu_window()
            return
        self.label_error.config(text="Incorrect Username or Password :(")
        return

    def validate_reg_bike(self):
        """Valida los datos de regsitro de la bicicleta."""
        serial = self.serial_entry.get()
        entry_time = self.time_entry.get()

        if self.bike_workshop.validate_bike_input(serial, entry_time):
            self.label_reg_error.config(text="Registered Succesfully :D")
            print(self.bike_workshop.registered_bikes())
            return
        self.label_reg_error.config(text="Something went wrong :(")
        return

    def clean_window(self):
        """
        Elimina todos los widgets (elementos) de la ventana actual.
        """
        # winfo_children() retorna una lista de todos los widgets hijos
        # destroy() elimina cada widget de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()


# --- EJECUTANDO LA APLICACIÓN ---
if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando corremos este archivo directamente.
    # No se ejecuta si importamos este archivo desde otro módulo.

    # Tk() crea la ventana principal de la aplicación
    root = tk.Tk()

    # Creando un taller de bicicletas:
    my_workshop = app_core.BikeWorkShop()
    # Colocando el precio por hora del taller:
    my_workshop.set_hour_price(7000)

    # Creamos una instancia de nuestra aplicación
    # Le pasamos la ventana principal como argumento
    app = BikeWorkShopApp(root, my_workshop)

    # mainloop() inicia el bucle de eventos de Tkinter
    # Mantiene la ventana abierta y esperando interacción del usuario
    # Sin esto, la ventana se abriría y cerraría inmediatamente
    root.mainloop()
