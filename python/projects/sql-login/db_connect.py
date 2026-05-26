# Definiendo las dependencias
import sqlite3 as sql
from pathlib import Path
import re
import random


class UsersDB:
    """Construye un usuario con los atributos definidos en en constructor"""

    def __init__(self, dni, full_name, email, phone, username, password):
        self.dni = dni
        self.full_name = full_name.upper()
        self.email = email.lower()
        self.phone = phone
        self.username = username.lower()
        self.password = password

    def __repr__(self):
        return f"""
                - dni: {self.dni}\n
                - full_name: {self.full_name}\n
                - email: {self.email}\n
                - phone: {self.phone}\n
                - username: {self.username}\n
                - password: {self.password}"""

    def validate_username(self) -> bool:
        """Recibe un nombre de usuario (str) y valida si cumple los parametros
        definidos mediante una expresion regular."""
        self.username = self.username.lower()
        us_dict = us_pwdData()

        # Si el username ya existe en la base de datos:
        if self.username in us_dict.keys():
            return False

        # Validando que el username contenga letras y digitos, se de no mas de 10 caracteres:
        regex = r'^[a-zA-Z0-9_]{1,10}$'
        # Buscando si la expresion regular coincide con el username
        matches = re.findall(regex, self.username)
        if matches:
            return True

        return False

    def pwd_check(self):
        """Recibe una contrasena (str) y valida si cumple los parametros
        definidos mediante una expresion regular."""
        regex = r'^[a-zA-Z0-9#-]{1,10}$'
        matches = re.findall(regex, self.password)
        if matches:
            return True
        return False

    def reg_user(self):
        """Ejecuta una consulta mediante SQL, que registra el usuario y todos sus datos 
        en la base de datos SQL."""
        try:
            # Conectar a la base de datos
            connect = connect_sql('users_database.sqlite3')
            cursor = connect.cursor()

            # Consulta parametrizada
            query = "INSERT INTO Users (dni, full_name, email, phone, username, password) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query, (self.dni, self.full_name, self.email, self.phone, self.username, self.password))

            # Confirmando el registro y los cambios:
            connect.commit()

        except sql.Error as e:
            # Manejo de errores en caso de problemas con la base de datos
            print(f"Error al registrar el usuario: {e}")
            return False

        finally:
            # Cerrar la conexión
            if connect:  # type: ignore
                connect.close()

        return True

    def send_txt(self):
        """Genera un codigo de verificacion para cada registro y lo envia mediante un archivo
        TXT a la carpeta sources. Simulando una verificacion de seguridad."""
        # Obtener el directorio del script actual
        script_dir = Path(__file__).parent
        # Crear la carpeta 'sources' si no existe
        txt_dir = script_dir / 'sources'
        txt_dir.mkdir(exist_ok=True)
        # Construir la ruta al archivo de la base de datos
        txt_file = txt_dir / 'verification-code.txt'
        rdm_code = random.randint(100000, 999999)
        with open(txt_file, 'w', encoding='utf-8') as archivo:
            archivo.write(
                f"Hola, '{self.username}'!\nTu codigo de verificacion es: {rdm_code}")
        return rdm_code


def connect_sql(file):
    """Recibe una ruta de un archivo SQL y se conecta a
    ella."""
    # Obtener el directorio del script actual
    script_dir = Path(__file__).parent
    # Crear la carpeta 'source_db' si no existe
    db_dir = script_dir / 'sources'
    db_dir.mkdir(exist_ok=True)
    # Construir la ruta al archivo de la base de datos
    db_file = db_dir / file
    # Imprimir información para depuración
    try:
        connection = sql.connect(db_file)
        return connection
    except sql.OperationalError as e:
        print("Error al conectar:", e)
        print("Directorio del script:", script_dir)
        print("Ruta completa al archivo:", db_file.resolve())
        raise


def userDB_read():
    """Lee toda la base de datos"""

    connect = connect_sql('users_database.sqlite3')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Users")
    connect.commit()
    data_set = cursor.fetchall()
    connect.close()
    return data_set


def us_pwdData() -> dict:
    """Devuelve un diccionario contodos los username y contrasenas
    respectivas de la base de datos."""
    connect = connect_sql('users_database.sqlite3')
    cursor = connect.cursor()
    cursor.execute("SELECT username, password FROM users")
    connect.commit()
    us_pwd = cursor.fetchall()
    connect.close()
    return dict(us_pwd)


def login_validate(username, password):
    """Valida si el usuario existe en la base de datos, al igual qu la contrasena
    para que se pueda inicar sesion"""
    data = us_pwdData()
    if username in data:
        temp_pwd = data[username]

        if password == temp_pwd:
            return True

        return False

    return False
