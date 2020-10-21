class Partida:
    def __init__(self, palabra, intentos, tipo_palabra, nombre_jugador):
        self.palabra = palabra
        self.intentos = intentos
        self.tipo_palabra = tipo_palabra
        self.nombre_jugador = nombre_jugador
        self.palabra_aciertos = [None for letra in palabra]

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, palabra):
        try:
            if len(palabra) == 0 or palabra is None:
                raise ValueError("El valor de la palabra inicial" +
                                 "no puede ser nulo.")
            self._palabra = list(palabra.upper())
        except ValueError:
            raise

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, intentos):
        try:
            if intentos < 0:
                raise ValueError("El valor inicial de intentos" +
                                 "no puede menor o igual 0.")
            self._intentos = intentos
        except ValueError:
            raise

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra):
        try:
            if len(tipo_palabra) == 0 or tipo_palabra is None:
                raise ValueError("El valor del tipo de palabra " +
                                 "no puede ser nulo.")
            self._tipo_palabra = tipo_palabra.upper()
        except ValueError:
            raise

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nombre_jugador):
        try:
            if len(nombre_jugador) == 0 or nombre_jugador is None:
                raise ValueError("El valor del nombre de jugador " +
                                 "no puede ser nulo.")
            self._nombre_jugador = nombre_jugador.upper()
        except ValueError:
            raise

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, palabra_aciertos):
        self._palabra_aciertos = palabra_aciertos
