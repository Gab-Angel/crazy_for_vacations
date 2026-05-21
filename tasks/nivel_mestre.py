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
    print("A) O limite lim_{x -> c} f(x) nunca existe.\nB) A função não está definida em x = c.\nC) Os limites laterais em c são obrigatoriamente infinitos.\nD) Pelo menos uma das três condições de continuidade falha: a existência de f(c),\n a existência de lim_{x -> c} f(x) ou a igualdade entre ambos.")

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

    resposta1 = float(input("sua resposta: "))

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
    print("Sejam {u} e {v} vetores no espaço tais que |{u}| = 3, |{v}| = 5 e o ângulo entre eles é de pi/{3} radianos. ")
    print("Determine o volume do paralelepípedo determinado pelos vetores {u} + {v}, {u} - {v} e {u} x {v}")
    print("")
    print("Dica: Utilize as propriedades do produto misto, lembrando que ({u} + {v}) x ( {u} - {v} ) = -2({u} x {v}.")

    resposta1 = float(input("sua resposta (sem u.v.): "))

    if resposta1 == 337.5 :
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
    print("Os vetores {u}, {v} e {w} satisfazem a relação {u} + {v} + {w} = {0}.\n Sabendo que |{u}| = 3, |{v}| = 4 e |{w}| = 5, calcule o valor do \nproduto escalar {u} * {v} + {v} * {w} + {w} * {u}.")
    print("")
    print("Dica: Desenvolva o produto escalar ({u} + {v} + {w}) * ({u} + {v} + {w}) = 0")
    print("")

    resposta1 = int(input("sua resposta: "))

    if resposta1 ==-25 :
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
    print("A reta r passa pelo ponto A(1, 0, 1) e tem a direção do vetor {d} = (1, 2, -1). O plano pi possui a ")
    print("equação cartesiana x + y + z = 1. Determine a equação da projeção ortogonal da reta r sobre o plano pi")
    print("")
    print("para essa questão subistitua a raiz √ por 2 e multiplique")

    resposta1 = int(input("sua resposta: "))

    if resposta1 == 15 :
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
    print("Dois algoritmos realizam exatamente n operações de leitura. O Algoritmo A lê os elementos de um")
    print("array unidimensional sequencialmente. O Algoritmo B lê os elementos de uma lista encadeada")
    print("percorrendo seus ponteiros. Por que o Algoritmo A é drasticamente mais rápido na prática para n grande?")
    print("")
    print("A) O array possui complexidade de busca O(log n), enquanto a lista é O(n).\nB) O array se beneficia da localidade espacial na memória cache, reduzindo os cache misses.\nC) A lista encadeada exige realocação dinâmica a cada leitura efetuada.\nD) O array utiliza busca binária nativa em nível de hardware para encontrar os índices.")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'B':
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_12", 50)
        atualizar_score("mestre", 50)
        colorirgreen("parabéns + 50 pontos")
        digitar("Arrays guardam elementos em blocos contíguos de memória, trazendo\n blocos inteiros para o cache do processador de uma vez (localidade espacial).\n Listas encadeadas têm nós espalhados, gerando múltiplos cache misses.")
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
    print("Ao inserir um elemento no final de um array dinâmico (como list em Python)\n que atingiu sua capacidade máxima, ocorre uma realocação de tamanho geométrico \n(Factor = 2). Qual é a complexidade de tempo de uma inserção individual no pior caso e a\n complexidade amortizada de uma sequência de inserções, respectivamente?")
    print("")
    print("A) O(1) e O(1)\nB) O(n) e O(n\nC) O(n) e O(1)\nD) O(1) e O(n)")
    print("")
    print("")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'C' :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_13", 50)
        atualizar_score("mestre", 50)
        colorirgreen("parabéns + 50 pontos")
        digitar("A inserção que estoura o tamanho exige copiar os $n$ elementos\n antigos para o novo espaço ($O(n)$). Porém, como isso raramente acontece,\n a média de custo por inserção (amortizada) permanece $O(1)$")
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
    print("Em uma tabela hash que utiliza Endereçamento Aberto com sondagem linear\n (Linear Probing), o que acontece se removermos um elemento alterando seu slot\n diretamente para  Vazio (null) sem usar um marcador especial (tombstone)?")
    print("")
    print("A) A tabela hash duplica seu tamanho automaticamente.\nB) O fator de carga ultrapassa instantaneamente o limite de $1.0$.\nC) As buscas por chaves que colidiram e foram inseridas após o elemento removido podem falhar incorretamente.\nD) A função de hash entra em um loop infinito na próxima inserção.")
    print("")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'C':
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_14", 50)
        atualizar_score("mestre", 50)
        colorirgreen("parabéns + 50 pontos")
        digitar("A sondagem linear para de buscar quando encontra um slot vazio.\n Se você simplesmente apagar o elemento, a busca por um item posterior que colidiu achará o vazio\n e dirá que o item não existe. O tombstone avisa: está vazio, mas continue\n procurando".)
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
    print("Se um atacante enviar intencionalmente milhares de\n requisições cujas chaves geram o mesmo valor de hash em um \ndicionário de pior caso tradicional (onde colisões formam listas encadeadas simples),\n qual será a nova complexidade de tempo de busca e o efeito no servidor?")
    print("")
    print("A) O(log n), causando lentidão imperceptível.\nB) O(n), podendo causar um ataque de Negação de Serviço Algébrica (DoS).\nC) O(1), mantendo o servidor perfeitamente estável.\nD) O(n^2), corrompendo a integridade dos dados armazenados.")
    print("")
    print("")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'B' :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_15", 50)
        atualizar_score("mestre", 50)
        colorirgreen("parabéns + 50 pontos")

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
    print("Por que a Otimização de Chamada de Cauda (Tail Call Optimization - TCO)\n impede que funções recursivas com deep stacks causem um estouro de pilha (Stack Overflow)?")
    print("")
    print("A) Ela move os dados da pilha (Stack) diretamente para a memória Heap.")
    print("B) Ela transforma a recursão em uma execução paralela usando threads adicionais")
    print("C) Ela permite que o runtime reutilize o mesmo frame de pilha atual, reduzindo o custo de memória para O(1).")
    print("D) Ela limita o número máximo de chamadas permitidas pelo sistema operacional.")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'C' :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_16", 50)
        atualizar_score("mestre", 50)
        colorirgreen("parabéns + 50 pontos")
        digitar("Se a chamada recursiva é a última ação da função \n(cauda), não há necessidade de guardar o estado da função anterior.\n O compilador reaproveita o frame atual, virando um loop iterativo por baixo dos pano")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_16", -30)
        atualizar_score("mestre", -30)
        colorired("você perdeu 25 pontos!!")


def task_17():
    print(">>"* 10)
    digitar("questão 17 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("Um algoritmo de IA recebe um conjunto de dados contendo o histórico de compras de clientes, sem")
    print("nenhuma classificação prévia ou rótulo, com o objetivo de agrupar perfis semelhantes para")
    print("campanhas de marketing. Esse cenário descreve qual paradigma de aprendizado?")
    print("")
    print("A) Aprendizado Supervisionado (Supervised Learning)\nB) Aprendizado por Reforço (Reinforcement Learning)\nC) Aprendizado Não Supervisionado (Unsupervised Learning)\nD) Aprendizado Semissupervisionado (Semi-supervised Learning)")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'C':
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_17", 60)
        atualizar_score("mestre", 60)
        colorirgreen("parabéns + 60 pontos")
        digitar("Quando os dados não possuem rótulos (labels)\n ou respostas corretas conhecidas, o algoritmo tenta encontrar padrões ocultos por conta \nprópria (como agrupamento ou clustering), o que caracteriza o Aprendizado Não Supervisionado.")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_17", -30)
        atualizar_score("mestre", -30)
        colorired("você perdeu 30 pontos!!")


def task_18():
    print(">>"* 10)
    digitar("questão 18 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("Em um modelo de classificação para diagnosticar uma doença raríssima e altamente letal, o custo")
    print("de liberar um paciente doente (Falso Negativo) é muito maior do que o custo de submeter um")
    print("paciente saudável a exames adicionais (Falso Positivo). Qual métrica deve ser maximizada")
    print("prioritariamente nesse modelo?")
    print("")
    print("A) Precisão (Precision)\nB) Revocação / Sensibilidade (Recall)\nC) Acurácia (Accuracy)\nD) Especificidade (Specificity)")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'B' :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_18", 60)
        atualizar_score("mestre", 60)
        colorirgreen("parabéns + 60 pontos")
        digitar("A Revocação (Recall) mede a proporção de positivos reais que foram identificados\n corretamente. Se queremos evitar ao máximo os Falsos Negativos (deixar passar\n um doente), precisamos de um Recall próximo a 100%.")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_18", -30)
        atualizar_score("mestre", -30)
        colorired("você perdeu 25 pontos!!")


def task_19():
    print(">>"* 10)
    digitar("questão 19 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("Durante o treinamento de uma rede neural profunda, observa-se que a perda (loss) no conjunto de ")
    print("treino continua caindo drasticamente perto de zero, mas a perda no conjunto de validação começa")
    print("a subir. O que está acontecendo com o modelo e como mitigar isso?")
    print("")
    print("A) Underfitting; mitiga-se aumentando a complexidade do modelo.\nB) Overfitting; mitiga-se aplicando técnicas de regularização (como Dropout ou L2).\nC) Overfitting; mitiga-se removendo as camadas de normalização do modelo.\nD) O modelo atingiu a convergência ideal e o treinamento deve continuar indefinidamente")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'B':
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_19", 60)
        atualizar_score("mestre", 60)
        colorirgreen("parabéns + 60 pontos")
        digitar("Quando o modelo decora o conjunto de treino (perda cai) mas perde a \ncapacidade de generalizar para dados novos (perda de validação sobe), ocorre o Overfitting. \nRegularizações como o Dropout forçam a rede a não depender de neurônios específicos.")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_19", -30)
        atualizar_score("mestre", -30)
        colorired("você perdeu 30 pontos!!")


def task_20():
    print(">>"* 10)
    digitar("questão 20 !!!")
    print(">>"*10)
    print("")            
    digitar("lembre-se quando você errar perderá pontos!!")        
    print("")
    print("Em redes neurais artificiais profundas, a função de ativação Sigmoide caiu em desuso nas camadas")
    print("ocultas devido ao problema do Desvanecimento do Gradiente (Vanishing Gradient). Qual função")
    print("de ativação corrigiu esse problema matemático ao manter o gradiente constante igual a 1 para qualquer entrada positiva?")
    print("")
    print("A) Tanh (Tangente Hiperbólica)\nB) Softmax\nC) ReLU (Rectified Linear Unit)\nD) Leaky ReLU")

    resposta1 = (input("sua resposta: ")).upper()

    if resposta1 == 'C' :
        digitar(f"não esperava meus mestres skywalker")
        atualizar_tasks('mestre', "task_20", 60)
        atualizar_score("mestre", 60)
        colorirgreen("parabéns + 60 pontos")
        digitar("A ReLU retorna $0$ para valores negativos e o próprio \nvalor ($x$) para positivos. Como a derivada de $x$ é $1$, o gradiente não \ndiminui à medida que é propagado de volta pelas camadas, resolvendo o vanishing gradient")
    else:
        print("essa tava sal mesmo ")
        atualizar_tasks('mestre', "task_20", -30)
        atualizar_score("mestre", -30)
        colorired("você perdeu 30 pontos!!")



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
    aleatorio = [task_01,task_02,task_03, task_04, task_05, task_06, task_07, task_08, task_09, task_10, task_11, task_12, task_13, task_14, task_15, task_16, task_17, task_18, task_19, task_20 ]
    shuffle(aleatorio) 
    for comando in aleatorio:
        comando ()
