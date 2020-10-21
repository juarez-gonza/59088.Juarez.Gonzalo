import re


def tomar_input(mensaje, bool_letra=True):
    patron = "^[a-zA-Z]+[ ]?[a-zA-Z]?$" if bool_letra\
        else "^[1-9]{1}[0-9]?$"
    while (entrada := re.compile(patron).search(str(input(mensaje)))) is None:
        continue
    if (entrada := entrada.group()).lower() == "salir":
        raise SystemExit("Salir del programa.")
    return entrada if bool_letra else int(entrada)
