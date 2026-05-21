from crud.crud import criar_user, pegar_dados
from anotacoes.notes import nova_nota, editar_nota, listar_notas, ver_conteudo, deletar_nota
from tasks.task import consultar_tasks, fazer_tasks
from utils import digitar
from cores import colorirciano
from apostas.apostas import trocar_pontos, apostar, sobre
#inicialização from

import time

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

        1 - Calourinho
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
    criar_user(nome_player)

    digitar(f"muito bem {nome_player}, agora você está conosco na jornada!!!")
    time.sleep(0.5)
    colorirciano("CRAZY FOR VOCATIONS")
    digitar("ou aportugaysando loucos por férias")
    time.sleep(0.5)
    digitar("coisa que vc sentirá ao decorrer do curso")
    time.sleep(0.5)
    digitar("Dito isso pronto(a) ou não, vamos para o game!!!")
    print("................")
    time.sleep(0.5)
    print("................")
    time.sleep(0.5)
    print("................")
    time.sleep(0.5)
    print("................")
    time.sleep(0.5)
    print("................")
    time.sleep(0.3)
    digitar(f"vamos lá!!! sua primeira task é achar sua didática calourinho {nome_player} (missão dificil ein KKKKKK)")
    digitar(f" tirando onda {nome_player} sua primeira missão é identificar qual nivel voce acha que merece...")
    time.sleep(4)
    digitar("opção A: calouro")
    digitar("opção B: veterano")
    digitar("opção C: senior")
    digitar("opção D: doutor")
    digitar("opção E: chefe do departamento")
    digitar("opção F: REItor")
 
    primeira_task = input("eai qual vai ser? diga-me: ")

    while True:
        if primeira_task == "A":
            digitar(f"boaa, ponha-se em seu lugar e dê sua devida desimportância")
            break
        elif primeira_task == "B":
            digitar("calma ae alegrim dourado")     
        elif primeira_task == "C":
            digitar("alto lá marujo, infelimente ainda não")
        elif primeira_task == "D":
            digitar('doutor é pra quem é médico?')
        elif primeira_task == 'E':
            digitar("KKKKKKKKKKKKKKKKKKKKKKKKKKKK boa", 0.02)
        elif primeira_task == 'F':
            digitar('papo de virar estampa de camisa, n toque nesse assunto...')
        else:
            digitar(f"não tem essa alternativa {nome_player}, veja se está minuscula")
        primeira_task = input("eai qual vai ser? diga-me: ") 


def exibir_dados(dados: dict):
    nickname = dados['nick_name']
    level = dados['level']
    score = dados['score'][level]
    tasks_completed = []
    tasks_incompleted = []

    for dado in dados['tasks'][level]:
        if dados['tasks'][level][dado]['completed'] == False:
            tasks_incompleted.append(dado)
        else:
            tasks_completed.append(dado)
    
    print(f'''

    Nickname: {nickname}
    Nível: {level}
    Pontuação: {score}
    Tasks completas no nível {level}: {tasks_completed}
    Tasks incompletas no nível {level}: {tasks_incompleted}
''')
    

def anotacoes():
    while True:
        digitar('='*100, 0.01)
        digitar("O que você deseja:")
        digitar('''
        1 - Nova nota
        2 - Listar notas
        3 - Editar nota
        4 - Ver conteudo da nota
        5 - Deletar nota
        6 - Sair
    ''', 0.01)
        
        choice = input('Escolha: ')

        if choice == '1':
            nome = input('Nome da nota que deseja criar: ')
            conteudo = input('O que voce deseja anotar: ')
            nova_nota(nome, conteudo)

        elif choice == '2':
            listar_notas()

        elif choice == '3':
            editar_nota()

        elif choice == '4':
            ver_conteudo()
        
        elif choice == '5':
            deletar_nota()
        
        elif choice == '6':
            break


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
            fazer_tasks()

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
        3 - Fazer anotações
        4 - Bets
        5 - Sair
    ''', 0.01)

        choice = input('Escolha: ')

        if choice == '1':
            task()


        elif choice == '2':
            dados = pegar_dados()
            exibir_dados(dados)
            

        elif choice == '3':
            anotacoes()

        elif choice == '4':
            bets()


        elif choice == '5':
            digitar('Saindo')
            time.sleep(1)
            break



if __name__ == "__main__":
    boas_vindas_calourinho()
    menu()