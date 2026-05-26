import tkinter as tk

root = tk.Tk()
root.title("Adivinando tu nombre y edad")

lbl_nombre = tk.Label(root, text="Nombre: ")
lbl_nombre.grid(row=0, column=0)
entrada_nombre = tk.Entry(root)
entrada_nombre.grid(row=0, column=1)

lbl_edad = tk.Label(root, text="Edad: ")
lbl_edad.grid(row=1, column=0)
entrada_edad = tk.Entry(root)
entrada_edad.grid(row=1, column=1)

def pulsar_boton():
    texto = entrada_nombre.get()
    texto2 = entrada_edad.get()
    muestra = tk.Label(root,text=f'Te llamas {texto} y tienes {texto2} años.')
    muestra.grid(row=3, column=1)

tk.Button(root, text="Comprobar", command=pulsar_boton).grid(row=2, column=1)

root.mainloop()