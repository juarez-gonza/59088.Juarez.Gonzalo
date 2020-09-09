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

    def get_productosList(self, repo_dict):
        productosList = list(repo_dict.values())
        productosList = [producto for producto in productosList if producto is not None]
        return productosList

    def get_disponiblesList(self, repo_dict):
        productosList = self.get_productosList(repo_dict)
        productosDisponibles = [ producto for producto in productosList if producto["_disponibilidad"]==1 ]
        return productosDisponibles

    def get_precio_ascendente(self, repo_dict):
        arr = self.get_productosList(repo_dict)
        for i in range(1, len(arr)):
            insert = arr[i]
            j = i - 1
            while j >= 0 and arr[j]["_precio"] > insert["_precio"]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = insert
        return arr

    def get_precio_descendente(self, repo_dict):
        arr = self.get_productosList(repo_dict)
        for i in range(1, len(arr)):
            insert = arr[i]
            j = i - 1
            while j >= 0 and arr[j]["_precio"] < insert["_precio"]:
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
            if sorted_arr[mid]["_precio"] == precio:
                ret = {**sorted_arr[mid]}
                # porque el test al comparar diccionarios no espera la key
                del ret["_key"]
                return ret
            elif sorted_arr[mid]["_precio"] > precio:
                end = mid - 1
            else:
                start = mid + 1
        return None
