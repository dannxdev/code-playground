from pathlib import Path
import os
import shutil

os.system('cls')


def is_empty_dir(path_dir: Path):
    """Verifica si la carpeta es vacia (True) o no (False)"""
    return not any(path_dir.iterdir())


def delete_content_dir(path_dir):
    """
    Borra el contenido de un directorio.
    """
    if os.path.exists(path_dir):
        # Elimina todo el contenido recursivamente
        shutil.rmtree(path_dir)
        # Vuelve a crear la carpeta vacía
        os.makedirs(path_dir)

        print(f"Contenido de '{path_dir}' eliminado correctamente.")

    else:
        print(f"La carpeta '{path_dir}' no existe.")


def backups_scan(path_dir: Path):
    """Escanea un directorio y su contenido en busca
    de carpetas backup"""

    for element in path_dir.iterdir():
        if element.is_dir() and not is_empty_dir(element):

            if element.name == 'Backup':
                print(f"Se eliminara el contenido de: {element}")
                while True:
                    user_check = input(
                        "¿Confirmar eliminacion? (s/n): ").lower()
                    if user_check in ('s', 'n'):
                        break
                    print("Opción no valida. Vuelva a intentarlo.")

                if user_check == 's':
                    delete_content_dir(element)

                if user_check == 'n':
                    print("Operación cancelada.")

            else:
                backups_scan(element)


if __name__ == "__main__":
    print("=== FL STUDIO - Delete Backup Folder ===")

    CURRENT_PATH = Path(__file__).parent

    while True:
        print(f"\nSe encuentra en el directorio:\n{CURRENT_PATH}")
        user_option = input("\n¿Desea continuar? (s/n): ")
        if user_option in ('s', 'n'):
            break
        print("Opción no valida. Vuelva a intentarlo.")

    if user_option == 's':
        backups_scan(CURRENT_PATH)

    else:
        print("Operación cancelada.")

    input("\nPresione ENTER para salir...\n")
