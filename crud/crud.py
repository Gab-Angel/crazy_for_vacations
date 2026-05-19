import json
from pathlib import Path

file = Path("crud/user.json")

def criar_user(nome: str):

    initial_data = {
        "nick_name": "bot",
    "level": "calourinho",
    "score": {
        "calourinho": 0,
        "veterano": 0,
        "mestre": 0,
        "doutor": 0,
        "chefe_do_departamento": 0,
        "reitor": 0,
    },
    "tasks": {
        "calourinho": {
            "task_01": {
                "score": 0,
                "completed": False
            },
            "task_02": {
                "score": 0,
                "completed": False
            },
            "task_03": {
                "score": 0,
                "completed": False
            },
            "task_04": {
                "score": 0,
                "completed": False
            },
            "task_05": {
                "score": 0,
                "completed": False
            },
             "task_06": {
                "score": 0,
                "completed": False
            },
             "task_07": {
                "score": 0,
                "completed": False
            },
             "task_08": {
                "score": 0,
                "completed": False
            },
             "task_09": {
                "score": 0,
                "completed": False
            },
             "task_10": {
                "score": 0,
                "completed": False
            },
         
            
        },
        "veterano": {
            "task_01": {
                "score": 0,
                "completed": False
            },
            "task_02": {
                "score": 0,
                "completed": False
            },
            "task_03": {
                "score": 0,
                "completed": False
            },
            "task_04": {
                "score": 0,
                "completed": False
            },
            "task_05": {
                "score": 0,
                "completed": False
            },
            "task_06": {
                "score": 0,
                "completed": False
            },
            "task_07": {
                "score": 0,
                "completed": False
            },
            "task_08": {
                "score": 0,
                "completed": False
            },
            "task_09": {
                "score": 0,
                "completed": False
            },
            "task_10": {
                "score": 0,
                "completed": False
            },
            "task_11": {
                "score": 0,
                "completed": False
            },
            "task_12": {
                "score": 0,
                "completed": False
            },
            "task_13": {
                "score": 0,
                "completed": False
            },
            "task_14": {
                "score": 0,
                "completed": False
            },
            "task_15": {
                "score": 0,
                "completed": False
            }
            

        },
        "mestre": {
            "task_01": {
                "score": 0,
                "completed": False
            },
            "task_02": {
                "score": 0,
                "completed": False
            },
            "task_03": {
                "score": 0,
                "completed": False
            },
            "task_04": {
                "score": 0,
                "completed": False
            },
            "task_05": {
                "score": 0,
                "completed": False
            },
            "task_06": {
                "score": 0,
                "completed": False
            },
            "task_07": {
                "score": 0,
                "completed": False
            },
            "task_08": {
                "score": 0,
                "completed": False
            },
            "task_09": {
                "score": 0,
                "completed": False
            },
            "task_10": {
                "score": 0,
                "completed": False
            },
            "task_11": {
                "score": 0,
                "completed": False
            },
            "task_12": {
                "score": 0,
                "completed": False
            },
            "task_13": {
                "score": 0,
                "completed": False
            },
            "task_14": {
                "score": 0,
                "completed": False
            },
            "task_15": {
                "score": 0,
                "completed": False
            },
            "task_16": {
                "score": 0,
                "completed": False
            },
            "task_17": {
                "score": 0,
                "completed": False
            },
            "task_18": {
                "score": 0,
                "completed": False
            },
            "task_19": {
                "score": 0,
                "completed": False
            },
            "task_20": {
                "score": 0,
                "completed": False
        },
        "chefe_do_departamento":{
            "task_01": {
                "score": 0,
                "completed": False
            },
            "task_02": {
                "score": 0,
                "completed": False
            },
            "task_03": {
                "score": 0,
                "completed": False
            },
            "task_04": {
                "score": 0,
                "completed": False
            },
            "task_05": {
                "score": 0,
                "completed": False
            }
        },
        "reitor": {
            "task_01": {
                "score": 0,
                "completed": False
            },
            "task_02": {
                "score": 0,
                "completed": False
            },
            "task_03": {
                "score": 0,
                "completed": False
            },
            "task_04": {
                "score": 0,
                "completed": False
            },
            "task_05": {
                "score": 0,
                "completed": False
            }
        }
    }
    }

    if file.is_file():
        ...
    else:
        with open(file, "w") as f:
            json.dump(initial_data, f)
    

    with open(file, 'r') as f:
        dados = json.load(f)

    dados['nick_name'] = nome

    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)


def atualizar_level(level: str):
    with open(file, 'r') as f:
        dados = json.load(f)
    
    dados['level'] = level 

    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)
    

def atualizar_score(level: str, score: int):
    # Abriu o arquivo para edição
    with open(file, 'r') as f:
        dados = json.load(f)


    # verificação de level e atribuição de score
    if level == 'calourinho':
        dados['score']['calourinho'] += score 
    elif level == 'veterano':
        dados['score']['veterano'] += score 
    elif level == 'mestre':
        dados['score']['mestre'] += score
    elif level == 'doutor':
        dados['score']['doutor'] += score 
    elif level == 'chefe_do_departamento':
        dados['score']['chefe_do_departamento'] += score 
    elif level == 'reitor':
        dados['score']['reitor'] += score 
    else:
        raise ValueError('Esse nível não existe')

    # atualiza o arquivo
    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)


def atualizar_tasks(level: str, task_name: str, score: int):
    with open(file, 'r') as f:
        dados = json.load(f)

    dados['tasks'][level][task_name]['score'] = score
    dados['tasks'][level][task_name]['completed'] = True


    with open(file, 'w') as f:
        json.dump(dados, f, indent=4)


def pegar_dados():
    try:
        with open(file, 'r') as f:
            dados = json.load(f)

            return dados
    except Exception as e:
        print(f'Erro ao buscar dados')





if __name__ == "__main__":
    criar_user(input('digite um nome: '))
    # atualizar_level(input('level: '))
    # atualizar_score(input('level: '), int(input('score: ')))
    # atualizar_tasks(input('level: '), input('task_name: '), int(input('score: ')))