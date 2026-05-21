from crud.crud import atualizar_tasks, atualizar_score, atualizar_bets
from utils import digitar
import time

from cores import colorirgreen, colorired, colorirpurple
#começaremos por cáculo


def task_01():
    print(">>"* 10)
    digitar("questão 1 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("esse algoritmo é a tomada de decisão local:\n em cada passo, ele escolhe o caminho que\n parece ser o mais vantajoso naquele momento,\n sem considerar as consequências a longo prazo \nou o custo acumulado até ali.")
    print("")
    print("")

    resposta1 = (input("qual tipo de busca é essa??(todas letras mínusculas e em português):  "))

    if resposta1 == "gulosa" or resposta1 == "gananciosa":
        digitar(f"muito meu veterano")
        atualizar_tasks('veterano', "task_01", 20)
        atualizar_score("veterano", 20)
        colorirgreen("parabéns + 20 pontos")
    else:
        colorired("não foi dessa vez ")
            

def task_02():
    print(">>"* 10)
    digitar("questão 2 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("em 1950 o teste _____, foi um marco na história da IA.")

    resposta1 = (input("qual o nome desse teste:  "))

    if resposta1 == "turing":
        digitar(f"tá sabidinho já ne meu peixe!!")
        atualizar_tasks('veterano', "task_02", 25)
        atualizar_score("veterano", 25)
        colorirgreen("parabéns + 25 pontos")
        atualizar_bets(2)
        colorirpurple('Dia de sorte! Você ganhou 2 bets!!!')
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")

    print("")
    print(">>"* 10)
    digitar("vetores !!!")
    print(">>"*10)
    print("")
    print("")

def task_03():
    print(">>"* 10)
    digitar("questão 3 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("Qual é o módulo do vetor {u} = (3,4)?.")

    resposta1 = (int(input("sua resposta(o mais simplificada possivel):  ")))

    if resposta1 == 5:
        digitar(f"muito meu veterano")
        atualizar_tasks('veterano', "task_03", 20)
        atualizar_score("veterano", 20)
        colorirgreen("parabéns + 20 pontos")
        atualizar_bets(2)
        colorirpurple('Dia de sorte! Você ganhou 2 bets!!!')
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_04():
    print(">>"* 10)
    digitar("questão 4 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("Dados {u} = (1, 2) e {v} = (3, -1), qual o valor de 2{u} + {v}?")
    print("")
    print("dadas as opções:")
    print("")
    print("A) (5, 3)")
    print("B) (4, 1)")
    print("C) (5, 5)")
    print("D) (2, 4)")
    resposta1 = (input("sua resposta(a letra MAIUSCULA):  "))

    if resposta1 == "A":
        digitar(f"essa tava o mel pode dizer")
        atualizar_tasks('veterano', "task_04", 30)
        atualizar_score("veterano", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")

def task_05():
    print(">>"* 10)
    digitar("questão 5 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("O produto escalar entre dois vetores é zero quando:")
    print("")
    print("dadas as opções:")
    print("")
    print("A)São paralelos \nB) São unitários \nC) São ortogonais \nD) Têm o mesmo módulo")
    
    resposta1 = (input("sua resposta(a letra MAIUSCULA):  "))

    if resposta1 == "C":
        digitar(f"essa tava o mel pode dizer")
        atualizar_tasks('veterano', "task_05", 25)
        atualizar_score("veterano", 25)
        colorirgreen("parabéns + 25 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")



def task_06():
    print(">>"* 10)
    digitar("questão 6 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("Considere os vetores {u} = (2, m, -1)$ e {v} = (m, 4, 2).\n Para que os vetores {u} e {v} sejam ortogonais (perpendiculares),\n qual deve ser o valor da constante m?:")
    print("")
    print("dadas as opções:")
    print("")
    print("A) m = 1/3\nB) m = -1/3\nC) m = 3\nD) m = 0\nE) m = 1/2")
    
    resposta1 = (input("qual o valor de m?? (a letra MAIUSCULA):  "))

    if resposta1 == "A":
        digitar(f"essa tava o mel pode dizer")
        atualizar_tasks('veterano', "task_06", 25)
        atualizar_score("veterano", 25)
        colorirgreen("parabéns + 25 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_07():
    print(">>"* 10)
    digitar("questão 7 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("Qual das seguintes alternativas define corretamente o conceito de uma variável na programação?")
    print("")
    print("dadas as opções:")
    print("")
    print("A)Um espaço na memória do computador reservado para armazenar um dado que pode ser alterado durante a execução do programa.\nB)Um tipo de dado que apenas pode assumir valores inteiros e positivos.\nC)Uma função matemática complexa pré-compilada no sistema operativo.\nD)Uma instrução que impede o fluxo do programa de continuar a ser executado.")
    
    resposta1 = (input("sua resposta?? (a letra MAIUSCULA):  ")).upper()

    if resposta1 == "A":
        digitar(f"essa tava o mel pode dizer")
        atualizar_tasks('veterano', "task_07", 25)
        atualizar_score("veterano", 25)
        colorirgreen("parabéns + 25 pontos")
        atualizar_bets(3)
        colorirpurple('Dia de sorte! Você ganhou 3 bets!!!')
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_08():
    print(">>"* 10)
    digitar("questão 8 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("Qual é a estrutura de controlei ideal\n quando se conhece previamente o número exato de \nvezes que um bloco de código deve ser repetido??")
    print("")
    print("dadas as opções:")
    print("")
    print("A)Estrutura de repetição Enquanto (while)\nB) estrutura de repetição para (for)\nC)estrutura condicional se-senão(if-else)\nD)estrututa de escolha mútipla caso (switch-case)")
    
    resposta1 = (input("sua resposta?? (a letra MAIUSCULA):  "))

    if resposta1 == "B":
        digitar(f"essa tava o mel pode dizer")
        atualizar_tasks('veterano', "task_08", 25)
        atualizar_score("veterano", 25)
        colorirgreen("parabéns + 25 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_09():
    print(">>"* 10)
    digitar("questão 9 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("Se uma condição numa estrutura 'Enquanto' (while)\n for inicialmente falsa, quantas vezes o bloco de código interno será executado?")
    print("")
    print("dadas as opções:")
    print("")
    print("A) 0 vezes\nB) Pelo menos 1 vez.\nC) Infinitas vezes, gerando um loop infinito.\nD) Depende do compilador utilizado.")
    
    resposta1 = (input("sua resposta?? (a letra MAIUSCULA):  "))

    if resposta1 == "A":
        digitar(f"essa tava o mel pode dizer")
        atualizar_tasks('veterano', "task_09", 30)
        atualizar_score("veterano", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_10():
    print(">>"* 10)
    digitar("questão 10 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("")
    print("Um vetor (ou array unidimensional) é definido como:")
    print("")
    print("dadas as opções:")
    print("")
    print("A) Uma tabela bidimensional composta por linhas e colunas de tipos de dados variados.\nB) Um ficheiro de texto guardado no disco rígido para persistência de dados.\nC) Uma estrutura de dados homogénea que armazena uma coleção de elementos do mesmo tipo sob um único nome.\nD) Uma função que gera números aleatórios sequenciais")
    
    resposta1 = (input("sua resposta?? (a letra MAIUSCULA):  "))

    if resposta1 == "C":
        digitar(f"boa chico da costa  uau tu tu tu sarru!!")
        atualizar_tasks('veterano', "task_10", 30)
        atualizar_score("veterano", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")

    

def task_11():
    print(">>"* 10)
    digitar("questão 11 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("Considere as seguintes proposições simples: ")
    print("p: O número 7 é primo.q: O número 9 é par")
    print(".Determine o valor lógico (Verdadeiro ou Falso) da proposição composta:")
    print("p^ ¬q")
    print("")
    print("")
    
    resposta1 = (input("sua resposta:  ")).upper()

    if resposta1 == "VERDADEIRA":
        digitar(f"boa chico da costa  uau tu tu tu sarru!!")
        atualizar_tasks('veterano', "task_11", 30)
        atualizar_score("veterano", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_12():
    print(">>"* 10)
    digitar("questão 12 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("A proposição composta dada por (p^ ¬p) é classificada como uma\n Tautologia, uma Contradição ou uma Contingência? ")
    print("")
    print("")
    print("")
   
    resposta1 = (input("sua resposta:  "))

    if resposta1 == "contradição":
        digitar(f"boa chico da costa  uau tu tu tu sarru!!")
        atualizar_tasks('veterano', "task_12", 30)
        atualizar_score("veterano", 30)
        colorirgreen("parabéns + 30 pontos")
        atualizar_bets(9)
        colorirpurple('Dia de sorte! Você ganhou 9 bets!!!')
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_13():
    print(">>"* 10)
    digitar("questão 13 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("A proposição composta é classificada como uma\n Tautologia, uma Contradição ou uma Contingência? ")
    print("")
    print("[(p -> q)^(q -> r)] -> (p -> r)")
    print("")
   
    resposta1 = (input("sua resposta(responda em mínusculo):  "))

    if resposta1 == "tautologia":
        digitar(f"boa chico da costa  uau tu tu tu sarru!!")
        atualizar_tasks('veterano', "task_13", 30)
        atualizar_score("veterano", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


def task_14():
    print(">>"* 10)
    digitar("questão 14 !!!")
    print(">>"*10)
    print("")            
    print("")        
    print("")
    print("")
    print("Simplifique ao máximo a proposição lógica abaixon\n utilizando as propriedades das álgebras booleanas \nleis de De Morgan, distributiva, absorção, etc.): ")
    print("")
    print("~[~(p ^ q) -> ~ p]")
    print("")
   
    resposta1 = (input("sua resposta(responda ^ = e; ~ = não):  "))

    if resposta1 == "p e nao q":
        digitar(f"boa chico da costa  uau tu tu tu sarru!!")
        atualizar_tasks('veterano', "task_14", 30)
        atualizar_score("veterano", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")



def task_15():
    print(">>"* 10)
    digitar("questão 15 !!!")
    print(">>"*10)
    print("")            
    digitar("a mais hard desse nível")        
    print("")
    print("")
    print("Considere três proposições p, q e r.\n Sabe-se que a proposição composta (p^ ~q) <-> (q -> r) é Veradeira.\n Se a proposição q é Verdadeira, determine, obrigatoriamente, os valores lógicos de p e de r. ")
    print("")
    print("obs: sabendo que uma preposição é indeterminavel, responda indeterminada")
    print("")
   
    resposta1 = (input("qual o valor de p: "))
    resposta2 = input(("qual o valor de r: "))

    if resposta1 == 'indeterminada' and resposta2 == 'falsa':
        digitar(f"boa chico da costa  uau tu tu tu sarru!!")
        atualizar_tasks('veterano', "task_15", 35)
        atualizar_score("veterano", 35)
        colorirgreen("parabéns + 35 pontos")
        atualizar_bets(2)
        colorirpurple('Dia de sorte! Você ganhou 2 bets!!!')
    else:
        print("tente dnv.....")
        time.sleep(3)
        colorired("só que não kkkkkk ")


tasks_veterano = [task_01,task_02,task_03,
        task_04, task_05, task_06,
        task_07, task_08, task_09, task_10, task_11, 
        task_12, task_13, task_14, task_15 ]


if __name__ =="__main__":
    print("         / \\")
    print("        /   \\")
    print("       /     \\")
    print("       |     |")
    print("       | cfv |")
    print("       |     |")
    print("      /|     |\\")
    print("     / |     | \\")
    print("    >> |_____| <<")
    print("   >>>>  |  |  <<<<")
    print("  >>>>>>      <<<<<<")
    print(" >>>>>>>>    >>>>>>>>")

    digitar("\n   UMA CAMISINHA ESTOUROU PRA EU NASCER E EU NASCI PARA ESTOURAR!")
    print("")
    print("") 
    digitar(">>"*10)
    digitar("BEM-VINDO VETERANO")
    digitar(">>"*10)
    print("")
    print("")
    digitar("apartir desse momento cada task terá apenas uma resposta")
    digitar("ou seja, se errar não poderá tentar novamente")
    print("")
    print("")
    print("")
    digitar("que comecem os jogos!! ha ha ha ha ha")
    print("")