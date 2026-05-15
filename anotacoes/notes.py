from pathlib import Path
import json

file = Path('anotacoes/notes.json')

def nova_nota(nome: str, conteudo: str):

    note = {}

    if  file.is_file():
        ...
    else:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(note, f)

    with open(file, 'r') as f:
        dados = json.load(f)

    dados[nome] = conteudo

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)
    
    print(f'Nota --> {nome} <-- criada!!!')


def listar_notas():
    if file.is_file():
        try:
            with open(file, 'r') as f:
                notas = json.load(f)

            if notas:
                for nota in notas: print(f"{'='*10}> {nota}")
            else:
                print(f"""
                    {'='*100}
                    Você não possui notas!!!
                    {'='*100}
                    """) 
        except json.JSONDecodeError:
            print('Arquivo vazio ou inválido' )

    else:
        print(f"""
              {'='*100}
              Você não possui notas!!!
              {'='*100}
              """) 
        

def editar_nota():
    if file.is_file():
        try:
            with open(file, 'r') as f:
                notas = json.load(f)

            if notas:
                nome = input('Nome da nota que deseja editar: ')
                conteudo = input('O que voce deseja anotar: ')
                for nota in notas:
                    if nota == nome:
                        notas[nota] = conteudo


                        with open(file, 'w', encoding='utf-8') as f:
                            json.dump(notas, f, indent=4)
                        
                        print('Nota atualizada')
                        break

                else:
                    print('Você deve ter errado o nome')
            else:
                    print(f"""
                        {'='*100}
                        Você não possui notas para editar!!!
                        {'='*100}
                        """)  
        except Exception as e:
            print(f'Erro: {e}')

    else:
        print(f"""
              {'='*100}
              Você não possui notas para editar!!!
              {'='*100}
              """)


def ver_conteudo():
    if file.is_file():
        try:
            with open(file, 'r') as f:
                dados = json.load(f)
            
            if dados:
                nome = input('Nome da nota que deseja ver o conteúdo: ')
                
                conteudo = dados[nome]

                print(f'Conteúdo === {conteudo} ===')
            
            else:    
                print(f"""
                {'='*100}
                Você não possui notas para visualizar!!!
                {'='*100}
                """)

        except Exception as e:
            print(f'Erro: {e}')
    else:
        print(f"""
              {'='*100}
              Você não possui notas para visualizar!!!
              {'='*100}
              """)


def deletar_nota():
    if file.is_file():
        with open(file, 'r') as f:
            dados = json.load(f)
        try:
            
            if dados:
                nome = input('Nome da nota que deseja deletar: ')

                dados.pop(nome)

                with open(file, 'w') as f:
                    json.dump(dados, f, indent=4)
                
                print(f'Nota --> {nome} <-- deletada!!!')
           
            else:
                print(f"""
              {'='*100}
              Você não possui notas para deletar!!!
              {'='*100}
              """)
        
        except Exception as e:
            print(f'Erro ao deletar: {e}')

    else:
        print(f"""
              {'='*100}
              Você não possui notas para deletar!!!
              {'='*100}
              """)
    


if __name__ == '__main__':
    # nova_nota(input('nome da nota: '), input('Conteudo da nota: '))
    # listar_notas()
    # editar_nota(input('nome da nota: '), input('Conteudo da nota: '))
    # ver_conteudo(input('nome da nota para ver o conteudo: '))
    # deletar_nota(input('nome da nota para deletar: '))

    ...



