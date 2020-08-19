class Producto:

    def __init__(self, descripcion=None, precio=None, tipo=None):
        self.precio = precio
        self.descripcion = descripcion
        self.tipo = tipo

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = int(precio) if precio is not None else None

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = str(descripcion) if descripcion is not None else None

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = str(tipo) if tipo is not None else None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = int(key)

    def update(self, dictionary):
        for key, value in dictionary:
            if key[0] != "_":
                key = "_{0}".format(key)
            self[key] = value