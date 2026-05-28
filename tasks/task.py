from crud.crud import pegar_dados
from utils import verificar_score
from utils import digitar
from random import shuffle


def consultar_tasks():
    dados = pegar_dados()

    nivel = dados['level']
    concluidos = []
    inconcluidos = []

    for task in dados['tasks'][nivel]:
        if dados['tasks'][nivel][task]['completed'] == True:
            concluidos.append(task)
        else:
            inconcluidos.append(task)
    
    digitar(f'Tasks concluídas do nível {nivel}:', 0.01)
    if concluidos:
        for c in concluidos:
            digitar(f"{'='*10}> {c}", 0.03)
    else:
        digitar(f"{'='*10}> Não há Tasks Concluídas", 0.01)
    
    digitar('='*100, 0.01)

    digitar(f'Tasks inconcluída do nível {nivel}:', 0.01)
    if inconcluidos:
        for c in inconcluidos:
         digitar(f"{'='*10}> {c}", 0.03)
    else:
        digitar(f"{'='*10}> Não há Tasks Inconcluídas", 0.01)



if __name__ == '__main__':
    # consultar_tasks()
    verificar_score()