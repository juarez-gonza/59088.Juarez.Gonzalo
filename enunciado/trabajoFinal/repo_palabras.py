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

    def __init__(self):
        pass

    @classmethod
    def get_palabra(repo_class, indice):
        return repo_class.repo[indice]
