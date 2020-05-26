class Punto2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print("Coordenadas (" + str(self.x) + ", " + str(self.y) + ")")


class PuntoMejorado(Punto2D):
    def cuadrante(self):
        cuadrante = "Cuandrante 0"
        
        if self.x > 0 and self.y > 0:
            cuadrante = "Cuadrante 1"
        elif self.x < 0 and self.y > 0:
            cuadrnate = "Cuadrnate 2"
        elif self.x < 0 and self.y < 0:
            cuadrnate = "Cuadrante 3"
        elif self.x > 0 and self.y < 0:
            cuadrnate = "Cuadrante 4"
        
        print("El punto de coordenadas (" + str(self.x) + ", " + str(self.y) + ") pertenece al cuadrante " + cuadrante)
        
        return int(cuadrante.split(" ")[1])

if __name__ == "__main__":
    punto = Punto2D()
    punto_mejorado = PuntoMejorado(3, 4)

    punto.mostrar_coordenadas()
    punto_mejorado.mostrar_coordenadas()

    punto_mejorado.cuadrante()

