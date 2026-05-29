from crud.crud import atualizar_tasks, atualizar_score, atualizar_bets
from utils import digitar
import time
from cores import colorired , colorirgreen
from tasks.nivel_calourinho.nivel_calorinho import task_01, task_02
from tasks.nivel_calourinho.lore_calourinho_alternativas import bperdido

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
