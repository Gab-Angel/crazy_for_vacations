from crud.crud import pegar_dados
from utils import verificar_score
from utils import digitar
from random import shuffle
from tasks.nivel_calorinho import tasks_calourinho
from tasks.nivel_veterano import tasks_veterano
# from tasks.nivel_mestre import tasks_mestre


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


def iniciar_task(tasks: list): 
    shuffle(tasks) 

    for comando in tasks:
        comando ()
        decisao = verificar_score()
        
        sair = input('Deseja Continuar? s/n').lower().strip()

        if sair == 'n':
            return

        if decisao == True:
            continue
        else:
            return
        

def fazer_tasks():
    dados = pegar_dados()
    nivel = dados['level']


    if nivel == 'calourinho':
        iniciar_task(tasks_calourinho)
    elif nivel == 'veterano':
        iniciar_task(tasks_veterano)
    elif nivel == 'mestre':
        # iniciar_task(tasks_mestre)
        ...
    elif nivel == 'doutor':
        ...
    elif nivel == 'chefe_do_departamento':
        ...
    else:
        ...



if __name__ == '__main__':
    # consultar_tasks()
    # fazer_tasks()
    verificar_score()