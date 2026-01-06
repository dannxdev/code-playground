import json
import os
import datetime

# Limpiando la consola en cada nueva ejecución:
os.system('cls')


class JsonManager:
    """Recibe una ruta de un archivo .JSON y crea una instancia que permite acceder a métodos que 
    leen y escriben em dicho archivo."""

    def __init__(self, ruta):  # path
        self.ruta = ruta

    def read_json(self):
        """Devuelve un diccionario con la lectura del archivo .json"""

        with open(self.ruta, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
        return data

    def write_json(self, data_dict: dict):
        """Escribe en un diccionario o modifica un diccionario dado"""

        with open(self.ruta, 'w', encoding='utf-8') as archivo:
            json.dump(data_dict, archivo, indent=4, ensure_ascii=False)


class Tarea:
    def __init__(self, titulo) -> None:
        self.titulo = titulo
        self.estado = False
        ahora = datetime.datetime.now()
        self.fecha = f"{ahora.year}-{ahora.month}-{ahora.day} {ahora.hour}:{ahora.minute}"

    def __repr__(self) -> str:
        return f"Titulo: {self.titulo}, Estado: {self.estado}, Fecha: {self.fecha}"


class GestorDeTareas:
    def __init__(self, archivo_json) -> None:
        self.archivo_json = archivo_json

    def guardar_tarea(self, tarea_dict):
        """Guarda la instancia de la clase Tarea en el archiv .JSON"""

        lectura_json = self.archivo_json.read_json()
        lectura_json.update(tarea_dict)
        self.archivo_json.write_json(lectura_json)

    def crear_tarea(self, titulo):
        """Crea una tarea, a partir de un titulo dado como parametro y la 
        guarda en el archivo .JSON"""

        nueva_tarea = Tarea(titulo)
        lectura_json = self.archivo_json.read_json()
        if len(lectura_json) > 0:
            claves = [int(clave) for clave in lectura_json]
            nueva_clave = (max(claves)) + 1
        else:
            nueva_clave = 1

        tarea = {}
        tarea[nueva_clave] = {
            "Titulo": nueva_tarea.titulo, "Estado": nueva_tarea.estado, "Fecha": nueva_tarea.fecha}
        self.guardar_tarea(tarea)
        print("Tarea creada con Exito!")

    def completar_tarea(self, codigo: str):
        """Se marca una tarea del archivo .JSON como completada (true), deacuerdo 
        al codigo pasado como parametro"""

        lectura_json = self.archivo_json.read_json()
        if codigo in lectura_json:
            print(lectura_json[codigo])
            confirmar = input("Marcar como Completada? (S/N): ").lower()
            if confirmar == 's':
                if lectura_json[codigo]["Estado"] is False:
                    lectura_json[codigo]["Estado"] = True
                    self.archivo_json.write_json(lectura_json)
                    print("Has completado la tarea.")
                else:
                    print("Ya haz completado esta tarea.")
            else:
                print("Cancelado")
        else:
            print("No se ha encontrado la tarea.")

    def eliminar_tarea(self, codigo: str):
        """Se elimina una tarea del archivo .JSON, deacuerdo al codigo 
        pasado como parametro"""

        lectura_json = self.archivo_json.read_json()
        if codigo in lectura_json:
            print(lectura_json[codigo])
            confirmar = input("Eliminar la Tarea? (S/N): ").lower()
            if confirmar == 's':
                del lectura_json[codigo]
                self.archivo_json.write_json(lectura_json)
                print("Se ha eliminado la tarea.")
            else:
                print("Haz cancelado la eliminacion.")
        else:
            print("No se ha encontrado la tarea.")

    def mostrar_tareas(self):
        """Muestra en consola un informe de todas las tareas guardadas."""

        print("----------------------------------------")
        lectura_json = self.archivo_json.read_json()
        print("TUS TAREAS:\n")

        cont_tareas = 0
        cont_completadas = 0
        cont_pendientes = 0

        for k, v in lectura_json.items():

            if v["Estado"] is False:
                estado = "Pendiente"
                cont_pendientes += 1
            else:
                estado = "Completada"
                cont_completadas += 1
            print(
                f"Codigo: {k}\n- Tarea: {v["Titulo"]}\n- Estado: {estado}\n- Fecha: {v["Fecha"]}\n")
            cont_tareas += 1

        print(
            f"Cantidad de Tareas: {cont_tareas}\nCompletadas: {cont_completadas}\nPendientes: {cont_pendientes}\n")
        print("----------------------------------------")


if __name__ == "__main__":
    print("========================================")
    print("      TO-DO LIST by DannyDev      ")
    print("========================================\n")

    tareas_json = JsonManager("app/appSources/task_list.json")
    GESTOR = GestorDeTareas(tareas_json)
    GESTOR.mostrar_tareas()

    print("Que deseas hacer?\n1. Crear una tarea\n2. Completar una Tarea\n3. Eliminar una Tarea\n4. Salir")

    while True:
        user_option = (input("\nSelecciona una opcion: ")).replace(" ", "")
        if len(user_option) > 0 and user_option != " ":
            try:
                user_option = int(user_option)
                break
            except ValueError:
                print("Error: Escribe un numero valido.")
        print("Por favor, elige una opcion valida.")

    if user_option < 5:
        if user_option == 1:
            print("Crear Tarea")
            titulo = (input("Titulo: ").strip()).capitalize()
            GESTOR.crear_tarea(titulo)
        elif user_option == 2:
            print("Completar Tarea")
            codigo = input("Codigo de la tarea: ").replace(" ", "")
            GESTOR.completar_tarea(codigo)
        elif user_option == 3:
            print("Eliminar Tarea")
            codigo = input("Codigo de la tarea: ").replace(" ", "")
            GESTOR.eliminar_tarea(codigo)
    else:
        print("Por favor, elige una opcion valida.")
