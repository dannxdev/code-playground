# SQLogin

## Descripción
SQLogin es un proyecto de aprendizaje no funcional diseñado para practicar la conexión de bases de datos SQLite con Python, implementando un sistema de inicio de sesión y registro. Incluye una interfaz gráfica desarrollada con PyQt6 (en progreso) y simula funcionalidades como el envío de un código de verificación mediante un archivo TXT para el registro de usuarios.

## Autor
DannyDev

## Funcionalidades
- **Registro de usuarios**: 
  - Recibe datos del usuario (nombre de usuario y contraseña).
  - Simula el envío de un código de verificación a través de un archivo TXT antes de registrar los datos en la base de datos SQLite.
- **Inicio de sesión**: 
  - Valida si el nombre de usuario existe en la base de datos.
  - Verifica si la contraseña ingresada coincide con la almacenada.
- **Interfaz gráfica**: 
  - Actualmente no funcional, pero se planea implementar utilizando PyQt6 en futuras actualizaciones.

## Estructura del Proyecto
El proyecto contiene las siguientes carpetas y archivos:

- **gui_sources/**: Contiene los recursos necesarios y la estructura de la interfaz gráfica del proyecto.
- **sources/**: Incluye:
  - La base de datos SQLite3 necesaria para el funcionamiento del proyecto.
  - El archivo TXT que simula el código de verificación para el registro.
- **Archivos de código**:
  - `sign_in_script.py`: Contiene la lógica y estructura del sistema de inicio de sesión.
  - `login_script.py`: Incluye la lógica y estructura del sistema de registro.
  - `db_connect.py`: Maneja la conexión a la base de datos SQLite, validaciones de usuarios, registro y modificación de datos.

## Requisitos
- Python 3.x
- PyQt6 (para la interfaz gráfica, en desarrollo)
- SQLite3

## Instalación
1. Clona el repositorio o descarga los archivos del proyecto.
2. Asegúrate de tener Python y las dependencias instaladas:
   ```bash
   pip install pyqt6
   ```
3. Verifica que la base de datos SQLite esté en la carpeta `sources/`.
4. Ejecuta los scripts según sea necesario (por ejemplo, `sign_in_script.py` o `login_script.py`).

## Estado Actual
El proyecto es un prototipo no funcional a nivel de interfaz gráfica. Las funcionalidades de backend (inicio de sesión, registro y conexión a la base de datos) están implementadas, pero la interfaz gráfica está en desarrollo.

## Notas
- Este es un proyecto de práctica, por lo que puede contener errores o limitaciones.
- Se planean mejoras en la interfaz gráfica y nuevas funcionalidades en el futuro.

