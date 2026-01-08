from pathlib import Path
import os
import shutil


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


def show_content_dir(path_dir: Path):
    """Muestra todo el contenido de una carpeta."""

    if path_dir.is_dir() and not is_empty_dir(path_dir):

        print(f"Analizando el contenido de: \n\n{path_dir}\n")

        for item in path_dir.iterdir():
            print(f"- {item.name}")

    else:
        print("La ruta especificada no contiene ningún elemento.")


def backups_scan(path_dir: Path):
    """Escanea un directorio y su contenido en busca
    de carpetas backup"""

    for element in path_dir.iterdir():
        if element.is_dir() and not is_empty_dir(element):
            # Si el item es una carpeta y no esta vacia.

            if element.name == 'Backup':
                # Si la carpeta tiene el nombre Backup.
                print("==========================")
                print("Carpeta Backup encontrada.\n")
                # Mostrando el contenido de la carpeta.
                show_content_dir(element)
                print(f"\nSe eliminara el contenido de: {element}")

                while True:
                    # Bucle de confirmation. Para seguridad.
                    user_check = input(
                        "\n¿Confirmar elimination? (s/n): ").lower()
                    if user_check in ('s', 'n'):
                        break
                    print("Opción no valida. Vuelva a intentarlo.")

                if user_check == 's':
                    # Si el usuario confirma la elimination.
                    delete_content_dir(element)

                if user_check == 'n':
                    print("Operación cancelada.")

            else:
                # Si la carpeta tiene otro nombre.
                backups_scan(element)


if __name__ == "__main__":
    print("=== FL STUDIO - Delete Backup Folder ===")

    CURRENT_PATH = Path(__file__).parent

    while True:
        print(f"\nSe encuentra en el directorio:\n{CURRENT_PATH}")
        user_option = input("\n¿Desea continuar? (s/n): ").lower()
        if user_option in ('s', 'n'):
            break
        print("Opción no valida. Vuelva a intentarlo.")

    if user_option == 's':
        backups_scan(CURRENT_PATH)

    else:
        print("Operación cancelada.")

    input("\nPresione ENTER para salir...\n")
