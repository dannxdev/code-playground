from pathlib import Path
import os

os.system('cls')


RUTA_ACTUAL = Path(__file__).parent
CARPETA_SOURCE = RUTA_ACTUAL / "src"
ruta_carpeta_proyecto = CARPETA_SOURCE / "mi-proyecto-ejemplo"

carpetas_base = {
    "config": ".csv",
    "data": ".xml",
    "logs": ".log",
    "output": ".pdf"
}

nombre_archivo = "report.txt"
ruta_archivo_txt = RUTA_ACTUAL/nombre_archivo

# ----------
with open(ruta_archivo_txt, 'w', encoding='utf-8') as archivo:
    # Crea el archivo vacío
    archivo.write(
        f"REPORTE DE ERRORES:\n Ruta: {ruta_carpeta_proyecto}:\n\n")
print(f"\nArchivo '{nombre_archivo}' creado.")
# ----------


def write_in_txt(texto: str):
    """
    Escribe lo que se reciba como argumento en un archivo TXT.
    """

    with open(ruta_archivo_txt, 'a', encoding='utf-8') as archivo_txt:
        archivo_txt.write(f"{texto}\n")


def es_carpeta_vacia(ruta_dir):
    """
    Verifica si la carpeta es vacia (True) o no (False). 
    arg: ruta de la carpeta
    """

    carpeta = Path(ruta_dir)
    return carpeta.is_dir() and not any(carpeta.iterdir())


def carpetas_principales(ruta_proyecto: Path):
    """
    Valida si existen las carpetas base dentro de la carpeta 
    principal del proyecto.
    """

    carpetas_esperadas = list(carpetas_base)

    # Validar y crear carpetas
    for folder_name in carpetas_esperadas:
        folder_path = ruta_proyecto / folder_name
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            print(f"📁 Carpeta creada: {folder_path}")
        else:
            print(f"✅ Carpeta existente: {folder_path}")


def validar_archivos(ruta_proyecto: Path):
    """
    Por definir
    """

    files_ok = True

    for carpeta in ruta_proyecto.iterdir():
        if not es_carpeta_vacia(carpeta):
            for file in carpeta.iterdir():
                if not file.name.endswith(carpetas_base[carpeta.name]):
                    files_ok = False

                    nombre, extension = file.name.split(".")
                    extension = "." + extension

                    dir_encontrado = False
                    dir_correcto = ""
                    for k, v in carpetas_base.items():
                        if v == extension:
                            dir_correcto = k
                            dir_encontrado = True
                            break

                    if dir_encontrado:
                        origen = file
                        destino = ruta_carpeta_proyecto / dir_correcto / file.name
                        try:
                            origen.replace(destino)
                            print(f"✅ - Movido: {file} a {destino}")

                        except Exception as e:
                            write_in_txt(f"❌ Error: {e}")
                    else:
                        write_in_txt(f"⚠️ Directorio no encontrado: {file}")

                else:
                    print(f"✅ Archivo correcto: {file}")
        else:
            write_in_txt(f"⚠️ Directorio vacio: {carpeta}")

    return files_ok


if __name__ == "__main__":
    carpetas_principales(ruta_carpeta_proyecto)
    validar_archivos(ruta_carpeta_proyecto)

    input("\nPresione ENTER para salir.")
