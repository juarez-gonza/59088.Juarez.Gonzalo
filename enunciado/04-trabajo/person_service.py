from person import Person


class PersonService:
    def __init__(self, repository):
        self.repository = repository

    def find_many(self):
        return self.repository.persons

    def find_one(self, id):
        try:
            person = self.repository.persons[id]
            return person
        except KeyError:
            # print("La persona no se encuentra en el repositorio. " +
            #      "Probar de nuevo.")
            return False

    # Agrega una persona en el dicionario person, definido en Repository
    def add_one(self, person=None):
        if person is None:
            person = Person()
            person.set_campos()
        person.id_assign()
        self.repository.persons[person.id] = person
        return person

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_one(self, id):
        self.find_one(id).set_campos()

    # Elimina persona segun key del dic person
    def delete_one(self, key):
        try:
            person = self.find_one(key)
            person.id = None
            # poner None en id hace q el setter levante un error
            # pero es un error esperable dado q se está eliminando
        except ValueError:
            del self.repository.persons[key]
        except KeyError:
            # persona no está en el repositorio, no hay nada q hacer
            pass
