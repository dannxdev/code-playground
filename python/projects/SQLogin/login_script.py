import app_source as app_src
from PyQt6 import QtWidgets
import db_connect as us_data


# main_window.loginButton.clicked.connect(push_lgnButton)
# main_window.sign_inButton.clicked.connect(push_signButton)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # ui_path = get_ui_file_path("loginWindow.ui")
    main_window = app_src.MainWindow(
        app_src.get_ui_file_path('loginWindow.ui'))
    main_window.show()  # Muestra la ventana principal.

    def push_continueButton():
        username_input = main_window.username_input.text()
        pswrd_input = main_window.pswrd_input.text()
        # crea una instancia del objeto usersDB para aplicar los metodos.
        if us_data.login_validate(username_input, pswrd_input):
            print('Ha iniciado sesion exitosamente')
        else:
            print('Usuario/Contrasena Invalidos')

    main_window.continue_Button.clicked.connect(push_continueButton)

    app.exec()  # Inicia el bucle de eventos de la aplicación.
