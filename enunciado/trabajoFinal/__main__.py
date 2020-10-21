import sys
from ahorcado import Ahorcado
from aux import tomar_input


class Menu():
    def __init__(self):
        self.ahorcado = Ahorcado()

    def menu_principal(self):
        while True:
            print("1. Iniciar Partida")
            print("2. Salir del juego")
            eleccion = tomar_input("Elegir una opción del menú: ", False)
            if eleccion == 1:
                self.iniciar_partida()
            else:
                break
        sys.exit()

    def iniciar_partida(self):
        while True:
            nro_jugadores =\
                tomar_input("Cantidad de jugadores (1 ó 2): ", False)
            if nro_jugadores == 1:
                self.ahorcado.un_jugador()
                break
            elif nro_jugadores == 2:
                self.ahorcado.dos_jugadores()
                break
            else:
                print("Ingresar un nro válido de jugadores.")


if __name__ == "__main__":
    Menu().menu_principal()
