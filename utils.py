import time
from crud.crud import pegar_dados, atualizar_level

def digitar(texto, velocidade=0.01):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print()


def verificar_score():
    dados = pegar_dados()
    nivel = dados['level']
    score_atual = dados['score'][nivel]

    p_calourinho = 200
    p_veterano = 500
    p_mestre = 600
    p_doutor = 800
    p_chefe_dp = 1000

    if nivel  == 'calourinho' and p_calourinho <= score_atual:
        atualizar_level('veterano')
        digitar(f'''
                {"="*100}

                PARABÉNS VOCÊ SUBIU DE NÍVEL. AGORA VOCÊ SE TORNOU:

                    🎉🥳🎉  === V-E-T-E-R-A-N-O ===  🎉🥳🎉
                
                {"="*100}
                ''')
        
        while True:
            choice = input('Deseja continuar fazendo as tasks s/n? ==>  ').lower()
            if choice == 's':
                return True
            elif choice == 'n':
                return False
            else:
                continue
        
    elif nivel == 'veterano' and p_veterano <= score_atual:
        atualizar_level('mestre')
        digitar(f'''
                {"="*100}

                PARABÉNS VOCÊ SUBIU DE NÍVEL. AGORA VOCÊ SE TORNOU:

                    🎉🥳🎉  === M-E-S-T-R-E ===  🎉🥳🎉
                
                {"="*100}
                ''')
        
        while True:
            choice = input('Deseja continuar fazendo as tasks s/n? ==>  ').lower()
            if choice == 's':
                return True
            elif choice == 'n':
                return False
            else:
                continue
        
    elif nivel == 'mestre' and  p_mestre <= score_atual:
        atualizar_level('doutor')
        digitar(f'''
                {"="*100}

                PARABÉNS VOCÊ SUBIU DE NÍVEL. AGORA VOCÊ SE TORNOU:

                    🎉🥳🎉  === D-O-U-T-O-R ===  🎉🥳🎉
                
                {"="*100}
                ''')
        
        while True:
            choice = input('Deseja continuar fazendo as tasks s/n? ==>  ').lower()
            if choice == 's':
                return True
            elif choice == 'n':
                return False
            else:
                continue
    
    elif nivel  == 'doutor' and p_doutor <= score_atual:
        atualizar_level('chefe_do_departamento')
        digitar(f'''
                {"="*100}

                PARABÉNS VOCÊ SUBIU DE NÍVEL. AGORA VOCÊ SE TORNOU:

            🎉🥳🎉  === C-H-E-F-E__D-O__D-E-P-A-R-T-A-M-E-N-T-O ===  🎉🥳🎉
                
                {"="*100}
                ''')
        
        while True:
            choice = input('Deseja continuar fazendo as tasks s/n? ==>  ').lower()
            if choice == 's':
                return True
            elif choice == 'n':
                return False
            else:
                continue

    elif nivel == 'chefe_do_departamento' and  p_chefe_dp <= score_atual:
        atualizar_level('reitor')
        digitar(f'''
                {"="*100}

                PARABÉNS VOCÊ SUBIU DE NÍVEL. AGORA VOCÊ SE TORNOU:

                    🎉🥳🎉  === R-E-I-T-O-R ===  🎉🥳🎉
                
                {"="*100}
                ''')
        
        while True:
            choice = input('Deseja continuar fazendo as tasks s/n? ==>  ').lower()
            if choice == 's':
                return True
            elif choice == 'n':
                return False
            else:
                continue

            
    return True