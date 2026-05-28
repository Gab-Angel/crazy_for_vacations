from inicializacao.inicio import boas_vindas_calourinho, menu
from pathlib import Path
import os

file = Path('session.json')


# aqui vai ficar tudo
def main():
    if not os.path.exists(file):
        boas_vindas_calourinho()

    menu()


if __name__ == '__main__':
    main()