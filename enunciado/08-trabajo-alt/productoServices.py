from repositorios import Repositorios


class ProductoService:

    def get_producto(self, key):
        try:
            if (key < len(Repositorios.productosList) and
                    Repositorios.productosList[key] is not None):
                producto = Repositorios.productosList[key]
                return producto
            raise KeyError()
        except KeyError:
            raise ValueError("ValueError: key not found")

    def add_producto(self, producto):
        try:
            key = len(Repositorios.productosList)
            Repositorios.productosList[key] = producto
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
            if (productoKey < len(Repositorios.productosList) and
                    Repositorios.productosList[productoKey] is not None):
                producto = Repositorios.productosList[productoKey]
                for attr, value in dict_product.items():
                    setattr(producto, attr, value)
            else:
                raise KeyError()
        except KeyError:
            raise ValueError("ValueError: key not found")

    def get_productosList(self, repo_dict):
        productosList = list(repo_dict.values())
        productosList = [producto for producto in productosList if producto is
                         not None]
        return productosList

    def get_disponiblesList(self, repo_dict):
        productosList = self.get_productosList(repo_dict)
        productosDisponibles = [producto for producto in productosList
                                if producto.disponibilidad == 1]
        return productosDisponibles

    def get_precio_ascendente(self, repo_dict):
        arr = self.get_productosList(repo_dict)
        for i in range(1, len(arr)):
            insert = arr[i]
            j = i - 1
            precio_actual = getattr(insert, "precio")
            while j >= 0 and getattr(arr[j], "precio") \
                    > precio_actual:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = insert
        return arr

    def get_precio_descendente(self, repo_dict):
        arr = self.get_productosList(repo_dict)
        for i in range(1, len(arr)):
            insert = arr[i]
            j = i - 1
            precio_actual = getattr(insert, "precio")
            while j >= 0 and getattr(arr[j], "precio") \
                    < precio_actual:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = insert
        return arr

    def busqueda_binaria(self, repo_dict, precio):
        sorted_arr = self.get_precio_ascendente(repo_dict)
        start = 0
        end = len(sorted_arr)-1
        while start <= end:
            mid = (start + end) // 2
            precio_mid = getattr(sorted_arr[mid], "precio")
            if precio_mid == precio:
                return sorted_arr[mid]
            elif precio_mid > precio:
                end = mid - 1
            else:
                start = mid + 1
        return None
