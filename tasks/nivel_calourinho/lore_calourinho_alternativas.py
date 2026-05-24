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
