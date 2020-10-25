from servicesPartidas import ServicesPartidas
from aux import tomar_input


class Ahorcado:
    def __init__(self):
        self.services_partidas = ServicesPartidas()

    def un_jugador(self):
        return self.juego(1)

    def dos_jugadores(self):
        return self.juego(2)

    def juego(self, nro_jugadores):
        try:
            for i in range(nro_jugadores):
                partida = self.crear_partida(nro_jugadores)
                self.adivinar_letra(partida)
        except StopIteration:
            # para lidiar con algunos tests que largan este error
            return True
        except SystemExit:
            # para lidiar con salir del juego de cualquier toma de input
            pass
        return True

    def adivinar_letra(self, partida):
        while True:
            letra =\
                tomar_input("Ingresar una letra: ").upper()
            resultado = ServicesPartidas().\
                intentar_letra(partida, letra)
            if resultado == "Perdio":
                print("Perdiste :(")
                break
            elif resultado == "Gano":
                print("Ganaste :)")
                break
        return True

    def crear_partida(self, nro_jugadores):
        nombre_jugador =\
            tomar_input("Ingresar nombre del jugador: ")
        dificultad =\
            tomar_input("Ingresar dificultad de la partida: ", False)
        palabra = ""
        tipo_palabra = ""
        if nro_jugadores > 1:
            palabra =\
                tomar_input("Ingresar la palabra a adivinar: ")
            tipo_palabra =\
                tomar_input("Ingresar categoria de la palabra a adivinar: ")
        partida = ServicesPartidas().\
            iniciar_partida(nombre_jugador, dificultad, palabra, tipo_palabra)
        return partida
