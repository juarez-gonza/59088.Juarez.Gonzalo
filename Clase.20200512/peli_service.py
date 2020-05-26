from pelicula import Pelicula


class PeliculaService:
    def __init__(self, repository):
        self.repository = repository

    def listar_peliculas(self):
        print("Listar")
        if self.repository.peliculas is not None:
            for key in self.repository.peliculas:
                print("     - " + str(self.repository.peliculas[key].__dict__))
        else:
            print("Aún no se han añadido películas.")

    def agregar_pelicula(self):
        print("Agregar")
        pelicula = Pelicula()
        pelicula.ingresar()
        self.repository.agregar_pelicula(pelicula.key, pelicula)
        print("Película agregada exitosamente.")

    def modificar_pelicula(self, key):
        pelicula = self.repository.peliculas[key]
        pelicula.ingresar(True)
        print("Película modificada exitosamente")

    def eliminar_pelicula(self, key):
        confirmar = input("Seguro que desea eliminar esta película?(Y/N)")
        if (confirmar[0].upper() == "Y"):
            del self.repository.peliculas[key]
            print("Película removida exitosamente.")
        return

    def get_pelicula(self):
        while(True):
            try:
                titulo = input("Ingresar título de la película a buscar: ")
                pelicula = self.repository.peliculas[hash(titulo)]
                return pelicula
            except KeyError:
                print("El actor no se encuentra en la base de datos. Probar " +
                      "de nuevo.")

    def agregar_al_cast(self, actor_service):
        actor = actor_service.get_actor()
        pelicula = self.get_pelicula()
        pelicula.actores.append(actor)
        print(actor.nombre + " agregado exitosamente al cast de " +
              pelicula.titulo)

    def remover_del_cast(self, actor_service):
        actor = actor_service.get_actor()
        pelicula = self.get_pelicula()
        pelicula.actores.remove(actor)
        print(actor.nombre + " removido exitosamente del cast de " +
              pelicula.titulo)

    def listar_cast(self):
        self.get_pelicula().listar_cast()
