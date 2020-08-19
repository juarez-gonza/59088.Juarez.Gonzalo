from repositorios import Repositorios


class ProductoService:

    def get_producto(self, key):
        try:
            if (key < len(Repositorios.productosList) and Repositorios.productosList[key] is not None):
                producto = Repositorios.productosList[key]
                return producto
            raise KeyError()
        except KeyError:
            raise ValueError("ValueError: key not found")

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
        productosList = list(Repositorios.productosList.values())
        return productosList

    def get_precio_ascendente(self):
        arr = self.get_productosList()
        for i in range(1, len(arr)):
            insert = arr[i]
            j = i - 1
            while j >= 0 and arr[j]["_precio"] > insert["_precio"]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = insert
        return arr

    def get_precio_descendente(self):
        arr = self.get_productosList()
        for i in range(1, len(arr)):
            insert = arr[i]
            j = i - 1
            while j >= 0 and arr[j]["_precio"] < insert["_precio"]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = insert
        return arr
