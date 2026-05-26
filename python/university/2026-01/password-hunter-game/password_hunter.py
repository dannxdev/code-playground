###
# JUEGO DEL CAZADOR DE CONTRASEñAS
# Autor: Daniel Benavides
# Curso: Programacion 213023 - Grupo 231
# Tutor: Juan Pablo Arango Cardona
###

# ===================== IMPORTS =====================
# re: Modulo para manejar expresiones regulares (validacion de strings)
# random: Modulo para funciones de aleatoriedad
# string: Modulo para acceso a funciones de cadena
# abc: Modulo para clases abstractas
# tkinter: Modulo para interfaz grafica

import re
import random
import string
from abc import ABC, abstractmethod
import tkinter as tk


# ===================== UTILIDADES =====================
def clean_text(string) -> "str | None":
    """Elimina espacios al inicio, al final y los dobles en medio del texto."""
    if not isinstance(string, str):
        return None
    result = string.strip()
    result = re.sub(r' {2,}', ' ', result)
    return result if result else None


def check_no_spaces(string: str):
    """
    Valida que una cadena de texto no esté vacía y no contenga espacios.
    """
    return bool(string) and ' ' not in string


# ===================== ERRORES PERZONALIZADOS =====================
class HunterGameError(Exception):
    """Clase Error del Juego"""

    def __init__(self, message, received_value=None):
        # inicializa la excepcion con el mensaje de error
        super().__init__(message)
        # almacena el valor que causo el error para referencia
        self.received_value = received_value


class InvalidPlayerScore(HunterGameError):
    """Error que se muestra al escribir un puntaje no valido"""
    pass


class InvalidPlayerName(HunterGameError):
    """Error que se muestra al escribir un nombre no valido"""
    pass


class InvalidPassword(HunterGameError):
    """Error que se muestra al escribir una contrasena no valida"""
    pass


# ===================== CLASE JUEGO CAZADOR =====================
class HunterGame:
    """Clase Juego Cazador"""

    def __init__(self) -> None:
        # inicializa el contador de rondas en cero
        self.rounds_number = 0

    @staticmethod
    def choice_chest(user_password):
        """Selecciona un cofre dependiendo de la calidad de la contrasena"""

        # verifica que la contrasena sea una instancia de Password
        if not isinstance(user_password, Password):
            # si no es instancia de Password, la convierte
            user_password = Password(user_password)

        # verifica si la contrasena es valida
        if not user_password.is_valid() or user_password.password is None:
            # si no es valida o es None devuelve un cofre maldito
            return CursedChest()

        # la contrasena es valida, ahora se elige el cofre segun su longitud
        if len(user_password.password) >= 14:
            # si tiene 14 o mas caracteres devuelve un cofre Legendario
            return LegendChest()

        # verifica si la longitud esta en el rango de 11 a 13 caracteres
        if 11 <= len(user_password.password) <= 13:
            # en ese rango devuelve un cofre Raro
            return RareChest()

        # si tiene 10 o menos caracteres
        # devuelve un cofre comun
        return CommonChest()


# ===================== CLASE JUGADOR =====================
class Player:
    """Clase Jugador"""

    def __init__(self, name: str) -> None:
        # convierte el nombre a mayuscula inicial y lo asigna
        self._name = name.capitalize()
        # inicializa el puntaje en cero
        self._score = 0

    def __str__(self) -> str:
        # retorna una representacion en string del jugador con su nombre y puntaje
        return f"{__class__.__name__}(name={self._name}, score={self.score})"

    def show_info(self):
        """Muestra la info. del jugador"""
        return f"""
Jugador: {self._name}
Puntuacion: {self.score}
"""

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_value):
        # valida que el nuevo puntaje sea de tipo int o float
        if isinstance(new_value, (int, float)):
            # asigna el nuevo valor de puntaje
            self._score = new_value
        else:
            # lanza una excepcion si el tipo no es valido
            raise InvalidPlayerScore(
                "Ha ingresado un puntaje no valido, debe ser int - float", received_value=type(new_value))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # limpia el nombre eliminando espacios al inicio, final y dobles
        new_name = clean_text(new_name)
        if new_name is None or len(new_name) < 3:
            # si el nombre no cumple los requisitos minimos
            raise InvalidPlayerName(
                "Ha ingresado un nombre de jugador no valido", received_value=new_name)
        # asigna el nombre validado y limpio
        self._name = new_name

    def add_score(self, new_score):
        """Agrega o quita puntuacion al jugador"""
        # valida que el puntaje sea de tipo numerico
        if isinstance(new_score, (float, int)):
            # suma el nuevo puntaje al puntaje actual
            self.score += new_score
            if self.score < 0:
                # si al anadir a puntuacion esta es menor a cero
                # sera igual a cero para evitar puntuaciones negativas
                self.score = 0
            return
        # lanza una excepcion si el puntaje no es valido
        raise InvalidPlayerScore(
            "Ha ingresado un puntaje de jugador no valido", received_value=type(new_score))


# ===================== CLASE CONTRASENA =====================

# caracteres permitidos para generar contrasenas
CHARACTERS_BASE = [
    string.ascii_letters,
    string.digits,
    "¿¡?=)(/¨*+-%&$#!",
]
# une los caracteres permitidos en una sola cadena
ALLOWED_CHARS = "".join(CHARACTERS_BASE)


class Password:
    """Clase Contrasena"""

    def __init__(self, password=None, gen_pwd=False) -> None:
        # si se solicita generar contraseña aleatoriamente
        if gen_pwd:
            password = self.generate_password()
        # asigna la contraseña proporcionada o generada
        self._password = password

    def __str__(self) -> str:
        # retorna una representacion en string de la contrasena
        return f"{__class__.__name__}(password={self.password})"

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        # valida que la contrasena no contenga espacios
        if check_no_spaces(new_password):
            # si no hay espacios, asigna la nueva contrasena
            self._password = new_password
            return
        # lanza una excepcion si la contrasena contiene espacios
        raise InvalidPassword(
            "La contrasena ingresada no es valida", received_value=new_password)

    def is_valid(self):
        """Verifica si la contrasena es valida"""

        # valida que la contrasena no sea None
        if not self.password is None:
            # verifica que tenga minimo 8 caracteres
            if len(self.password) < 8:
                # Si la longitud de la contrasena es menor a 8 caracteres
                return False
            # Regex: busca cualquier letra mayuscula del alfabeto (A-Z)
            # no permite tildes
            if not re.search(r'[A-Z]', self.password):
                # si no contiene al menos una letra mayuscula es invalida
                return False
            # Regex: busca cualquier letra minuscula del alfabeto (a-z)
            # no permite tildes
            if not re.search(r'[a-z]', self.password):
                # si no contiene al menos una letra minuscula es invalida
                return False
            # Regex: \d es un shorthand que equivale a [0-9], busca cualquier digito numerico
            if not re.search(r'\d', self.password):
                # si no contiene al menos un digito es invalida
                return False
            # Regex: agrupa los simbolos especiales permitidos:
            # ¿ ¡ ? = ) ( / ¨ * + \ - % & $ # !
            # El guion (-) va al final para que sea literal y no defina un rango
            special_chars = r'[¿¡?=)(/¨*+\-%&$#!]'
            if not re.search(special_chars, self.password):
                # si no encuentra al menos un caracter especial en la contrasena es invalida
                return False
            # verifica que no haya caracteres repetidos
            if len(set(self.password)) < len(self.password):
                # Si existen caracteres repetidos la contrasena es invalida
                return False
            # Si paso todas las validaciones la contrasena es valida
            return True
        # Si de entrada la contrasena es None no es valida
        return False

    def generate_password(self):
        """
        Genera y devuelve contrasenas aleatoriamente.
        """

        # Define aleatoriamente si aumentar la probabilidad de generar
        # contraseñas validas
        increase_prob = random.choice([True, False])

        # Se elige aleatoriamente la longitud de la contrasena:
        password_lenght = random.randint(8, 15)
        # Contrasena generada (vacia al inicio)
        result_password = ""

        # itera hasta alcanzar la longitud deseada de la contrasena
        for i in range(password_lenght):
            # escoge un caracter aleatorio de la categoria seleccionada
            new_char = random.choice(ALLOWED_CHARS)

            if increase_prob:
                # si el incremento de probabilidad es true
                # evita la repeticion de caracteres
                while new_char in result_password:
                    new_char = random.choice(ALLOWED_CHARS)
            # anade el caracter elegido a la contrasena generada
            result_password += new_char

        # retorna la contrasena generada
        return result_password


# ===================== CLASE COFRES =====================
class Chest(ABC):
    """Clase Cofre Base Abstracta"""

    def __init__(self, points=0) -> None:
        # inicializa los puntos por defecto del cofre
        # esta clase es abstracta y no debe instanciarse directamente
        self._points = points

    @property
    def points(self):
        return self._points

    @abstractmethod
    def show_info(self) -> str:
        """Muestra la informacion del cofre"""
        pass

    def __str__(self) -> str:
        return f"{__class__.__name__}(points={self.points})"


class CommonChest(Chest):
    """Clase Cofre Comun"""

    def __init__(self, points=10) -> None:
        # 10 puntos al encontrarlo
        super().__init__(points)
        self.name = "Comun"

    def __str__(self) -> str:
        return f"{__class__.__name__}(points={self.points})"

    def show_info(self):
        return f"""COFRE COMUN: Se obtienen {self.points} puntos"""


class RareChest(Chest):
    """Clase Cofre Raro"""

    def __init__(self, points=25) -> None:
        # 25 puntos al encontrarlo
        super().__init__(points)
        self.name = "Raro"

    def __str__(self) -> str:
        return f"{__class__.__name__}(points={self.points})"

    def show_info(self):
        return f"""COFRE RARO: Se obtienen {self.points} puntos"""


class LegendChest(Chest):
    """Clase Cofre Legendario"""

    def __init__(self, points=50) -> None:
        # 50 puntos al encontrarlo
        super().__init__(points)
        self.name = "Legendario"

    def __str__(self) -> str:
        return f"{__class__.__name__}(points={self.points})"

    def show_info(self):
        return f"""COFRE LEGENDARIO: Se obtienen {self.points} puntos"""


class CursedChest(Chest):
    """Clase Cofre Maldito"""

    def __init__(self, points=-20) -> None:
        # -20 puntos al encontrarlo
        super().__init__(points)
        self.name = "Maldito"

    def __str__(self) -> str:
        return f"{__class__.__name__}(points={self.points})"

    def show_info(self):
        return f"""COFRE MALDITO: Se obtienen {self.points} puntos"""


# =======================================
# CLASE INTERFAZ GRÁFICA
# =======================================

# Paleta de colores
COLORS = {
    "bg":           "#1a1a2e",   # Fondo principal oscuro
    "panel":        "#16213e",   # Fondo de paneles
    "card":         "#0f3460",   # Fondo de tarjetas/frames
    "accent":       "#e2b96f",   # Dorado (color principal de acento)
    "accent_hover": "#f0d080",   # Dorado más claro para hover
    "text":         "#e0e0e0",   # Texto principal
    "text_dim":     "#a0a0b0",   # Texto secundario
    "positive":     "#4caf82",   # Verde para puntos positivos
    "negative":     "#e05c5c",   # Rojo para puntos negativos
    "common":       "#90a4ae",   # Gris azulado — cofre común
    "rare":         "#7c83f0",   # Azul/violeta — cofre raro
    "legend":       "#f5c518",   # Amarillo — cofre legendario
    "cursed":       "#e05c5c",   # Rojo — cofre maldito
}

# Emojis por tipo de cofre
CHEST_ICONS = {
    "Comun":       "📦",
    "Raro":        "💠",
    "Legendario":  "🏆",
    "Maldito":     "💀",
}

# Color del nombre por tipo de cofre
CHEST_NAME_COLORS = {
    "Comun":       COLORS["common"],
    "Raro":        COLORS["rare"],
    "Legendario":  COLORS["legend"],
    "Maldito":     COLORS["cursed"],
}


class GUIHunterGame:
    """Clase Interfaz del Juego"""

    def __init__(self, root_window):
        # guarda la referencia a la ventana raiz
        self.root = root_window
        # establece el titulo de la ventana
        self.root.title("Cazador de Contraseñas")
        # define el ancho de la ventana
        self.window_width = 520
        # define el alto de la ventana
        self.window_height = 630
        # centra la ventana en la pantalla
        self.center_window(self.window_width, self.window_height)
        # aplica el color de fondo a la ventana
        self.root.config(bg=COLORS["bg"])
        # impide que se redimensione la ventana
        self.root.resizable(False, False)

        # --- Instancias del juego ---
        # crea una instancia del juego principal
        self.hunter_game_instance = HunterGame()
        # crea un jugador con nombre vacio (se asignara al jugar)
        self.current_player = Player("")
        # variable para guardar el cofre encontrado en cada ronda
        self.find_chest = None

        # muestra la pantalla principal del juego
        self.show_main_window()

    # ------------------------------------------------------------------
    # Utilidades de ventana
    # ------------------------------------------------------------------

    def clean_window(self):
        """Elimina todos los widgets de la ventana actual."""
        # itera sobre todos los widgets hijos y los elimina
        for widget in self.root.winfo_children():
            widget.destroy()

    def center_window(self, width, height):
        """Centra la ventana en pantalla."""
        # obtiene las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # calcula las coordenadas para centrar la ventana
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # aplica la geometria con la ventana centrada
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    # ------------------------------------------------------------------
    # Widgets
    # ------------------------------------------------------------------

    def make_title_bar(self, text):
        """Crea la barra de título superior."""
        # crea una barra de color acento en la parte superior
        bar = tk.Frame(self.root, bg=COLORS["accent"], height=4)
        bar.pack(fill="x")

        # crea el label del titulo con el texto proporcionado
        title = tk.Label(
            self.root,
            text=text,
            font=("Courier", 20, "bold"),
            bg=COLORS["bg"],
            fg=COLORS["accent"],
        )
        title.pack(pady=(18, 6))

        # crea un separador visual debajo del titulo
        sep = tk.Frame(self.root, bg=COLORS["accent"], height=1)
        sep.pack(fill="x", padx=40, pady=(0, 16))

    def make_card(self, parent=None):
        """Crea un frame con estilo de 'tarjeta'."""
        # si no se especifica un padre, usa la ventana raiz
        if parent is None:
            parent = self.root
        # crea un frame con estilos de tarjeta
        card = tk.Frame(
            parent,
            bg=COLORS["card"],
            bd=0,
            padx=24,
            pady=18,
        )
        return card

    def make_label(self, parent, text, size=11, bold=False, color=None):
        """Crea un label con estilo del juego."""
        # determina si el texto debe ser negrita
        weight = "bold" if bold else "normal"
        # usa el color proporcionado o el color de texto por defecto
        fg = color if color else COLORS["text"]
        # retorna un label con estilos
        return tk.Label(
            parent,
            text=text,
            font=("Courier", size, weight),
            bg=COLORS["card"],
            fg=fg,
        )

    def make_button(self, parent, text, command, width=22):
        """Crea un botón para la interfaz"""
        # crea un boton con estilos
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Courier", 11, "bold"),
            bg=COLORS["accent"],
            fg=COLORS["bg"],
            activebackground=COLORS["accent_hover"],
            activeforeground=COLORS["bg"],
            relief="flat",
            cursor="hand2",
            width=width,
            pady=8,
        )
        return btn

    # ------------------------------------------------------------------
    # Pantalla principal
    # ------------------------------------------------------------------

    def show_main_window(self):
        """Muestra la pantalla de inicio."""
        # limpia la ventana de widgets anteriores
        self.clean_window()

        # crea la barra de titulo
        self.make_title_bar("🗝  CAZADOR DE CONTRASEÑAS")

        # reinicia el numero de rondas cuando el jugador regresa a inicio
        self.hunter_game_instance.rounds_number = 0

        # crea un subtitulo del juego
        sub = tk.Label(
            self.root,
            text="Descubre contraseñas y abre cofres",
            font=("Courier", 10),
            bg=COLORS["bg"],
            fg=COLORS["text_dim"],
        )
        sub.pack(pady=(0, 20))

        # --- Tarjeta de entrada de nombre ---
        # crea una tarjeta para el formulario de nombre
        card = self.make_card()
        card.pack(padx=50, pady=8, fill="x")

        # etiqueta que solicita el nombre del jugador
        name_label = tk.Label(
            card,
            text="Ingresa tu nombre aqui:",
            font=("Courier", 11, "bold"),
            bg=COLORS["card"],
            fg=COLORS["accent"],
        )
        name_label.pack(anchor="w", pady=(0, 6))

        # campo de entrada para que el jugador escriba su nombre
        self.name_entry_box = tk.Entry(
            card,
            font=("Courier", 12),
            bg=COLORS["panel"],
            fg=COLORS["text"],
            insertbackground=COLORS["accent"],
            relief="flat",
            bd=6,
        )
        self.name_entry_box.pack(fill="x", ipady=4)
        # permite enviar el nombre presionando Enter
        self.name_entry_box.bind(
            "<Return>", lambda e: self.validate_player_name())

        # etiqueta para mostrar mensajes de error de validacion
        self.name_msg_error = tk.Label(
            card,
            text="",
            font=("Courier", 9),
            bg=COLORS["card"],
            fg=COLORS["negative"],
        )
        self.name_msg_error.pack(anchor="w", pady=(6, 0))

        # --- Frame para el boton de jugar ---
        # crea un contenedor para el boton de inicio
        btn_frame = tk.Frame(self.root, bg=COLORS["bg"])
        btn_frame.pack(pady=20)

        # boton para iniciar el juego con el nombre ingresado
        btn = self.make_button(
            btn_frame, "⚔  COMENZAR", self.validate_player_name)
        btn.pack()

        # --- Leyenda de cofres del juego ---
        # crea una tarjeta para mostrar informacion sobre los cofres
        legend_card = self.make_card()
        legend_card.pack(padx=50, pady=(8, 0), fill="x")

        # titulo de la seccion leyenda
        legend_title = tk.Label(
            legend_card,
            text="Cofres que encontraras:",
            font=("Courier", 9, "bold"),
            bg=COLORS["card"],
            fg=COLORS["text_dim"],
        )
        legend_title.pack(anchor="w", pady=(0, 6))

        # lista con la informacion de cada tipo de cofre
        chest_info = [
            ("📦 Común",     "+10 pts",  COLORS["common"]),
            ("💠 Raro",      "+25 pts",  COLORS["rare"]),
            ("🏆 Legendario", "+50 pts",  COLORS["legend"]),
            ("💫 Maldito",   "-20 pts",   COLORS["cursed"]),
        ]

        # crea un frame para mostrar los cofres en una sola fila
        row_frame = tk.Frame(legend_card, bg=COLORS["card"])
        row_frame.pack(fill="x")

        # itera sobre cada cofre y crea una columna para mostrarlo
        for name, pts, color in chest_info:
            # crea una columna para cada tipo de cofre
            col = tk.Frame(row_frame, bg=COLORS["card"])
            col.pack(side="left", expand=True)
            # muestra el nombre del cofre con su color especifico
            tk.Label(col, text=name, font=("Courier", 8, "bold"),
                     bg=COLORS["card"], fg=color).pack()
            # muestra los puntos asociados al cofre
            tk.Label(col, text=pts, font=("Courier", 8),
                     bg=COLORS["card"], fg=COLORS["text_dim"]).pack()

        # --- Frame para botones inferiores ---
        # crea un contenedor para el boton de salida
        btn2_frame = tk.Frame(self.root, bg=COLORS["bg"])
        btn2_frame.pack(pady=20)

        # boton para cerrar la aplicacion
        btn_exit = self.make_button(
            btn2_frame, "✖  Salir",
            self.root.destroy,
            width=12)
        btn_exit.pack(pady=(8, 0))

    # ------------------------------------------------------------------
    # Pantalla de juego
    # ------------------------------------------------------------------

    def show_play_window(self):
        """Muestra la pantalla de juego."""
        # limpia la pantalla anterior
        self.clean_window()

        # --- Lógica del juego ---
        # Incrementa el contador de rondas
        self.hunter_game_instance.rounds_number += 1
        # Genera una contrasena aleatoria para esta ronda
        self.player_password = Password(gen_pwd=True)
        # Elige un cofre segun la calidad de la contrasena
        self.find_chest = self.hunter_game_instance.choice_chest(
            self.player_password)
        # Añade o disminuye el puntaje del cofre elegido al jugador
        self.current_player.add_score(self.find_chest.points)
        # ----------------------------------------

        self.make_title_bar("🗝  CAZANDO CONTRASEÑAS...")

        # --- Barra de estado del jugador ---
        # crea un frame para mostrar info del jugador y ronda actual
        status_frame = tk.Frame(self.root, bg=COLORS["panel"], pady=10)
        status_frame.pack(fill="x", padx=40)

        tk.Label(
            status_frame,
            text=f"👤 {self.current_player.name}",
            font=("Courier", 10, "bold"),
            bg=COLORS["panel"],
            fg=COLORS["text"],
        ).pack(side="left", padx=12)

        tk.Label(
            status_frame,
            text=f"⭐ {self.current_player.score} pts",
            font=("Courier", 10, "bold"),
            bg=COLORS["panel"],
            fg=COLORS["accent"],
        ).pack(side="left", padx=12)

        tk.Label(
            status_frame,
            text=f"🔄 Ronda {self.hunter_game_instance.rounds_number}",
            font=("Courier", 10, "bold"),
            bg=COLORS["panel"],
            fg=COLORS["text_dim"],
        ).pack(side="right", padx=12)

        # --- Tarjeta de resultado ---
        card = self.make_card()
        card.pack(padx=40, pady=20, fill="x")

        # Contraseña generada
        tk.Label(
            card,
            text="CONTRASEÑA GENERADA",
            font=("Courier", 8, "bold"),
            bg=COLORS["card"],
            fg=COLORS["text_dim"],
        ).pack(anchor="w")

        tk.Label(
            card,
            text=self.player_password.password,  # type: ignore
            font=("Courier", 15, "bold"),
            bg=COLORS["card"],
            fg=COLORS["accent"],
        ).pack(anchor="w", pady=(2, 16))

        def copy_password():
            """Permite copiar la contrasena generada"""
            # limpia el portapapeles
            self.root.clipboard_clear()
            # copia la contrasena al portapapeles
            self.root.clipboard_append(self.player_password.password)
            # cambia el texto del boton para indicar que se copio
            btn_copy.config(text="✔  COPIADO!")
            # restablece el texto del boton despues de 1.5 segundos
            self.root.after(1500, lambda: btn_copy.config(
                text="📋  COPIAR") if btn_copy.winfo_exists() else None)

        # Boton copiar contraseña
        btn_copy = tk.Button(
            card,
            text="📋  COPIAR",
            command=copy_password,
            font=("Courier", 8, "bold"),
            bg=COLORS["panel"],
            fg=COLORS["accent"],
            activebackground=COLORS["card"],
            activeforeground=COLORS["accent_hover"],
            relief="flat",
            cursor="hand2",
            pady=4,
            padx=10,
        )
        btn_copy.pack(anchor="w", pady=(4, 12))

        # Separador interno
        tk.Frame(card, bg=COLORS["panel"], height=1).pack(
            fill="x", pady=(0, 14))

        # Cofre encontrado
        # obtiene el nombre, icono y color del cofre segun su tipo
        chest_name = self.find_chest.name
        chest_icon = CHEST_ICONS.get(chest_name, "📦")
        chest_color = CHEST_NAME_COLORS.get(chest_name, COLORS["text"])

        tk.Label(
            card,
            text="COFRE ENCONTRADO",
            font=("Courier", 8, "bold"),
            bg=COLORS["card"],
            fg=COLORS["text_dim"],
        ).pack(anchor="w")

        tk.Label(
            card,
            text=f"{chest_icon}  {chest_name.upper()}",
            font=("Courier", 16, "bold"),
            bg=COLORS["card"],
            fg=chest_color,
        ).pack(anchor="w", pady=(2, 14))

        # Puntos obtenidos
        # obtiene los puntos del cofre
        points = self.find_chest.points
        # define el color segun si los puntos son positivos o negativos
        pts_color = COLORS["positive"] if points >= 0 else COLORS["negative"]
        # agrega un signo mas si los puntos son positivos
        pts_sign = "+" if points >= 0 else ""

        tk.Frame(card, bg=COLORS["panel"], height=1).pack(
            fill="x", pady=(0, 14))

        tk.Label(
            card,
            text="PUNTOS OBTENIDOS",
            font=("Courier", 8, "bold"),
            bg=COLORS["card"],
            fg=COLORS["text_dim"],
        ).pack(anchor="w")

        tk.Label(
            card,
            text=f"{pts_sign}{points}",
            font=("Courier", 22, "bold"),
            bg=COLORS["card"],
            fg=pts_color,
        ).pack(anchor="w", pady=(2, 0))

        # --- Botón siguiente ronda ---
        # crea un frame para los botones de la parte inferior
        btn_frame = tk.Frame(self.root, bg=COLORS["bg"])
        btn_frame.pack(pady=16)

        # boton para buscar una nueva contrasena en la siguiente ronda
        btn = self.make_button(
            btn_frame,
            "🔍  BUSCAR NUEVA CONTRASEÑA",
            self.show_play_window,
            width=28,
        )
        btn.pack()

        # --- Boton finalizar juego ---
        # boton para abandonar el juego y volver a la pantalla principal
        btn_end_game = self.make_button(
            btn_frame,
            "X ABANDONAR",
            self.show_main_window,
            width=28,
        )
        btn_end_game.pack(pady=5)

    # ------------------------------------------------------------------
    # Lógica de validación
    # ------------------------------------------------------------------

    def get_player_name_entry(self):
        """Obtiene el nombre de usuario del campo de entrada de la interfaz."""
        # retorna el texto del campo de entrada del nombre
        return self.name_entry_box.get()

    def validate_player_name(self):
        """Valida el nombre ingresado por el jugador."""
        # obtiene y limpia el nombre del campo de entrada
        name_player_entry = clean_text(self.get_player_name_entry())

        if name_player_entry is None or len(name_player_entry) < 3:
            # se valida que el nombre de jugador no sea
            # una entrada invalida
            self.name_msg_error.config(
                text="⚠  El nombre debe tener al menos 3 caracteres")
            return

        # asigna el nombre validado al jugador actual
        self.current_player.name = name_player_entry
        # muestra la pantalla de juego si el nombre es valido
        self.show_play_window()


# === PUNTO DE ENTRADA ===
if __name__ == '__main__':
    # crea la ventana raiz de la aplicacion tkinter
    root = tk.Tk()
    # inicializa la interfaz grafica del juego con la ventana raiz
    app_gui = GUIHunterGame(root)
    # inicia el loop principal de la aplicacion
    root.mainloop()
