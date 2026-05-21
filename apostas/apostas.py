from crud.crud import pegar_dados, atualizar_score, atualizar_bets
from utils import  digitar

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



def apostar():
    ...



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