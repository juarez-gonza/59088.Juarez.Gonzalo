class Actor:
    def __init__(self, key="", nombre="", apellido=""):
        self.key = key
        self.nombre = nombre
        self.apellido = apellido

    def ingresar(self, modificar=False):
        if (modificar):
            print("Ingresar nuevos datos: ")
        else:
            print("Ingresando actor: ")
        self.nombre = input("   Ingrese nombre: ")
        self.key = hash(self.nombre)
        self.apellido = input("   Ingrese apellido: ")
