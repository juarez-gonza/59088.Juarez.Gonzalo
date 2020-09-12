import unittest
from punto import Punto2D, PuntoMejorado


class TestPunto(unittest.TestCase):
    def test_constr_vacio(self):
        punto = Punto2D(0, 0)
        self.assertEqual(punto.x, 0)
        self.assertEqual(punto.y, 0)

    def test_constr(self):
        punto = Punto2D(1, 3)
        self.assertEqual(punto.x, 1)
        self.assertEqual(punto.y, 3)

    def test_cuadrante_uno(self):
        punto = PuntoMejorado(1, 3)
        self.assertEqual(punto.cuadrante(), 1)

    def test_cuadrante_dos(self):
        punto = PuntoMejorado(-1, 3)
        self.assertEqual(punto.cuadrante(), 2)

    def test_cuadrante_tres(self):
        punto = PuntoMejorado(-1, -3)
        self.assertEqual(punto.cuadrante(), 3)

    def test_cuadrante_cuatro(self):
        punto = PuntoMejorado(1, -3)
        self.assertEqual(punto.cuadrante(), 4)


if __name__ == "__main__":
    loader = unittest.TestLoader().loadTestsFromTestCase(TestPunto)
    unittest.TextTestRunner().run(loader)
