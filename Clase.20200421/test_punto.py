import unittest
from punto import Punto2D, PuntoMejorado

class TestPunto(unittest.TestCase):
    def test_constr_vacio(self):
        punto = Punto2D(0, 0)
        self.assertEqual(punto.x, 0)
        self.assertEqual(punto.y, 0)
    
    def test_constr_valores(self):
        punto = Punto2D(1, 3)
        self.assertEqual(punto.x, 1)
        self.assertEqual(punto.y, 3)

    def test_punto_mejorado(self):
        punto = PuntoMejorado(1, 3)
        self.assertEqual(punto.cuadrante(), 1)

if __name__ == "__main__":
    loader = unittest.TestLoader().loadTestsFromTestCase(TestPunto)
    unittest.TextTestRunner().run(loader)
    