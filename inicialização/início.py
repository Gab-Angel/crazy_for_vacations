#inicialização
import time
import sys

def digitar(texto, velocidade=0.05):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print() 


nome_player = input("digite seu nickname:")
digitar(f"tudo bem {nome_player}, seja bem vindo ao crazy for vocations ")
time.sleep(1)
digitar("ou aportugaysando loucos por férias")
time.sleep(1)
digitar("coisa que vc sentirar ao decorrer do curso")
time.sleep(1)
digitar("Dito isso pronto(a) ou não, vamos para o game!")
print("................")
time.sleep(1)
print("................")
time.sleep(1)
print("................")
time.sleep(1)
print("................")
time.sleep(1)
print("................")
time.sleep(2)
digitar(f"vamos lá sua primeira task é achar sua didática calorinho {nome_player}")
digitar(f" tirando onda {nome_player} sua primeira missão é identificar qual sua patente")
time.sleep(4)
digitar("opção A calouro")
digitar("opção B veterano")
digitar("opção C devsenior")
digitar("opção D estombelo")

primeira_task = input("digite sua resposta: ")
while primeira_task != "A":
    if primeira_task == "B":
        digitar("calma ae alegrim dourado")     
    elif primeira_task == "C":
        digitar("alto lá marujo, infelimente ainda não")
    elif primeira_task == "D":
        digitar("nem se você quisse muito")
    else:
        digitar(f"não tem essa alternativa {nome_player}, veja se está minuscula")
    primeira_task = input("digite sua resposta novamente: ") 

if primeira_task == "A":
    digitar(f"parabéns{nome_player}")