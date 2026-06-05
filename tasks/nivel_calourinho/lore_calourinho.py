from crud.crud import atualizar_tasks, atualizar_score, atualizar_bets
from utils import digitar
import time
from cores import colorired , colorirgreen
from tasks.nivel_calourinho.nivel_calorinho import task_01, task_02,task_05,task_06,task_07,task_08
from tasks.nivel_calourinho.lore_calourinho_alternativas import bperdido, nãovoudia2

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


digitar('Voce acorda e lembra que seu primeiro dia de aula na faculdade é hj:')
digitar('o que voce vai fazer??')
print("")
digitar("A) levantar da cama")
digitar("B) voltar a dormir")
digitar("C) refletir sobre sua vida")
digitar("D) começar a scrolar videos no tiktok")
print("")


while True:
    resposta = input("sua resposta: ").upper()

    if resposta == 'A':
        colorirgreen("+5 pontos pela disposição")
        atualizar_score("calourinho", 5)
        break
    elif resposta == 'B':
        colorired("perdeu aura -5")
        atualizar_score("calourinho", -5)
    elif resposta == 'C':
        digitar("voce pensou tanto que resolveu trancar o curso sem nem pisar na faculdade..")
    elif responda == 'D':
        digitar("voce scrolou tanto sua for you que perdeu o horário de ir pra ufs...")
time.sleep(2.5)
print("\n\n\n\n")
digitar('- Agora voce está indo pegar seu onibus pois voce não nasceu playboy, porem voce não sabe a rota\n do seu onibus pois não escutou sua mãe quando ela disse pra voce procurar saber:\n\n')
digitar("A)perguntar a um desconhecido\nB)tentar sorte acompanhando um grupo de pessoas que voce acha que vão pra facul\nC)baixar o app de rotas e buscar se informar na hora\nD)gastar todo seu dinheiro do pix para pagar um uber\n\n")
resposta2 = input("digite sua resposta: ").upper()
if resposta2 == 'A':
    digitar('...')
    digitar('esse desconhecido na verdade é um colega do seu curso o nome dele é mirosvaldo')
    colorirgreen("voce consegui um amigo")
elif resposta2 == 'B':
    digitar("o grupo de pessoas não estavam indo pra facul....")
    colorired("voce está perdido")
    bperdido()
elif resposta2 == "C":
    digitar("voce conseguiu achar sem problemas")
elif resposta2 == 'D':
    digitar("voce chegou porém está liso...")

time.sleep(2.5)
print("\n\n\n\n")
digitar("- Voce chega na UFS... observa muitas pessoas de diferentes tipos, cores, personalidades, jeitos... \nSeu corpo treme e voce tem seu primeiro desafio \nna faculdade: encontrar a sala de apresentação de seu curso:")
digitar("A)olhar no grupo de whatsapp que voce entrou pra ter ctz de qual sala é\nB)ir pro seu departamento e buscar informações por lá\nC)mandar mensagem no grupo dos veteranos correndo o risco de ser ignorado\nD)abrir o mapa da UFS que voce baixou em baixa qualidade pois seu smartphone estava sem memoria e verificar o local")
resposta3 = input("sua resposta: ").upper()
if resposta3 == 'A':
    digitar("voce achou a sala")
elif resposta3 == "B":
    digitar("voce não sabe onde fica o departamento e perferiu olhar o zapzap..")
elif resposta3 == "C":
    digitar("voce tentou mandar mensagem mais seu 4g estava fora de área\n(afinal a ufs tem um sinal ruim)")
elif resposta3 == "D":
    digitar("voce se perdeu, porém um colega seu te ajudou a localizar")
time.sleep(2.5)
print("\n\n\n\n")
digitar("voce chegou na sua primeira aula de cáculo A ")
digitar("haahahahhahhha")
digitar("a professora Josenaura gilbert passou o primeiro teste de verificação ")
task_01()
task_02()

print("\n\n\n\n")
digitar("sua aula de calculo acabou!!!")
print('.\n.\n.\n.\n.')
digitar('agora vamos procurar a sala de de programação A\n')
digitar('qual did vc vai??\na)did2 \nb)did3\nc)did4\nd)labratório do DCOMP')

while True:
    resposta = input("sua resposta: ").upper()

    if resposta == 'D':
        colorirgreen("muito bem calorinho")
        break
    elif resposta == 'B':
        colorired("naoooo")
    elif resposta == 'C':
        digitar("naooo")
    elif responda == 'D':
        digitar("naaaoooo")
    else:
        digitar("digite apenas a,b,c ou d")

digitar("sua primeira aula de programação já começou Doutora mistsubist já faz a pergunta classica:\no que é um algoritmo??")
digitar("oq voce vai responder??\na)uma serie se rotinas que o usuario toma\nb)é uma receita de bolo\nc)é uma serie de ações para chegar a um objetivo\nd)uma sequencia finita de instruções")
resposta3 = input("sua resposta: ").upper()
if resposta3 == 'A':
    digitar("todas respostas estão certas de certa forma")
elif resposta3 == 'B':
    digitar("todas respostas estão certas de certa forma")
elif resposta3 == 'C':
    digitar("todas respostas estão certas de certa forma")
else:
    digitar("todas respostas estão certas de certa forma")
print('\n\n\n\n')
digitar('sua aula de programação terminou\nmas ao chegar perto da sala de fundamentos da IA\n')
digitar('um email chega no seu smartfone.....')
time.sleep(1)
digitar("professor chicharito:\n-nossa aula de hoje foi cancelada")
digitar("happy happy\n ")
time.sleep(2)
digitar('primeiro dia concluido com sucesso')

#========
# DIA 2
#========

digitar("\n\n\n=="*15)
digitar("SEGUNDO DIA DE AULA")
digitar("=="*15)
digitar("\n\nbom dia campeão(a) seu dia hoje promete!!")
digitar("antes de tudo quero saber qual seu nível de entusiamos para as tasks diárias?? ")
digitar("\na)muito empolgado\nb)bem empolgado\nc)medianamente entusiasmado\nd)legalzinho\ne)medio legal\nf)puco entusiasmado\ng)pouquissimo entusiasmado\nh)nada entusiasmado")
resposta = input("sua resposta: ").upper()
if resposta == "A":
    print("vocÊ achou mesmo que eu teria respostas diferentes para cada uma das suas respostas???")
    digitar("NINGUÉM LIGA PRO SEU ENTUSIASMO kkkkk")
else:
    print("vocÊ achou mesmo que eu teria respostas diferentes para cada uma das suas respostas???")
    digitar("NINGUÉM LIGA PRO SEU ENTUSIASMO kkkkk")

digitar("\n\n vamos voltar a seguir o roteiro\nvocÊ acorda com a mensagem do seu colega de classe...")
digitar("________________")
digitar("|mirosvaldo UFS|")
digitar(" bom dia caro colega!\n vai para ufs hoje??\nparece que teremos uma palestra\nULTRAMENTE IMPORTANTE PARA O NOOOSSSO \nDESEVOLVIMENTO COMO DISCENTES")
digitar("o que vc vai responder??\n opção a) vou nada zé\n opção b) comparecerei")
resposta2 = input("sua resposta: ").upper()
if resposta2 == "A":
    nãovoudia2()
else:
    digitar("você escolheu ir para aula, muito bem!!")

    digitar("\n\nvocê chegou na ufs e vai para sua aula de fundamentos da matemática\n\nlogo surgiram as primeiras questões")
    digitar("pronto ou não lá vamos nós\n\n")
    task_05()
    task_06()
    digitar("sua aula de fem terminou...\nvamos para a aula de vetores\n las't goo")
    digitar("\n o que é formado pro uma ordenação de pares de pontos:\na)direção\nb)sentido\nc)segmento orientado\nd)módulo ")
    while True:
        resposta3 = input("sua resposta: ").upper()
        if resposta3 == "C":
            digitar(f"muito bem zequinha,continue assim !!!")
                    atualizar_score("calourinho", 30)
                    colorirgreen('parabéns + 30 pontos')
                    break
                else:
                    digitar("não foi dessa fez meu peixe")
                    digitar("tente novamente: ")        
    digitar("\n\n o que é o módulo do vetor\na)comprimento\nb)área\nc)extremidade\nd)seguimento equipolente")
    while True:
        resposta4 = input("sua resposta: ").upper()
        if resposta4 == "A":
            digitar(f"muito bem zequinha,continue assim !!!")
                    atualizar_score("calourinho", 30)
                    colorirgreen('parabéns + 30 pontos')
                    break
                else:
                    digitar("não foi dessa fez meu peixe")
                    digitar("tente novamente: ")

    digitar("\n\nagora decisão EXTREMAMENTE IMPORTANTE você vai ficar para a palestra??")
    digitar('\na)sim\nb)não')
    resposta5 = input("sua resposta: ").upper()
    if resposta5 == "A":
        digitar(" vocÊ asssistiu a palestra e foi interessante")
        atualizar_score("calourinho", 10)
        colorirgreen('parabéns + 10 pontos')
    else:
        digitar("está no seu direito!!!")
    digitar("\n\nfinalmente seu expediente de estudos acabou...\n pode retornar para casa")
    digitar("\ndia concluído com sucesso ")
    digitar("=="*10)
    colorirgreen("+105 conquistados no dia")
    digitar("=="*10)