from crud.crud import atualizar_tasks, atualizar_score


#começaremos por cáculo

import time
import sys

def digitar(texto, velocidade=0.05):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print() 
#tesk 1

# --- Desenho de Foguete com >> ---

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
        digitar("parabéns + 20 pontos")
    else:
        print("não foi dessa vez ")
            

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
        digitar("parabéns + 25 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        digitar("só que não kkkkkk ")

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
        digitar("parabéns + 20 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        digitar("só que não kkkkkk ")


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
        digitar("parabéns + 30 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        digitar("só que não kkkkkk ")

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
        digitar("parabéns + 25 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        digitar("só que não kkkkkk ")



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
        digitar("parabéns + 25 pontos")
    else:
        print("tente dnv.....")
        time.sleep(3)
        digitar("só que não kkkkkk ")



if __name__ =="__main__":
    task_01()
    task_02()
    task_03()
    task_04()
    task_05()
    task_06()