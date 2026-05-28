from crud.crud import atualizar_tasks, atualizar_score, atualizar_bets
from utils import digitar
import time
from cores import colorired


def task_01():
    print("")
    digitar("\n resolva: ")
    print("\n (5)²³\n -----\n (5)²¹")

    time.sleep(1)
    while True:
        resposta = int(input("sua resposta: "))

        if resposta == 25:
            digitar(f"very good ")
            atualizar_tasks('calourinho', "task_01", 20)
            atualizar_score("calourinho", 20)
            digitar("parabéns + 20 pontos")
            break
        else:
            digitar("errou feio painho")
            digitar("tente novamente: ")


def task_02():
    digitar(">>"* 10)
    digitar("questão 2 !!!")
    digitar(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    print("\nx² -x - 12 ")
    print("")
    while True:
        resposta2 = (input("sua resposta: "))

        if resposta2 == "-3,4" or resposta2 == "4,-3":
            digitar(f"muito bem zequinha,continue assim !!!")
            atualizar_tasks('calourinho', "task_02", 25)
            atualizar_score("calourinho", 25)
            digitar("\033[32mparabéns + 25 pontos\033[m")
            break
        else:
            digitar("não foi dessa fez meu peixe")
            digitar("tente novamente: ")        


def task_03():
    digitar(">>"* 10)
    digitar("questão 3 !!!")
    digitar(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    print("\n|x-4| < 3 ")
    print("")
    while True:
        resposta3 = input("obs: os dois agarismos devem se separados por vírgula\n sua resposta: ")

        if resposta3 == "1,7":
            digitar(f"muito bem zequinha,continue assim !!!")
            atualizar_tasks('calourinho', "task_03", 25)
            atualizar_score("calourinho", 25)
            digitar("\033[32mparabéns + 25 pontos\033[m")
            break
        else:
            digitar("não foi dessa fez meu peixe")
            digitar("tente novamente: ")        


def task_04():
    digitar(">>"* 10)
    digitar("questão 4 !!!")
    digitar(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    print("\nlim x²-1/x-1\n(x->1)")
    print("")
    while True:
        resposta3 = float(input("sua resposta: "))

        if resposta3 == 2:
            digitar(f"muito bem zequinha,continue assim !!!")
            atualizar_tasks('calourinho', "task_04", 30)
            atualizar_score("calourinho", 30)
            digitar("\033[32mparabéns + 30 pontos\033[m")
            break
        else:
            digitar("não foi dessa fez meu peixe")
            digitar("tente novamente: ")        

    #iniciaremos fem

    digitar(">>"*10)
    digitar("partiu FEM calourinho!!!")
    digitar(">>"*10)
    print('')
    print("")

def task_05():
    print(">>"* 10)
    digitar("questão 5 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    digitar("p:faltar aula pra jogar sinuca\nq:serei aprovado ")
    print("\np => q")
    print("")
    while True:
        resposta4 = (input("responda se a sentença é verdadeira ou falsa:  "))

        if resposta4 == "falsa":
            digitar(f"infelizmente o cara não pode ter tudo na vida")
            atualizar_tasks('calourinho', "task_05", 20)
            atualizar_score("calourinho", 20)
            digitar("\033[32mparabéns + 20 pontos\033[m")
            atualizar_bets(2)
            colorired('Dia de sorte! Você ganhou 2 bets!!!')
            break
        else:
            digitar("queria que fosse verdade...")
            digitar("tente novamente: ")        


def task_06():
    print(">>"* 10)
    digitar("questão 6 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    digitar("p:faltar aula pra jogar sinuca\nq:serei aprovado \nr: eu estudei")
    print("p: V\nq: F\nr: V")
    print("se eu estudar então serei aprovado ou serei aprovado\n se somente se faltar aula pra jogar sinuca ")
    print("")
    while True:
        resposta6 = (input("responda se a sentença é verdadeira ou falsa:  "))

        if resposta6 == "verdadeira":
            digitar(f"muito bem zeca pagodinho")
            atualizar_tasks('calourinho', "task_06", 25)
            atualizar_score("calourinho", 25)
            digitar("\033[32mparabéns + 25 pontos\033[m")
            break
        else:
            digitar("não foi dessa vez chicão")
            digitar("tente novamente: ")        


def task_07():
    print(">>"* 10)
    digitar("questão 7 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    digitar("resolva: ")
    digitar("p: fiz a prova\nq:serei aprovado \nr: eu estudei")
    print("p: V\nq: F\nr: F")
    print("se eu fizer a prova, então serei aprovado ou se fiz a prova, então estudei")
    print("")
    while True:
        resposta7 = (input("responda se a sentença é verdadeira ou falsa:  "))

        if resposta7 == "falsa":
            digitar(f"muito bem chico sience")
            atualizar_tasks('calourinho', "task_07", 25)
            atualizar_score("calourinho", 25)
            digitar("\033[32mparabéns + 25 pontos\033[m")
            atualizar_bets(5)
            colorired('Dia de sorte! Você ganhou 5 bets!!!')
            break
        else:
            digitar("não foi dessa vez chicão")
            digitar("tente novamente: ")        



def task_08():
    print(">>"* 10)
    digitar("questão 8 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("Proposições:")
    print("p: O código compila")
    print("q: Existe um erro de lógica")
    print("r: O programador toma café")
    print("\nAnalise a validade da sentença para os valores:")
    print("p = V, q = V, r = F")
    print("\nExpressão: ((p ∧ ¬q) ↔ r) ⊕ (p ∧ q)")
    while True:
        resposta7 = (input("responda se a sentença é verdadeira ou falsa:  "))

        if resposta7 == "falsa":
            digitar(f"muito good tirou onda aqui")
            atualizar_tasks('calourinho', "task_08", 30)
            atualizar_score("calourinho", 30)
            digitar("\033[32mparabéns + 30 pontos\033[m")
            break
        else:
            digitar("aconteçe com as melhores famílias chicão ")
            digitar("tente novamente: ")        

    # tasks de fundamentos da IA

   

def task_09():
    digitar(">>"*10)
    print("fundamentos da IA")
    digitar(">>"*10)
    print("")
    print("")
    print("")
    print(">>"* 10)
    digitar("questão 9 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("o que significa o A do PEAS?? ")
    while True:
        resposta7 = (input("responda em português:  "))

        if resposta7 == "atuadores":
            digitar(f"muito bem calorinho")
            atualizar_tasks('calourinho', "task_09", 25)
            atualizar_score("calourinho", 25)
            digitar("\033[32mparabéns + 25 pontos\033[m")
            break
        else:
            digitar("vamos, você consegue ")
            digitar("tente novamente: ")        



def task_10():
    print(">>"* 10)
    digitar("questão 10 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("É uma descrição matemática abstrata que \nmapeia qualquer sequência de percepções em uma ação específica \n($f: P^* -> A$). ")
    print("")
    print("")
    print("obs: responda ecatamente como é está escrito na pergunta")
    while True:
        resposta7 = (input("É a função_do_agente ou programa_do_agente??:  "))

        if resposta7 == "função_do_agente":
            digitar(f"muito bem calorinho")
            atualizar_tasks('calourinho', "task_10", 25)
            atualizar_score("calourinho", 25)
            digitar("\033[32mparabéns + 25 pontos\033[m")
            atualizar_bets(2)
            colorired('Dia de sorte! Você ganhou 2 bets!!!')
            break
        else:
            digitar("vamos, você consegue ")
            digitar("tente novamente: ")        




if __name__ == "__main__":
    print("\033[34m            / \\")
    print("\033[34m           /   \\")
    print("\033[34m          /     \\")
    print("\033[34m          |     |")
    print("\033[34m          | cfv |")
    print("\033[34m          |     |")
    print("\033[34m         /|     |\\")
    print("\033[34m        / |     | \\")
    print("\033[36m      >>  |_____| <<")
    print("\033[33m    >>>>  | | | |  <<<<")
    print("\033[33m   >>>>>>         <<<<<<")
    print("\033[31m  >>>>>>>>         <<<<<<<<\033[m")

    digitar("\n   UMA CAMISINHA ESTOUROU PRA EU NASCER E EU NASCI PARA ESTOURAR!")
    print("")
    print("") 

    digitar(">>"* 10)
    digitar("\033[;30;46mnível calouro!!!\033[m")
    digitar(">>"*10)

    print("")
    print("")