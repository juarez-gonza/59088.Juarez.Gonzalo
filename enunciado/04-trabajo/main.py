from person import Person
from personService import PersonService
from repository import Repository


def print_dict(dictionary):
    for key in dictionary:
        is_dict = isinstance(dictionary[key], object)
        print(dictionary[key].__dict__) if is_dict else print(dictionary[key])


class App:
    def __init__(self):
        self.person_repo = Repository()
        self.person_service = PersonService(self.person_repo)

    def menu(self):
        flag = True
        while flag:
            print("==MENÚ==")
            print("1. Buscar persona en particular.")
            print("2. Listar el total de personas.")
            print("3. Añadir una persona.")
            print("4. Modificar una persona.")
            print("5. Eliminar una persona.")
            res = int(input("Elegir una acción: "))
            if res == 1:
                id = int(input("Ingresar id de la persona a buscar: "))
                person = self.person_service.find_one(id)
                if person is False:
                    continue
                print(person.__dict__)
            elif res == 2:
                person_dict = self.person_service.find_many()
                print_dict(person_dict)
            elif res == 3:
                self.person_service.add_one(None)
            elif res == 4:
                id = int(input("Ingresar id de la persona a modificar: "))
                self.person_service.update_one(id)
            elif res == 5:
                id = int(input("Ingresar id de la persona a remover de " +
                               "la lista: "))
                self.person_service.delete_one(id)
            else:
                print("Interacción " + str(res) + " no existe")
                flag = False
        print("==FIN INTERACCIÓN==")
        return flag


if __name__ == '__main__':

    app = App()
    persons_dict = app.person_repo.persons
    # Agregamos una persona
    p1 = Person('federico', 'gonzales', '20')
    app.person_service.add_one(p1)

    # Agregamos una persona
    p1 = Person('claudio', 'pico', '33')
    app.person_service.add_one(p1)

    # Agregamos al hermano **********************
    p2 = Person("nicolas", "pico", '40')
    print("===ADD NICOLAS===")
    app.person_service.add_one(p2)

    print_dict(persons_dict)
    # {
    #   0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ',
    #       '_age': '20'},
    #   1: {'_name': 'NICOLAS', '_surname': 'PICO',
    #       '_age': 30},
    #   2: {'_name': 'NICOLAS', '_surname': 'PICO',
    #       '_age': 30}
    # }
    # Update Federico
    print("===UPDATE FEDERICO===")
    app.person_service.find_one(1).age = 30
    print_dict(persons_dict)

    # delete person
    app.person_service.delete_one(2)
    print("===DELETE NICOLAS===")
    print_dict(persons_dict)

    # {
    #   0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ',
    #       '_age': '20'},
    #   1: {'_name': 'NICOLAS', '_surname': 'NICOLAS',
    #       '_age': 41}
    # }
    print("===FIN INICIALIZACIÓN===")
    app.menu()
