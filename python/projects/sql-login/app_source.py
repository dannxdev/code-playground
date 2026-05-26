from pathlib import Path
from PyQt6 import QtWidgets, uic


def get_ui_file_path(file_ui: str) -> Path:
    script_dir = Path(__file__).parent
    return script_dir / "gui-sources" / file_ui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui_file: Path):
        super().__init__()
        self.ui_file = ui_file
        # Carga el diseño de la interfaz de usuario desde el archivo .ui en esta instancia.
        uic.loadUi(self.ui_file, self)

    def showWindow(self):
        app = QtWidgets.QApplication([])
        self.show()
        app.exec()

    #     # define que hacer en caso de pulsar el boton dado
    #     self.pushButton.clicked.connect(self.data_lgnWindow)

    # def data_lgnWindow(self):
    #     lgn_userInput = self.username_input.text()
    #     lgn_pwdInput = self.pswrd_input.text()
    #     # valida los datos ingresados en la ventana en la base de datos.
    #     if users_db.login_validate(lgn_userInput, lgn_pwdInput):
    #         print('Haz iniciado sesion correctamente')


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     # ui_path = get_ui_file_path("loginWindow.ui")
#     main_window = MainWindow(ui_path)
#     main_window.show()  # Muestra la ventana principal.

#     app.exec()  # Inicia el bucle de eventos de la aplicación.
