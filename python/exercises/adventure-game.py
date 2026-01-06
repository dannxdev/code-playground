import random
import os
os.system('cls')

# Problema 4: Aventura en el Bosque Encantado

# Descripción:
# Crea un programa en Python que simule una aventura en un bosque encantado.
# El jugador tomará decisiones que influirán en el desarrollo de la historia.
# El juego comienza con el jugador en la entrada del bosque y le ofrece tres opciones iniciales:

# Opciones Iniciales:
# 1. Entrar al bosque
# 2. Buscar un objeto mágico
# 3. Salir del juego

# Reglas del Juego:

# 1. Entrar al Bosque:
#    - Si el jugador elige entrar al bosque, se le presentarán dos caminos:
#      a. Caminar por el camino iluminado
#      b. Aventurarse por el camino oscuro
#    - Dependiendo de su elección:
#      * Camino iluminado:
#        - Lleva a un hermoso lago.
#        - Opción de descansar.
#        - Si descansa, recupera energía.
#      * Camino oscuro:
#        - Lleva a un lugar lleno de criaturas mágicas.
#        - Si se encuentra con una criatura, debe decidir:
#          i. Luchar: Resulta en perder energía.
#          ii. Negociar: Puede ganar un objeto mágico.

# 2. Buscar un Objeto Mágico:
#    - Se presentan tres objetos disponibles:
#      a. Espada mágica
#      b. Escudo encantado
#      c. Poción curativa
#    - El jugador elige uno y se le informa sobre sus beneficios.

# 3. Salir del Juego:
#    - Se muestra un mensaje de despedida.

CRIATURAS_MAGICAS = [
    "Dragón",
    "Unicornio",
    "Fénix",
    "Minotauro",
    "Centauro",
    "Kraken",
    "Hada",
    "Duende",
    "Vampiro",
    "Trol"]


OBJETOS_MAGICOS = [
    "Espada Mágica",
    "Libro de Magia",
    "Escudo Encantado",
    "Amuleto de la Suerte",
    "Anillo de Invisibilidad",
    "Botas de Velocidad",
    "Poción de Curación",
    "Guantes de Fuerza",
    "Arpa Encantada",
    "Daga Venenosa",
]


class Jugador:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.inventario = []
        self.energia = 50

    def mostrar_info(self):
        """Muestra las estadisticas del jugador"""

        if self.energia > 0:
            print(
                f'{self.nombre}, tu estado actual:\n- Inventario: {self.inventario}\n- Energia: {self.energia}%')
        else:
            print(f'{self.nombre}, haz gastado toda tu energia. Haz muerto.')

    def modificar_energia(self, cant: int):
        """Modifica la energia del jugador, si se ingresa una cantidad negativa se restara energia, si es
        positiva se sumara."""

        if cant > 0 or cant < 0:
            self.energia += cant
            self.mostrar_info()
        else:
            print('No haz ingresado una cantidad de energia')


class Criatura:
    def __init__(self) -> None:
        self.nombre = random.choice(CRIATURAS_MAGICAS)
        self.objeto_secreto = random.choice(OBJETOS_MAGICOS)

    def mostrar_criatura(self):
        """Muestra informacion de la criatura"""
        print(f'- Criatura: {self.nombre}\n- Tiene: {self.objeto_secreto}')


def bosque_magico(jugador):
    """Encapsula la logica de cuando el jugador elije acceder
    al bosque magico."""

    print('Bienvenido al Bosque Magico\n')
    print('Haz encontrado dos caminos:\nA. Caminar por el camino iluminado\nB. Aventurarse por el camino oscuro')
    opcion_camino = input('\nElige un camino: ').lower()

    # Si el usuario elige la opcion A:
    if opcion_camino == 'a':
        print('\nHaz llegado a un hermoso lago.')
        opcion_descansar = input('¿Quieres descansar? (SI/NO): ').lower()

        if opcion_descansar == 'si':
            print('\nHaz recuperado 20% de tu energia\n')
            jugador.modificar_energia(20)
        else:
            print('No haz descansado')

    # Si el usuario elige la opcion B:
    elif opcion_camino == 'b':
        # Crea una instancia nueva de la clase Criatura:
        criatura_nueva = Criatura()
        print(
            f'\nHaz llegado a un lugar lleno de criaturas magicas.\nCriatura magica encontrada: {criatura_nueva.nombre}')
        opcion_luchar_negociar = input(
            '\nLuchar (L) o Negociar (N) con la criatura : ').upper()

        # Si la opcion es luchar:
        if opcion_luchar_negociar == 'L':
            print(
                f'\nHaz luchado con la criatura {criatura_nueva.nombre}, tu energia se ha reducido.\n')
            jugador.modificar_energia(-30)

        # Si la opcion es negociar:
        elif opcion_luchar_negociar == 'N':
            jugador.inventario.append(criatura_nueva.objeto_secreto)
            print(
                f'\nHaz negociado con la criatura.\nTe ha dado un objeto: {criatura_nueva.objeto_secreto}\n')
            jugador.mostrar_info()

        # Si el usuario ingresa una opcion incorrecta:
        else:
            print(
                f'\nNo haz tomado una desicion correcta.\nLa criatura {criatura_nueva.nombre} te ha asesinado.')

    else:
        print('\nOpcion no valida, Intentalo de nuevo')
