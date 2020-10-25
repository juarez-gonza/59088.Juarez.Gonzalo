class Repo_Palabras:

    repo = [
            {
             "palabra": "freeBSD",
             "tipo_palabra": "sistemas operativos".upper(),
            },
            {
             "palabra": "python",
             "tipo_palabra": "lenguaje de programacion".upper(),
            }
        ]

    inicializado = False

    def __init__(self):
        pass

    @classmethod
    def get_palabra(repo_class, indice):
        if not repo_class.inicializado:
            with open("word_list.txt", "r") as f:
                while line := f.readline():
                    repo_class.repo.append({
                        "palabra": line,
                        "tipo_palabra": "random"
                        })
            repo_class.inicializado = True
        return repo_class.repo[indice]
