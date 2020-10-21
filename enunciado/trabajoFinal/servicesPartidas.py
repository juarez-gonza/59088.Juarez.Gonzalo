import random
from partida import Partida
from repo_palabras import Repo_Palabras


class ServicesPartidas():
    def __init__(self):
        self.repo_palabras = Repo_Palabras()

    def iniciar_partida(self, nombre_jugador, dificultad,
                        palabra="", tipo_palabra=""):
        try:
            if len(palabra) == 0 and len(tipo_palabra) == 0:
                palabra_random = self.get_random_palabra()
                tipo_palabra = palabra_random["tipo_palabra"]
                palabra = palabra_random["palabra"]
            intentos = self.calcular_dificultad(palabra, dificultad)
            return Partida(palabra, intentos, tipo_palabra, nombre_jugador)
        except Exception:
            raise

    def intentar_letra(self, partida, letra):
        try:
            partida.palabra_aciertos = self.\
                insertar_letra(partida.palabra,
                               partida.palabra_aciertos,
                               letra)
            iguales = self.\
                comparar_palabras(partida.palabra,
                                  partida.palabra_aciertos)
            # partida.py -> @intentos.setter:  ValueError cuando intentos < 0
            partida.intentos = partida.intentos - 1
            if iguales:
                return "Gano"
            elif partida.intentos == 0:
                return "Perdio"
            else:
                return "Continua"
        except ValueError:
            raise

    def calcular_dificultad(self, palabra, dificultad):
        try:
            if dificultad <= 0 or dificultad > 10:
                raise ValueError("La dificultad debe tomar un valor entre " +
                                 "1 y 10")
            return len(palabra) * dificultad
        except ValueError:
            raise

    def get_random_palabra(self):
        return self.repo_palabras.\
            get_palabra(random.randrange(len(self.repo_palabras.repo)))

    def comparar_palabras(self, palabra_obj, palabra_intento):
        i = 0
        while (palabra_obj[i] == palabra_intento[i] and
                (i := i+1) < len(palabra_obj)):
            continue
        return i == len(palabra_obj)

    def insertar_letra(self, palabra_obj, palabra_intento, letra):
        for i in range(len(palabra_intento)):
            palabra_intento[i] = letra if letra == palabra_obj[i]\
                else palabra_intento[i]
        return palabra_intento
