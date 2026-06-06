from db.crud import (
    get_random_items,
    insert_item_bag,
    insert_item_vaults,
    update_user_bets,
    update_score,
    get_data_user
)
from utils import digitar, get_data_session
from cores import colorired, coloriryellow
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
    'score': [5, 10, 15, 20, 25, 30],
    'items': [0],
    'achievements': [0]
}

raros = {
    'bets': [2, 3, 5, 7, 10, 15, 20],
    'score': [10, 15, 20, 25, 30, 35],
    'items': [0],
    'achievements': [0]
}
epicos = {
    'bets': [3, 5, 8, 10, 15, 20, 30],
    'score': [15, 20, 25, 30, 35, 40],
    'items': [0],
    'achievements': [0]
}
lendarios = {
    'bets': [5, 7, 9, 10, 20, 30, 50],
    'score': [40, 50, 60, 70, 90, 100],
    'items': [0],
    'achievements': [0]
}


def trocar_pontos():
    dados = get_data_user(user_id)
    bets = dados['bets']
    score = dados['total_score']

    digitar(f"""
    Você tem {score} pontos para transfomar em bets
    Bets disponíveis: {bets}
    obs: (cuidado para não deixar sua pontuação negativada, modere!!!)

    Compras de Bets:

    bets    |   custo (em pontos)
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
            update_score(user_id, -25)
            update_user_bets(user_id,1)
            digitar(f'Você acabou de trocar 25 pontos em {troca} jogada')
            
        elif troca == 2:
            update_score(user_id, -50)
            update_user_bets(user_id, 2)
            digitar(f'Você acabou de trocar 50 pontos em {troca} jogadas')

        elif troca == 5: 
            update_score(user_id, -100)
            update_user_bets(user_id, 5)
            digitar(f'Você acabou de trocar 100 pontos em {troca} jogadas')

        elif troca == 10:
            update_score(user_id, -150)
            update_user_bets(user_id, 10)
            digitar(f'Você acabou de trocar 150 pontos em {troca} jogadas')

        elif troca == 15:
            update_score(user_id, -200)
            update_user_bets(user_id, 15)
            digitar(f'Você acabou de trocar 200 pontos em {troca} jogadas')

        elif troca == 20:
            update_score(user_id, -300)
            update_user_bets(user_id, 20)
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


def mensagem_ganho(item: dict) -> None:

    if item['tipo'] == 'achievements':
        name = item['premio']['name']
        raridad = item['premio']['rarity']
        categoria = item['premio']['category']
        descricao = item['premio']['description']

        print(f"=== PARABÉNS VOCÊ GANHOU UM \033[1;32m{'TRÓFEU'}\033[m  ===")
        coloriryellow(f"""

                Nome: {name}
                Raridade: {raridad}
                Categoria: {categoria}
                Descrição: {descricao}
                      
        """)


    elif item['tipo'] == 'items':
        name = item['premio']['name']
        raridad = item['premio']['rarity']
        categoria = item['premio']['category']
        descricao = item['premio']['description']

        print(f"=== PARABÉNS VOCÊ GANHOU UM \033[1;32m{'ITEM'}\033[m  ===")
        coloriryellow(f"""

                Nome: {name}
                Raridade: {raridad}
                Categoria: {categoria}
                Descrição: {descricao}
                      
        """)


    elif item['tipo'] == 'bets':
        premio = item['premio']
        print(f'''
            ===>    SEU PRÊMIO: \033[1;32m{premio}\033[m bets 
        ''')


    elif item['tipo'] == 'score':
        premio = item['premio']
        print(f'''
            ===>    SEU PRÊMIO: \033[1;32m{premio}\033[m pontos 
        ''')


def girar():

    data = get_data_user(user_id)
    bets = data['bets']

    print(f"""
        Bets que você tem disponível: {bets}
    """)

    quant_bets = input("Quantas bets você deseja jogar?: ")

    if quant_bets.isdigit():
        quant_bets = int(quant_bets)
    else:
        colorired("Digite números por favor")
        return


    if quant_bets > bets or bets == 0:
        colorired(f'\nVocê não tem bets suficientes para essa jogada!\nAdquira mais ou diminua sua aposta.')
        return


    confirma = input(f"Confirma girar com {quant_bets} bets? s/n: ").lower().strip()

    if confirma == 's':
        tentativas = 0

        while True:
            tentativas += 1

            if tentativas > 99:
                raise RuntimeError(
                    'Não foi possível encontrar um prêmio válido.'
                )
            
            # busca raridade randomicamente
            raridade = sortear_raridade(quant_bets)

            # pega tipo e premio que vem da lista de premios no topo do arquivo
            tipo_e_premio = buscar_premio(raridade)

            # o tipo de premio que foi salvo no bd
            result = guardar_premio_bd(tipo_e_premio, raridade)
            if result is None:
                continue

            # mensagem que retorna ao user ao salvar o premio
            mensagem_ganho(result)

            # atualiza o bd debitando as bets
            update_user_bets(user_id, -quant_bets)

            break
        

    elif confirma == 'n':
        return
    else:
        digitar("Valor digitado inválido!")


def sortear_raridade(bets: int) -> str:
    pesos = raridade.copy()
    # pesos = raridade
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
            weights=[80, 15, 4, 1]
        )[0]

        premio = random.choice(
            list(comuns[tipo])
        )

        return [tipo, premio]


    elif raridade == 'raro':
        tipo = random.choices(
            list(raros),
            weights=[80, 15, 4, 1]
        )[0]
    
        premio = random.choice(
            list(raros[tipo])
        )

        return [tipo, premio]

    elif raridade == 'epico':
        tipo = random.choices(
            list(epicos),
            weights=[80, 15, 4, 1]
        )[0]
    
        premio = random.choice(
            list(epicos[tipo])
        )

        return [tipo, premio]

    elif raridade == 'lendario':
        tipo = random.choices(
            list(lendarios),
            weights=[80, 15, 4, 1]
        )[0]
    
        premio = random.choice(
            list(lendarios[tipo])
        )

        return [tipo, premio]


def guardar_premio_bd(tipo_e_premio: list, raridade: str) -> dict | None:
    tipo = tipo_e_premio[0]
    premio = tipo_e_premio[1]

    if tipo == 'items':
        item = get_random_items(raridade, tipo, user_id)

        items_id = item['id']

        insert_item_bag(user_id=user_id, items_id=items_id)

        return {
            'tipo': 'items',
            'premio': item
            }
    
    
    elif tipo == 'achievements':
        item = get_random_items(raridade, tipo, user_id)

        if item is None:
            return None
        
        else:
            items_id = item['id']

            insert_item_vaults(user_id=user_id, items_id=items_id)

            return {
                'tipo': 'achievements',
                'premio': item
                }


    elif tipo == 'bets':
        update_user_bets(user_id,premio)

        return {
            'tipo': 'bets',
            'premio': premio
            }
        

    elif tipo == 'score':
        update_score(user_id,premio)

        return {
            'tipo': 'score',
            'premio': premio
            }
        

def apostar():
    while True: 
        digitar('''
    1 - Girar
    2 - Sair

''')
  
        choice = input('O que você deseja: ')

        if choice == '1':
            girar()
        elif choice == '2':
            break
        else:
            digitar('Digite uma das opções acima!!!')





if __name__ == "__main__":
    apostar()

    # for _ in range(20):

    #     raridad = sortear_raridade(1)

    #     # pega tipo e premio que vem da lista de premios no topo do arquivo
    #     tipo_e_premio = buscar_premio(raridad)

    #     # o tipo de premio que foi salvo no bd
    #     result = guardar_premio_bd(tipo_e_premio, raridad)
    #     if result is None:
    #         continue

    #     # mensagem que retorna ao user ao salvar o premio
    #     mensagem_ganho(result)

    #     # atualiza o bd debitando as bets
    #     update_user_bets(user_id, -1)
