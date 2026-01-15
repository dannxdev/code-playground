import tkinter as tk
from tkinter import ttk

import app_source as app_src


class BikeWorkShopApp:
    """
    Clase que gestiona toda la aplicación.
    """

    def __init__(self, root_window):
        """Constructor de la aplicación."""

        self.root = root_window
        # Configuración inicial de la ventana
        self.root.title("Bike WorkShop")

        # Definimos el tamaño de la ventana (ancho x alto)
        self.ancho_ventana = 500
        self.alto_ventana = 400

        # Centramos la ventana en la pantalla usando nuestra función personalizada
        self.centrar_ventana(self.ancho_ventana, self.alto_ventana)

        # Configuramos el color de fondo de la ventana
        self.root.config(bg="#f0f0f0")

        # Iniciamos mostrando la pantalla de bienvenida
        self.mostrar_pantalla_menu()

    def centrar_ventana(self, ancho, alto):
        """
        Centra la ventana en el medio de la pantalla.

        Args:
            ancho: Ancho deseado de la ventana en píxeles
            alto: Alto deseado de la ventana en píxeles
        """
        # Obtener el ancho total de la pantalla del usuario
        ancho_pantalla = self.root.winfo_screenwidth()
        # Obtener el alto total de la pantalla del usuario
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular la posición X (horizontal) para centrar
        # Dividimos entre 2 para obtener el punto medio
        x = (ancho_pantalla - ancho) // 2

        # Calcular la posición Y (vertical) para centrar
        y = (alto_pantalla - alto) // 2

        # Aplicar la geometría: "ANCHOxALTO+POSICION_X+POSICION_Y"
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def limpiar_ventana(self):
        """
        Elimina todos los widgets (elementos) de la ventana actual.
        Esto es esencial antes de mostrar una nueva pantalla.
        """
        # winfo_children() retorna una lista de todos los widgets hijos
        # destroy() elimina cada widget de la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_pantalla_menu(self):
        """Muestra la pantalla de menu."""

        self.limpiar_ventana()
        self.root.title("Bike WorkShop | Menu")

        menu_window_label = tk.Label(
            master=self.root,
            text="BIKE WORKSHOP | MENU",
            font='Arial')

        menu_window_label.pack()

        # Boton de registrar bicicleta:
        reg_option_button = ttk.Button(
            master=self.root,
            text="Register Bike",
            command=self.mostrar_pantalla_registro)

        reg_option_button.pack(pady=10)

        # Boton de registrar salida bicicleta:
        reg_option_button = ttk.Button(
            master=self.root,
            text="Register Bike Exit",
            command=self.mostrar_pantalla_registrar_salida)

        reg_option_button.pack(pady=5)

    def mostrar_pantalla_registro(self):
        """Muestra la pantalla de registro de bicicletas."""

        # Limpiando la ventana:
        self.limpiar_ventana()
        self.root.title("Bike WorkShop | Register")

        reg_bike_window_label = tk.Label(
            master=self.root,
            text="REGISTER BIKE",
            font='Arial')

        reg_bike_window_label.pack()

        # INPUTS PARA DATOS DE LA BICICLETA:

        bike_data_frame = tk.Frame()
        bike_data_frame.pack()
        # Serial:
        serial_input_label = tk.Label(
            master=bike_data_frame,
            text="Serial (15):")
        serial_input_label.pack()
        self.serial_input = ttk.Entry(master=bike_data_frame)
        self.serial_input.pack()
        # Hora ingreso:
        entry_time_input_label = tk.Label(
            master=bike_data_frame,
            text="Entry Time (HH:MM):")
        entry_time_input_label.pack()
        self.entry_time_input = ttk.Entry(master=bike_data_frame)
        self.entry_time_input.pack()

        # Botón de confirmar registro
        reg_bike_button = ttk.Button(
            master=self.root,
            text="Register",
            command=self.reg_bike_action)
        reg_bike_button.pack(pady=10)

        # --- Botón Volver ---
        reg_back_button = ttk.Button(
            master=self.root,
            text="Back to menu",
            command=self.mostrar_pantalla_menu)
        reg_back_button.pack(pady=10)

        # Mensajes de salida:
        self.reg_output_text = tk.StringVar()
        reg_output_label = tk.Label(
            master=self.root,
            text="Output",
            textvariable=self.reg_output_text,
            fg='blue2')

        reg_output_label.pack(pady=5)

    # --- FUNCION MOSTRAR VENTANA DE REGISTRAR SALIDA ---
    def mostrar_pantalla_registrar_salida(self):
        """Muestra la pantalla de registrar salida de una bicicleta."""

        # Limpiando la ventana:
        self.limpiar_ventana()
        self.root.title("Bike WorkShop | Register Exit")

        reg_bike_exit_window_label = tk.Label(
            master=self.root,
            text="REGISTER EXIT BIKE",
            font='Arial')

        reg_bike_exit_window_label.pack()

        datos_bicicleta_frame = tk.Frame(self.root)
        datos_bicicleta_frame.pack()
        # Etiqueta de serial:
        serial_label = tk.Label(
            master=datos_bicicleta_frame,
            text="Serial (15):"
        )
        serial_label.pack()
        # Serial input
        self.input_reg_ext_serial = ttk.Entry(master=datos_bicicleta_frame)
        self.input_reg_ext_serial.pack()

        # Etiqueta de Hora salida:
        ext_time_label = tk.Label(
            master=datos_bicicleta_frame,
            text="Exit Time (HH:MM):"
        )
        ext_time_label.pack()
        # Hora salida input
        self.input_reg_ext_time = ttk.Entry(master=datos_bicicleta_frame)
        self.input_reg_ext_time.pack()

        # Botón de buscar serial
        reg_bike_ext_button = ttk.Button(
            master=self.root,
            text="Search bike",
            command=self.search_bike_action)
        reg_bike_ext_button.pack(pady=10)

        # Boton de volver al menu.
        # --- Botón Volver ---
        reg_back_button = ttk.Button(
            master=self.root,
            text="Back to menu",
            command=self.mostrar_pantalla_menu)
        reg_back_button.pack(pady=10)

        # Mensajes de salida:
        self.reg_ext_output_text = tk.StringVar()
        reg_ext_output_label = tk.Label(
            master=self.root,
            text="Output",
            textvariable=self.reg_ext_output_text,
            fg='blue2')

        reg_ext_output_label.pack(pady=5)

    # --- FUNCIONES DE LA INTERFAZ ---

    def search_bike_action(self):
        """Accion del boton de buscar serial."""

        get_serial_ext = self.capturar_input(self.input_reg_ext_serial).upper()
        get_time_ext = self.capturar_input(self.input_reg_ext_time)
        if app_src.reg_salida_bicicleta(get_serial_ext, get_time_ext):
            self.reg_ext_output_text.set("Changes Applied :D")

            app_src.TALLER_BICICLETAS.mostrar_bicicletas()

        else:
            self.reg_ext_output_text.set("Something Wrong :(")

    def capturar_input(self, object_input: tk.Entry):
        """Captura la entrada de un objeto Input."""
        return object_input.get()

    def reg_bike_action(self):
        """
        Acción que se realiza al presionar el boton
        de registro
        """

        serial_user = self.capturar_input(self.serial_input)
        entry_time_user = self.capturar_input(self.entry_time_input)

        if app_src.reg_nueva_bicicleta(serial_user, entry_time_user):
            self.reg_output_text.set('Registro Exitoso :D')

        else:
            self.reg_output_text.set('Algo salio mal :(')

    # --- PUNTO DE ENTRADA DE LA APLICACIÓN ---
if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando corremos este archivo directamente.
    # No se ejecuta si importamos este archivo desde otro módulo.

    # Tk() crea la ventana principal de la aplicación
    root = tk.Tk()

    # Creamos una instancia de nuestra aplicación
    # Le pasamos la ventana principal como argumento
    app = BikeWorkShopApp(root)

    # mainloop() inicia el bucle de eventos de Tkinter
    # Mantiene la ventana abierta y esperando interacción del usuario
    # Sin esto, la ventana se abriría y cerraría inmediatamente
    root.mainloop()
