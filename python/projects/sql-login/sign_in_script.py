import app_source as app_src
from PyQt6 import QtWidgets
import db_connect as us_data


# main_window.loginButton.clicked.connect(push_lgnButton)
# main_window.sign_inButton.clicked.connect(push_signButton)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # ui_path = get_ui_file_path("loginWindow.ui")
    main_window = app_src.MainWindow(
        app_src.get_ui_file_path('sign_inWindow.ui'))
    main_window.show()  # Muestra la ventana principal.

    def push_continueButton():
        dni_input = main_window.dni_input.text()
        name_input = main_window.name_input.text()
        email_input = main_window.email_input.text()
        phone_input = main_window.phone_input.text()
        username_input = main_window.username_input.text()
        pswrd_input = main_window.pswrd_input.text()
        # crea una instancia del objeto usersDB para aplicar los metodos.
        new_user = us_data.UsersDB(
            dni_input, name_input, email_input, phone_input, username_input, pswrd_input)
        new_user.send_txt()
        new_user.reg_user()

    main_window.continue_button.clicked.connect(push_continueButton)

    app.exec()  # Inicia el bucle de eventos de la aplicación.
