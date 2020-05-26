from peli_service import PeliculaService
from peli_repo import PeliculaRepo
from actor_service import ActorService
from actor_repo import ActorRepo


class App():
    def __init__(self):
        self.peli_repo = PeliculaRepo()
        self.actor_repo = ActorRepo()
        self.peli_service = PeliculaService(self.peli_repo)
        self.actor_service = ActorService(self.actor_repo)

    def menu_pelicula(self):
        print("===Menú->Películas===")
        print("1. Listar películas.")
        print("2. Agregar película.")
        print("3. Modificar película.")
        print("4. Eliminar película.")
        print("5. Agegar actor/actriz al cast.")
        print("6. Quitar actor/actriz del cast.")
        print("7. Listar cast de película.")
        try:
            res = int(input("Elegir una acción: "))
            if res == 1:
                app.peli_service.listar_peliculas()
            elif res == 2:
                app.peli_service.agregar_pelicula()
            elif res == 3:
                titulo = input("    Ingresar titulo de la película que " +
                               "se desea modificar: ")
                app.peli_service.modificar_pelicula(hash(titulo))
            elif res == 4:
                titulo = input("    Ingresar titulo de la película que " +
                               "se desea eliminar: ")
                app.peli_service.eliminar_pelicula(hash(titulo))
            elif res == 5:
                app.peli_service.agregar_al_cast(self.actor_service)
            elif res == 6:
                app.peli_service.remover_del_cast(self.actor_service)
            elif res == 7:
                app.peli_service.listar_cast()
            else:
                return False
        except KeyError:
            print("No existe en el repositorio el dato al que se " +
                  "intenta acceder.")
            return False

    def menu_actor(self):
        print("===Menú->Actores/Actrices===")
        print("1. Listar actores/actrices.")
        print("2. Agregar actor/actriz.")
        print("3. Modificar actor/actriz.")
        print("4. Eliminar actor/actriz.")
        try:
            res = int(input("Elegir una acción: "))
            if res == 1:
                app.actor_service.listar_actores()
            elif res == 2:
                app.actor_service.agregar_actor()
            elif res == 3:
                nombre = input("    Ingresar nombre del actor que " +
                               "se desea modificar: ")
                app.actor_service.modificar_actor(hash(nombre))
            elif res == 4:
                nombre = input("    Ingresar nombre del actor que " +
                               "se desea eliminar: ")
                app.actor_service.eliminar_actor(hash(nombre))
            else:
                return False
        except KeyError:
            print("No existe en el repositorio el dato al que se " +
                  "intenta acceder.")
            return False

    def menu_general(self):
        print("===Menú===")
        flag = True
        while(flag):
            print(" 1. Menu de películas")
            print(" 2. Menú de actores/actrices")
            res = int(input("Elegir una opción: "))
            if res == 1:
                flag = self.menu_pelicula()
            if res == 2:
                flag = self.menu_actor()
            else:
                flag = False


if __name__ == "__main__":
    app = App()
    while True:
        app.menu_general()
