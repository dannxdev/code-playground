import app_source as app_src
from PyQt6 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # ui_path = get_ui_file_path("loginWindow.ui")
    main_window = app_src.MainWindow(app_src.get_ui_file_path('mainWindow.ui'))
    main_window.show()  # Muestra la ventana principal.

    def push_lgnButton():
        print('Ha pulsado INICIAR SESION')

    def push_signButton():
        print('Ha pulsado REGISTRATE')

    main_window.loginButton.clicked.connect(push_lgnButton)
    main_window.sign_inButton.clicked.connect(push_signButton)

    app.exec()  # Inicia el bucle de eventos de la aplicación.
