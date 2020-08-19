from productoServices import ProductoService
from producto import Producto


class App:
    def __init__(self):
        pass

    def menu(self):
        flag = True
        while flag:
            print("1. Agregar producto")
            print("2. Editar producto")
            print("3. Eliminar producto")
            print("4. Salir del menú")
            try:
                eleccion = int(input("elegir una opción: "))
                if eleccion == 1:
                    self.add_producto_forma()
                elif eleccion == 2:
                    self.update_producto_forma()
                elif eleccion == 3:
                    self.delete_producto_forma()
                elif eleccion == 4:
                    flag = False
                else:
                    raise ValueError("valor ingresado no válido. Volver a intentar")
            except ValueError as e:
                print(e)
            print("==============================================")
        return 0

    def add_producto_forma(self):
        try:
            producto = Producto()
            for key in producto.__dict__:
                if (stdin := input(f"{key} del producto: ")) == "":
                    pass
                else:
                    setattr(producto, key, stdin)
            productKey = ProductoService().add_producto(producto)
            print(f"Producto agregado. Key {productKey}")
        except Exception:
            raise

    def update_producto_forma(self):
        productKey = int(input("Ingresar key del producto a modificar: "))
        actualProduct = ProductoService().get_producto(productKey)
        print("Estado actual del producto: ")
        print(actualProduct)
        print("Campos a actualizar (dejar en blanco los que no se quieran cambiar)")
        try:
            producto = Producto().__dict__
            for key in producto:
                if (stdin := input(f"{key} del producto: ")) == "":
                    producto[key] = actualProduct[key]
                    pass
                else:
                    producto[key] = stdin
            ProductoService().update_producto(productKey, producto)
            print("Producto modificado: ")
            print(ProductoService().get_producto(productKey))
        except Exception:
            raise

    def delete_producto_forma(self):
        try:
            productKey = int(input("Ingresar key del producto a eliminar: "))
            producto = ProductoService().get_producto(productKey)
            ProductoService().delete_producto(productKey)
            print("Producto eliminado: ")
            print(producto)
            del producto
        except Exception:
            raise


if __name__ == "__main__":
    app = App()
    app.menu()

    exit(0)
