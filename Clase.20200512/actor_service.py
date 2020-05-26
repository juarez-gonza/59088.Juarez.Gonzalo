from actor import Actor


class ActorService:
    def __init__(self, repository):
        self.repository = repository

    def listar_actores(self):
        print("Listar")
        if self.repository.actores is not None:
            for key in self.repository.actores:
                print("     - " + str(self.repository.actores[key].__dict__))
        else:
            print("Aún no se han añadido actores.")

    def agregar_actor(self):
        print("Agregar")
        actor = Actor()
        actor.ingresar()
        self.repository.agregar_actor(actor.key, actor)
        print(actor.nombre + " " + actor.apellido +
              "agregado exitosamente a repositorio.")

    def modificar_actor(self, key):
        actor = self.repository.actores[key]
        actor.ingresar(True)
        print(actor.nombre + " " + actor.apellido +
              "modificado exitosamente en repositorio.")

    def eliminar_actor(self, key):
        confirmar = input("Seguro que desea eliminar este actor?(Y/N)")
        if (confirmar[0].upper() == "Y"):
            del self.repository.actores[key]
            print("eliminado exitosamente de repositorio.")
        return

    def get_actor(self):
        while(True):
            try:
                nombre = input("Ingresar nombre del actor a buscar: ")
                actor = self.repository.actores[hash(nombre)]
                return actor
            except KeyError:
                print("El actor no se encuentra en la base de datos. Probar " +
                      "de nuevo.")
