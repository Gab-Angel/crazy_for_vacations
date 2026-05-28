from db.crud import create_user, get_data_user
from tasks.task import consultar_tasks
from utils import digitar
from apostas.apostas import trocar_pontos, apostar, sobre
import time
from pathlib import Path
import json

SESSION_FILE = Path('session.json')

#inicialização 

def boas_vindas_calourinho():
    digitar(
        """
        Bem-vindo a sua jornada em busca das férias CALOURO!!!
        No Crazy for Vocations você encontrará a nata do que é ser universitário
        Pra provar que entreterimento e conhecimento andam de mãos dadas
        E que no fim só queremos férias 👍

        Basicamente sua missão aqui é subir de nível
        Para isso você deve resolver as tasks para ganhar pontuação

        Existe os seguintes níveis:

        1 - Calouro
        2 - Veterano
        3 - Mestre
        4 - Doutor
        5 - Chefe do Departamento
        6 - Reitor

        Cada nível tem suas determinadas tasks e sua dificuldade
        Quanto maior seu nível mais difícil ficam as tasks e subir para o próximo nível

        Durante sua Jornada terá muitas outras situações inusitadas e alguns joguinhos.........

        MAAAAASSSS
        SEM ENROLAÇÃO... AVANTE CALOURO!!!
        """
        , 0.01)   
    
    nome_player = input("Primeiro quero saber qual seu nickname:  ")
    user_id = create_user(nome_player)

    try:
        with open(SESSION_FILE, 'w') as f:
            json.dump({
                "user_id": user_id,
                "nick_name": nome_player
                },
                f,
                indent=4
            )
    except:
        raise ('ERRO AO CRIAR SESSION_FILE')





def exibir_dados(dados: dict):
    nickname = dados['nick_name']
    level = dados['level_name']
    score = dados['total_score']
    bets = dados['bets']
    
    print(f'''
    Nickname: {nickname}
    Nível: {level}
    Bets: {bets}
    Pontuação: {score}
''')
    


def task():
    while True:
        digitar('''
            O que vamos fazer:
                
            1 - Fazer Task
            2 - Consultar Tasks
            3 - Sair 
            ''', 0.01)
        choice = input('O que você deseja: ')
        if choice == '1':
            ...

        elif choice == '2':
            consultar_tasks()

        elif choice == '3':
            break


def bets():
    while True:
        digitar("""
        1 - Trocar pontos em jogadas
        2 - Apostar
        3 - Sobre
        4 - Sair
""")
        choice = input('O que você deseja: ')

        if choice == '1':
            trocar_pontos()
        elif choice == '2':
            apostar()
        elif choice == '3':
            sobre()
        elif choice == '4':
            break


def menu():
    while True:
        digitar('=' * 100, 0.01)
        digitar('''
        O que você deseja:
            
        1 - Tasks
        2 - Consultar dados
        3 - Bets
        4 - Sair
    ''', 0.01)

        choice = input('Escolha: ')

        if choice == '1':
            task()


        elif choice == '2':
            with open(SESSION_FILE, 'r') as f:
                data = json.load(f)
            
            user_id = data['user_id']

            dados = get_data_user(user_id)
            exibir_dados(dados)


        elif choice == '3':
            bets()


        elif choice == '4':
            digitar('Saindo')
            time.sleep(1)
            break



if __name__ == "__main__":
    boas_vindas_calourinho()
    menu()