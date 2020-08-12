from repositorios import Repositorios


class ProductoService:
    def add_producto(self, producto):
        try:
            key = len(Repositorios.productosList)
            Repositorios.productosList[key] = producto.__dict__
            producto.key = key
            return key
        except Exception:
            raise

    def delete_producto(self, key):
        try:
            if (key < len(Repositorios.productosList)):
                Repositorios.productosList[key] = None
            else:
                raise KeyError()
        except KeyError:
            raise ValueError("ValueError: key not found")

    def update_producto(self, productoKey, dict_product):
        try:
            if (productoKey < len(Repositorios.productosList) and Repositorios.productosList[productoKey] is not None):
                producto = Repositorios.productosList[productoKey]
                producto.update(dict_product)
            else:
                raise KeyError()
        except KeyError:
            raise ValueError("ValueError: key not found")

    def get_productosList(self):
        productosList = [producto for producto in Repositorios.productosList]
        return productosList

