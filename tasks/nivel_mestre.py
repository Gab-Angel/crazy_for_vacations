from crud.crud import atualizar_tasks, atualizar_score
from random import shuffle

from cores import colorirgreen, colorired
#começaremos por cáculo

import time
from utils import digitar


def task_01():
    print(">>"* 10)
    digitar("questão 1 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Seja f(x) = x^ln(x) para x > 0. Qual é a primeira derivada f'(x)?")
    print("")

    resposta1 = input("sua resposta(para dividi use X\Y): ")

    if resposta1 == "2\ln(x)":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_01", 40)
        atualizar_score("mestre", 40)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_01", -35)
        atualizar_score("mestre", -35)
        colorired("você perdeu 35 pontos!!")


def task_02():
    print(">>"* 10)
    digitar("questão 2 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Considere a curva definida implicitamente pela equação x^3 + y^3 = 3xy. \nDetermine a inclinação da reta tangente à curva no ponto {3}/{2}, {3}/{2}).")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == 2:
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_02", 35)
        atualizar_score("mestre", 35)
        colorirgreen("parabéns + 35 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_02", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")
    

def task_03():
    print(">>"* 10)
    digitar("questão 3 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Se uma função f(x) é descontínua num ponto x = c, \nqual das seguintes afirmações teóricas é necessariamente verdadeira?")
    print("")
    print("")
    print("A) O limite lim_{x -> c} f(x) nunca existe.\nB) A função não está definida em x = c.\nC) Os limites laterais em $c$ são obrigatoriamente infinitos.\nD) Pelo menos uma das três condições de continuidade falha: a existência de f(c),\n a existência de lim_{x -> c} f(x) ou a igualdade entre ambos.")

    resposta1 = (input("sua resposta: "))

    if resposta1 == "D":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_03", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_03", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_04():
    print(">>"* 10)
    digitar("questão 4 !!!")
    print(">>"*10)
    print("")            
    digitar("a partir de agora quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Qual é a interpretação geométrica correta da afirmação de que lim_{x -> infty} f(x) = L?")
    print("")
    print("")
    print("A) A reta y = L é uma assíntota horizontal do gráfico de f(x) quando x cresce indefinidamente.\nB)A reta x = L é uma assíntota vertical do gráfico da função\nC)A função cessa o seu crescimento e estabiliza rigidamente a partir de um determinado valor de x\nD)A função é limitada superiormente por L para todo e qualquer valor do seu domínio.")

    resposta1 = (input("sua resposta: "))

    if resposta1 == "A":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_04", 35)
        atualizar_score("mestre", 35)
        colorirgreen("parabéns + 35 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_04", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_05():
    print(">>"* 10)
    digitar("questão 5 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Seja a função f(x) = 5x^4 - 3x^2 + 7x - 12. Qual é a sua primeira derivada, f'(x)?")
    print("")
    print("")
    print("a) 20x^3 - 6x + 7\nb) 5x^3 - 3x + 7\nc) 20x^4 - 6x^2 + 7\nd) 20x^3 - 6x")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == "A":
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_05", 35)
        atualizar_score("mestre", 35)
        colorirgreen("parabéns + 35 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_05", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_06():
    print(">>"* 10)
    digitar("questão 6 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Dois vetores, {A} e {B}, partem da mesma origem e formam entre si um ângulo de 60°\n. Sabendo que o módulo de {A} é 5 unidades e o módulo de {B} é 8 unidades, determine:")
    print("")
    print("")
    print("O módulo do vetor diferença {D} = {A} - {B}")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == 7:
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_06", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_06", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_07():
    print(">>"* 10)
    digitar("questão 7 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Sejam os vetores {u} = 2{i} + 3{j} -{k} e {v} = {i} - {j} + 2{k}\n representados em um sistema de coordenadas cartesianas.")
    print("")
    print("")
    print("Calcule o produto escalar {u} * {v}")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == -3:
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_07", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_07", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_08():
    print(">>"* 10)
    digitar("questão 8 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("Dados os pontos A(1, 2), B(4, 6) e C(x, 10) no plano cartesiano:")
    print("")
    print("")
    print("Sabendo que o vetor {AC} é ortogonal (perpendicular) ao vetor {AB},\n encontre o valor da coordenada x do ponto C")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == -29/3:
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_08", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_08", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_09():
    print(">>"* 10)
    digitar("questão 9 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_09", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_09", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_10():
    print(">>"* 10)
    digitar("questão 10 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_10", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_10", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_11():
    print(">>"* 10)
    digitar("questão 11 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_11", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_11", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_12():
    print(">>"* 10)
    digitar("questão 12 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_12", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_12", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_13():
    print(">>"* 10)
    digitar("questão 13 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_13", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_13", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_14():
    print(">>"* 10)
    digitar("questão 14 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_14", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_14", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_15():
    print(">>"* 10)
    digitar("questão 15 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_15", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_15", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



def task_16():
    print(">>"* 10)
    digitar("questão 16 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_16", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_16", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_17():
    print(">>"* 10)
    digitar("questão 17 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_17", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_17", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_18():
    print(">>"* 10)
    digitar("questão 18 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_18", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_18", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_19():
    print(">>"* 10)
    digitar("questão 19 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_19", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_19", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")


def task_20():
    print(">>"* 10)
    digitar("questão 20 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_20", 30)
        atualizar_score("mestre", 30)
        colorirgreen("parabéns + 30 pontos")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_20", -25)
        atualizar_score("mestre", -25)
        colorired("você perdeu 25 pontos!!")



tasks_mestre = [task_01,task_02,task_03, task_04, task_05,   
    task_06, task_07, task_08, task_09, task_10,task_11, 
    task_12, task_13, task_14, task_15, task_16, task_17, 
    task_18, task_19, task_20]




if __name__ =="__main__":
    time.sleep(0.1)
    digitar("      ____________________________________")
    digitar("   //\\                                    |")
    digitar("  //        CRAZY FOR VOCATIONS         |")
    digitar(" //____________________________________|")
    digitar("  |=====================================[ ]>>>")
    digitar(" -|------------------------------------|")
    digitar("  \\ |                                    |")
    digitar("   \\|____________________________________|")
    time.sleep(0.5)
    print("")
    print("")
    print("")
    digitar("####         ____________________________________")
    digitar(" ########//\\                                    |")
    digitar(" ###########//        CRAZY FOR VOCATIONS         |")
    digitar(" ############//____________________________________|")
    digitar(" ###########|=====================================[ ]>>>")
    digitar(" #########|------------------------------------|")
    digitar(" #######\\ |                                    |")
    digitar(" ###### \\|____________________________________|")
    print("")
    print("")
    print("")
    time.sleep(0.5)
    digitar("                                    ____________________________________")
    digitar("   _____                       /|                                    |")
    digitar(" ######### \\_______             / |        CRAZY FOR VOCATIONS         |")
    digitar(" ####___\\       \\___________/_|____________________________________|")
    digitar("########  [====|   UFS   |===============================================[ ]>>>")
    digitar("######## \---/-------/-----------^-|------------------------------------|")
    digitar("#########/-------'             \\ |                                    |")
    digitar("#######-'                      \\|____________________________________|")
    print("")
    print("")
    print("")
    time.sleep(0.5)
    digitar("                                    ____________________________________")
    digitar("   //\\_____                       /|                                    |")
    digitar("  //   \\    \\_______             / |        CRAZY FOR VOCATIONS         |")
    digitar(" //     \\___\\       \\___________/_|____________________________________|")
    digitar("##   ##  [====|   UFS   |===============================================[ ]>>>")
    digitar(" \\\\     /---/-------/-----------^-|------------------------------------|")
    digitar("  \\\\   /    /-------'             \\ |                                    |")
    digitar("   \\\\/`-----'                      \\|____________________________________|")
    print("")
    print("")
    print("")
    time.sleep(0.5)
    digitar("     ====>")
    digitar("   =======>")
    digitar("  ==========>")
    digitar(" ==============> [IGNIÇÃO COMPLETA]")
    digitar("  ==========>")
    digitar("   =======>")
    digitar("     ====>")
    print("")
    print("")
    print("")
    time.sleep(0.3)
    digitar(">>     <<        << <          *      <<<    *     <<<  * ")
    digitar(">>>>>    < <<    *      <<         >     < < <               ")
    digitar(">>>>>>> ___________________________  *   <<      *      < < <      *  ")
    digitar("<<>>>><<<                    \ |   ----_____ < < <<<       *  ")
    digitar("<<>>><<<<        for          | |          ----_______  ")
    digitar("<<<<<<<<<  crazy    vocations | |       ___----  ")
    digitar("<<>>><<<< ___________________/_|___-----          * <<  <*  << <     * ")
    digitar(">>>>>>.      *         < <        <  <<    <<     *   <<   <<  << <       *            ")
    digitar(">>>>            <<    *      << < <          *     < < *  * ")
    digitar(">>       *        <<            << <     *         *       ")
    digitar("   *                 *          < <      ")
    print("")
    print("")
    digitar("GAIA É QUE NEM ANEMIA, SÓ TEM QUEM NÃO COME DIREITO!!!!!!")
    print("")
    print("")
    aleatorio = [task_01,task_02,task_03, task_04, task_05 ]
    shuffle(aleatorio) 
    for comando in aleatorio:
        comando ()
