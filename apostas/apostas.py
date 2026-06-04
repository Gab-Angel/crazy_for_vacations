from crud.crud import pegar_dados, atualizar_score, atualizar_bets
from db.crud import get_random_items, insert_item_bag, insert_item_vaults, update_user_bets, update_score
from utils import digitar, get_data_session
import random


data = get_data_session()
user_id = data['user_id']



raridade = {
    'comum': 50,
    'raro': 30,
    'epico': 15,
    'lendario': 5,
}

comuns = {
    'bets': [1, 2, 3, 4, 5, 10, 20],
    'score': [10, 20, 30, 40, 50, 100, 150, 200, 300],
    'items': [0]
}

raros = {
    'bets': [5, 7, 9, 10, 20, 50, 100],
    'score': [50, 60, 70, 80, 90, 100, 150, 200, 300],
    'items': [0]
}
epicos = {
    'bets': [5, 7, 9, 10, 20, 50, 100],
    'score': [50, 60, 70, 80, 90, 100, 150, 200, 300],
    'items': [0]
}
lendarios = {
    'bets': [5, 7, 9, 10, 20, 50, 100],
    'score': [50, 60, 70, 80, 90, 100, 150, 200, 300],
    'items': [0]
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


def ver_odds():
    ...


def mensagem_ganho(tipo_de_premio, tipo_e_premio: list) -> None:
    if tipo_de_premio == 'achievements':
        ...
    elif tipo_de_premio == 'items':
        ...
    elif tipo_de_premio == 'bets':
        ...
    elif tipo_de_premio == 'score':
        ...


def girar():
    quant_bets = int(input("Quantas bets você deseja jogar?: "))

    # VERIFICAR SE TEM A QUANTIDADE DE BETS 

    if ...:
        ...


    confirma = input(f"Confirma girar com {quant_bets} bets? s/n: ").lower().strip()

    if confirma == 's':
        # busca raridade randomicamente
        raridade = sortear_raridade(quant_bets)

        # pega tipo e premio que vem da lista de premios no topo do arquivo
        tipo_e_premio = buscar_premio(raridade)

        # o tipo de premio que foi salvo no bd
        tipo_de_premio = guardar_premio(tipo_e_premio, raridade)

        # mensagem que retorna ao user ao salvar o premio
        mensagem_ganho(tipo_de_premio, tipo_e_premio)

        

    elif confirma == 'n':
        ...
    else:
        digitar("Valor digitado inválido!")



def sortear_raridade(bets: int) -> str:
    pesos = raridade.copy()

    luck = 1 + (bets / 100)

    pesos['epico'] *= luck
    pesos['lendario'] *= luck

    result = random.choices(
        list(pesos.keys()),
        weights=list(pesos.values())
    )[0]

    return result


def buscar_premio(raridade: str) -> list:
    if raridade == 'comum':
        tipo = random.choices(
            list(comuns),
            weights=[40, 35, 25]
        )[0]

        premio = random.choice(
            list(comuns[tipo])
        )

        return [tipo, premio]


    elif raridade == 'raro':
        tipo = random.choices(
            list(raros),
            weights=[40, 35, 25]
        )[0]
    
        premio = random.choice(
            list(raros[tipo])
        )

        return [tipo, premio]

    elif raridade == 'epico':
        tipo = random.choices(
            list(epicos),
            weights=[40, 35, 25]
        )[0]
    
        premio = random.choice(
            list(epicos[tipo])
        )

        return [tipo, premio]

    elif raridade == 'lendario':
        tipo = random.choices(
            list(lendarios),
            weights=[40, 35, 25]
        )[0]
    
        premio = random.choice(
            list(lendarios[tipo])
        )

        return [tipo, premio]


def guardar_premio(tipo_e_premio: list, raridade: str) -> str:
    tipo = tipo_e_premio[0]
    premio = tipo_e_premio[1]

    if tipo == 'items':
        item = get_random_items(raridade)

        type = item['type']
        items_id = item['id']

        if type == 'achievements':
            insert_item_vaults(user_id=user_id, items_id=items_id)

            return 'achievements'
        
        elif type == 'items':
            insert_item_bag(user_id=user_id, items_id=items_id)

            return 'items'


    elif tipo == 'bets':
        update_user_bets(user_id,premio)

        return 'bets'
        
    elif tipo == 'score':
        update_score(user_id,premio)

        return 'score'
        



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


    # item = get_random_items('lendario')
    # id_item = item['id']

    # insert_item_vaults(user_id=user_id, items_id=id_item)
    # insert_item_bag(user_id=user_id, items_id=id_item)
    apostar()


