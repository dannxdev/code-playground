from app.tkinter_interface import BikeWorkShopApp
from app.bike_workshop import BikeWorkShop
import tkinter as tk

# --- EJECUTANDO LA APLICACIÓN ---
if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando corremos este archivo directamente.
    # No se ejecuta si importamos este archivo desde otro módulo.

    # Tk() crea la ventana principal de la aplicación
    root = tk.Tk()

    # Creando un taller de bicicletas:
    my_workshop = BikeWorkShop()
    # Colocando el precio por hora del taller:
    my_workshop.set_hour_price(7000)

    # Creamos una instancia de nuestra aplicación
    # Le pasamos la ventana principal como argumento
    app = BikeWorkShopApp(root, my_workshop)

    # mainloop() inicia el bucle de eventos de Tkinter
    # Mantiene la ventana abierta y esperando interacción del usuario
    # Sin esto, la ventana se abriría y cerraría inmediatamente
    root.mainloop()
