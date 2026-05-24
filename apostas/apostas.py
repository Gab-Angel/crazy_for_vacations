from crud.crud import pegar_dados, atualizar_score, atualizar_bets
from utils import  digitar
import random

raridade = {
    'comum': 50,
    'raro': 30,
    'epico': 15,
    'lendario': 5,
}

comuns = {
    'bets': [1, 2, 3, 4, 5, 10, 20],
    'score': [10, 20, 30, 40, 50, 100, 150, 200, 300],
    'itens': ['comum1', 'comum2', 'comum3']
}

raros = {
    'bets': [5, 7, 9, 10, 20, 50, 100],
    'score': [50, 60, 70, 80, 90, 100, 150, 200, 300],
    'itens': ['raro1', 'raro2', 'raro3']
}
epicos = {
    'bets': [5, 7, 9, 10, 20, 50, 100],
    'score': [50, 60, 70, 80, 90, 100, 150, 200, 300],
    'itens': ['epico1', 'epico2', 'epico3']
}
lendarios = {
    'bets': [5, 7, 9, 10, 20, 50, 100],
    'score': [50, 60, 70, 80, 90, 100, 150, 200, 300],
    'itens': ['Caneta do Reitor', 'Senha da Secretaria', 'Nada']
}


def trocar_pontos():
    dados = pegar_dados()
    bets = dados['bets']
    nivel = dados['level']
    score = dados['score'][nivel]

    digitar(f"""
    Você tem {score} pontos para transfomar em bets
    Bets disponíveis: {bets}
    obs: (cuidado para não deixar sua pontuação negativada, modere!!!)

    Compras de Bets:

    bets  |   custo (em pontos)
    ________|_____________________
            |
    1       |    25
    2       |    50
    5       |   100
    10      |   150
    15      |   200
    20      |   300
    ______________________________

    Escolha com sabedoria...
""")
    while True:
        troca = int(input('Quantos jogadas você quer adquirir: '))

        if troca == 1:
            atualizar_score(nivel, -25)
            atualizar_bets(1)
            digitar(f'Você acabou de trocar 25 pontos em {troca} jogada')
            
        elif troca == 2:
            atualizar_score(nivel, -50)
            atualizar_bets(2)
            digitar(f'Você acabou de trocar 50 pontos em {troca} jogadas')

        elif troca == 5: 
            atualizar_score(nivel, -100)
            atualizar_bets(5)
            digitar(f'Você acabou de trocar 100 pontos em {troca} jogadas')

        elif troca == 10:
            atualizar_score(nivel, -150)
            atualizar_bets(10)
            digitar(f'Você acabou de trocar 150 pontos em {troca} jogadas')

        elif troca == 15:
            atualizar_score(nivel, -200)
            atualizar_bets(15)
            digitar(f'Você acabou de trocar 200 pontos em {troca} jogadas')

        elif troca == 20:
            atualizar_score(nivel, -300)
            atualizar_bets(20)
            digitar(f'Você acabou de trocar 300 pontos em {troca} jogadas')

        else:
            digitar('Escolha uma das opções acima')



        choice = input('Deseja trocar mais pontos? s/n: ').lower().strip()

        if choice == 'n':
            break
        elif choice == 's':
            ...
        else:
            break 



def sobre():
    digitar(f"""
    {'='*100}
    
    Como funciona:
            
    Você tem a possibilidade de apostar com bets.
    Bets são créditos que é possível adquirir através de trocas de pontos
    ou resolvendo determinadas tasks.
    
    Com as bets você conseguirá tentar sua sorte no algoritimo da incerteza:

    Qaunto mais bets você aposta de uma vez maior a chance do algoritmo te entregar
    algo de valor, como:

    1. pontos
    2. bets

    Mas cuidado para não trocar pontos por bets e ficar negativado !!!
    Use com moderação...

    {'='*100}

""")


def premios_bets(categoria: str, premio):
    ...
    

def randomBets(bets: int):
    pesos = raridade.copy()

    luck = 1 + (bets / 100)

    pesos['epico'] *= luck
    pesos['lendario'] *= luck

    result = random.choices(
        list(pesos.keys()),
        weights=list(pesos.values())
    )

    if result == ['comum']:
        categoria = random.choice(list(comuns))
        lista = comuns[categoria]
        premio = random.choice(lista)
        premios_bets(categoria, premio)

    elif result == ['raro']:
        categoria = random.choice(list(raros))
        lista = raros[categoria]
        premio = random.choice(lista)
        premios_bets(categoria, premio)

    elif result == ['epico']:
        categoria = random.choice(list(epicos))
        lista = epicos[categoria]
        premio = random.choice(lista)
        premios_bets(categoria, premio)

    elif result == ['lendario']:
        categoria = random.choice(list(lendarios))
        lista = lendarios[categoria]
        premio = random.choice(lista)
        premios_bets(categoria, premio)

    return categoria, premio



def girar():
    quant_bets = int(input("Quantas bets você deseja jogar?: "))
    confirma = input(f"Confirma girar com {quant_bets} bets? s/n: ").lower().strip()

    if confirma == 's':
        ...

    elif confirma == 'n':
        ...
    else:
        digitar("Valor digitado inválido!")


    


def ver_odds():
    ...


def apostar():
    while True: 
        digitar('''
    1 - Girar
    2 - Ver odds
    3 - Sair

''')
        
        choice = input('O que você deseja: ')

        if choice == '1':
            girar()
        elif choice == '2':
            ver_odds()
        elif choice == 'sair':
            break
        else:
            digitar('Digite uma das opções acima!!!')

    

if __name__ == "__main__":
    # cont = 0
    # while True:
        
    #     if randomBets(1) == ['lendario']:
    #         break
    #     else:
    #         cont += 1
    # print(cont)

    premio = randomBets(1)
    print(premio)
