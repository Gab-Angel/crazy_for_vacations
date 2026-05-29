from utils import digitar
import time
from cores import colorired, colorirgreen


def bperdido():
    print("voce está andando por um bairo desconhecido, vê um onibus com UFS no letreiro\no que fazer ???\n\nA)subir nele\nB)deixar passar e ir a pé")
    respostab = input("").upper()
    if respostab == "A":
        colorirgreen("voce chegou na ufs a tempo..")
    else:
        colorired("voce até chegou porém, perdeu a aula de calculo")
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