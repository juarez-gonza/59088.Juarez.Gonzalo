class Person:

    def __init__(self, name="", surname="", age=0):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        try:
            if id is None:
                raise ValueError("Los campos no pueden tener valores nulos.")
            else:
                self._id = int(id)
        except ValueError as err:
            print("Error: " + str(err))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        try:
            if name is None:
                raise ValueError("Los campos no pueden tener valores nulos.")
            else:
                self._name = name.upper()
        except ValueError as err:
            print("Error: " + str(err))

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        try:
            if surname is None:
                raise ValueError("Los campos no pueden tener valores nulos.")
            else:
                self._surname = surname.upper()
        except ValueError as err:
            print("Error: " + str(err))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        try:
            if age is None:
                raise ValueError("Los campos no pueden tener valores nulos.")
            else:
                self._age = int(age)
        except ValueError as err:
            print("Error: " + str(err))

    def set_campos(self):
        self.name = input("Ingresar nombre: ")
        self.surname = input("Ingresar apellido: ")
        self.age = input("Ingresar edad ")
