import tkinter as tk
from tkinter import ttk


class BikeWorkShopApp:
    """
    Clase que gestiona toda la aplicación.
    """

    def __init__(self, root):
        """
        Constructor de la aplicación.

        Args:
            root: La ventana principal de Tkinter (Tk())
        """

        self.root = root
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
        reg_option_button = tk.Button(
            master=self.root,
            text="Register Bike",
            command=self.mostrar_pantalla_registro)

        reg_option_button.pack(pady=10)

        # Boton de registrar salida bicicleta:
        reg_option_button = tk.Button(
            master=self.root,
            text="Register Bike Exit")

        reg_option_button.pack(pady=5)

    def mostrar_pantalla_registro(self):
        """Muestra la pantalla de registro de bicicletas."""

        self.limpiar_ventana()
        self.root.title("Bike WorkShop | Register")

        reg_bike_window_label = tk.Label(
            master=self.root,
            text="REGISTER BIKE",
            font='Arial')

        reg_bike_window_label.pack()

        # INPUTS PARA DATOS DE LA BICICLETA:

        bike_data_frame = tk.Frame()
        # Serial:
        serial_input_label = tk.Label(
            master=bike_data_frame,
            text="Serial (15):")
        serial_input = tk.Entry(master=bike_data_frame)
        # Hora ingreso:
        entry_time_input_label = tk.Label(
            master=bike_data_frame,
            text="Entry Time (HH:MM):")
        entry_time_input = tk.Entry(master=bike_data_frame)

        bike_data_frame.pack()
        serial_input_label.pack()
        serial_input.pack()
        entry_time_input_label.pack()
        entry_time_input.pack()

        # Boton de confirmar registro
        reg_bike_button = tk.Button(
            master=self.root,
            text="Register",
            command=self.add_bike)
        reg_bike_button.pack(pady=10)

        # Mensajes de salida:
        reg_output_text = tk.StringVar()
        reg_output_label = tk.Label(
            master=self.root,
            text="Output",
            textvariable=reg_output_text,
            fg='blue2')

        reg_output_label.pack(pady=5)

    def add_bike(self):
        print("Holaaaaa")


    # --- PUNTO DE ENTRADA DE LA APLICACIÓN ---
if __name__ == "__main__":
    """
    Este bloque solo se ejecuta cuando corremos este archivo directamente.
    No se ejecuta si importamos este archivo desde otro módulo.
    """

    # Tk() crea la ventana principal de la aplicación
    root = tk.Tk()

    # Creamos una instancia de nuestra aplicación
    # Le pasamos la ventana principal como argumento
    app = BikeWorkShopApp(root)

    # mainloop() inicia el bucle de eventos de Tkinter
    # Mantiene la ventana abierta y esperando interacción del usuario
    # Sin esto, la ventana se abriría y cerraría inmediatamente
    root.mainloop()
