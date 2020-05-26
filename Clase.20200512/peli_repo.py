class PeliculaRepo():
    def __init__(self):
        self.peliculas = {}

    def agregar_pelicula(self, key, pelicula):
        self.peliculas[key] = pelicula
