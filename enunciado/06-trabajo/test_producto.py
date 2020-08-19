import unittest
from producto import Producto
from parameterized import parameterized
from productoServices import ProductoService
from repositorios import Repositorios


class TestProducto(unittest.TestCase):

    def test_uso_property(self):
        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras'})

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras'})

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras'),
            ("samsung s10", 200000, 'celular'),
            ("samsung s20", 400000, 'celular'),
            ("acer", 6000500, 'computadoras'),
            ("HP", 6000000, 'computadoras'),
        ])
    # Agregar un producto
    def test_add_producto(self, descripcion, precio, tipo):
        producto = Producto(descripcion, precio, tipo)
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto.__dict__)

    def test_get_producto(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             ProductoService().get_producto(productoKey))

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras'),
            ("samsung s10", 200000, 'celular'),
            ("samsung s20", 400000, 'celular'),
            ("acer", 6000500, 'computadoras'),
            ("HP", 6000000, 'computadoras'),
        ])
    # Modificar un producto
    def test_update_producto(self, descripcion, precio, tipo):
        producto = Producto(descripcion, precio, tipo)
        productoKey = ProductoService().add_producto(producto)
        nonUpdated = {**Repositorios.productosList[productoKey]}

        ProductoService().update_producto(productoKey, {"precio": 1})
        self.assertNotEqual(nonUpdated, Repositorios.productosList[productoKey])

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras')
    ])
    # Verificar la exeption al modificar un book con un legajo que no existe
    def test_update_producto_value_error(self, descripcion, precio, tipo):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().update_producto(long_list+1, {"precio": 1})

    # Eliminar un producto
    def test_delete_producto(self):
        ProductoService().delete_producto(0)
        self.assertEqual(Repositorios.productosList.get(0), None)

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras')
    ])
    # Verificar la exeption al modificar un book con un legajo que no existe
    def test_delete_producto_value_error(self, descripcion, precio, tipo):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().delete_producto(long_list+1)

    def test_get_precio_ascendente(self):
        ordered_arr = ProductoService().get_precio_ascendente()
        flag = True
        for i in range(1, len(ordered_arr)):
            flag = True if ordered_arr[i]["_precio"] >= ordered_arr[i-1]["_precio"] else False
            if flag is not True:
                break
        self.assertTrue(flag)

    def test_get_precio_descendente(self):
        ordered_arr = ProductoService().get_precio_descendente()
        flag = True
        for i in range(1, len(ordered_arr)):
            flag = True if ordered_arr[i]["_precio"] <= ordered_arr[i-1]["_precio"] else False
            if flag is not True:
                break
        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()
