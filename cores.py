from utils import digitar



def colorirwhite(texto):
    return digitar(f"\033[1;37m{texto}\033[m")

def colorired(texto):
    return digitar(f"\033[1;31m{texto}\033[m")

def colorirgreen(texto):
    return digitar(f"\033[1;32m{texto}\033[m")

def coloriryellow(texto):
    return digitar(f"\033[1;33m{texto}\033[m")

def colorirblue(texto):
    return digitar(f"\033[1;34m{texto}\033[m")

def colorirpurple(texto):
    return digitar(f"\033[1;35m{texto}\033[m")

def colorirciano(texto):
    return digitar(f"\033[1;36m{texto}\033[m")

def colorircinza(texto):
    return digitar(f"\033[1;m{texto}\033[m")

#cores invertidas

def colorirwhitei(texto):
    return digitar(f"\033[7;37m{texto}\033[m")

def coloriredi(texto):
    return digitar(f"\033[7;31m{texto}\033[m")

def colorirgreeni(texto):
    return digitar(f"\033[7;32m{texto}\033[m")

def coloriryellowi(texto):
    return digitar(f"\033[7;33m{texto}\033[m")

def colorirbluei(texto):
    return digitar(f"\033[7;34m{texto}\033[m")

def colorirpurplei(texto):
    return digitar(f"\033[7;35m{texto}\033[m")

def colorircianoi(texto):
    return digitar(f"\033[7;36m{texto}\033[m")

def colorircinzai(texto):
    return digitar(f"\033[7;m{texto}\033[m")



# arco_iris = [colorirbluei, colorircianoi, colorirpurplei, colorirgreeni, coloriredi]

# for n in arco_iris:
#     digitar(f'{n("caraca")} ')