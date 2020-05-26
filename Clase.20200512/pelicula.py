class Pelicula:
    def __init__(self, key="", titulo="", duracion="", generos=""):
        self.key = key
        self.titulo = titulo
        self.duracion = duracion
        self.generos = generos
        self.actores = []

    def ingresar(self, modificar=False):
        if (modificar):
            print("Ingresar nuevos datos: ")
        else:
            print("Ingresando película: ")
        self.titulo = input("   Ingrese titulo: ")
        self.key = hash(self.titulo)
        self.duracion = int(input("   Ingrese duración: "))
        self.generos = input("   Ingrese género: ")

    def listar_cast(self):
        print("===CAST DE " + self.titulo.upper() + "===")
        for i in self.actores:
            print(i.__dict__)
