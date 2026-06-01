# começamos dia 11/05/2026 às 21h:10 (segunda-feira)
*definimos ideias
- chegamos na conclusão de fazer um rpg voltado para os estudos
- sob a ótica do nosso curso
- discutimos e aprendemos como fazer o projeto em colab

## dia 12/05
- fizemos o crud
- as 5 primeiras tasks
- adicionamos o sistema que capta o score do player
- tela inicial(provisória)

## dia 13/05
- atualizou crud
- 5 tasks adicionadas
- função do menu inicializada
- estrutura de dados do user atualizadas
- teste de tasks: funcionando 
- função de atualizar tasks melhorada
- diário de bordo inicializado

# dia 14/05
- atualizamos o crud (alteramos algumas patentes erradas0)
- 10 tasks do nivel calorinho finalizada
- 5 tasks dp nivel veterano
- fizemos a pasta de anotações

# dia 15/05

Angel:

- conclusão da funcionalidade de anotações:
1. criar nota
2. editar nota
3. listar notas
4. ver conteído da nota

- atualização de pegar dados do crud
- mudanças em inicializacao:
1. função task

- mudanças no nivel_calourinho:
1. melhoria da ramdomização das tasks em uma função
2. função para iniciar tasks 

- arquivo task.py:
1. consultar_tasks
2. fazer_tasks

- arquivo utils.py
1. colocado função digitar
2. criada função verificar_escore

- criada main.py 

---
Jorge:

- atualizei todas as tasks:
1. garanti isonomia nas questões
2. randomizaei o as questões
3. corrigir uma patente no arquivo crud
4. adicionei mais uma task no nivel veterano
- finalizado o nivel_veterano
- foguete novo frase nova
- nivel_mestre atualizado com lógica de perda

# dia 16/05
Angel:

- lógica de inicialização inserida na main
- mudanças na chamada de função dos arquivos de tasks (agora a função está no arquivo de funcionalidades: task.py)
- refatoração da função de verificar score

Jorge:

- garanti a isonomia dos níveis
- adicionei + 5 tasks ao nivel_veterano
§§ criei um relatório de tasks:
    - nesse relatório dei o somatório analítico para a progressão de level
    - favor observar, que a relação é acumulativa
    - irá nos ajudar a manter a coerência das tasks para cada nível e modo de cobrança  

# dia 17/05
Jorge:
- criei um sistema de cores para as tesks
- indicadores de erro e acerto (red,green)
- consertei a função digitar que estava muito rápida em alguns arquivos
- consertei o texto do início ("aquela parte do aportugaysando") que tava incoerente

# dia 18/05

- dia da convocação do neymar!!!!!
- correção de bugs
- eliminação de código desnecessário: função digitar2 deletada


# dia 19/05
Jorge:
- 20 feitas com 11 vazias
- score da nivel mestre 1100 para subir de level
- pequenas correções


# dia 20/05 
Jorge:
- 20 tasks do nivel mestre concluidas
- garanti a rígidez do nível_mestre deixando as questões equitativas
- grade de possibilidades 2% de chance de passar com 9 tasks
- por padrão 13,14 questões seguidas (só os fortes sobrevivem)

Angel:
- criou a blazer dentro do cfv só falta o conteúdo agora
- criado as bets:
1. função de apostar no menu
2. função de trocar pontos em bets
3. função 'sobre'
4. crud: função atualizar_bets
5. otimização das cores
6. logica de ganhar bets nas tasks

# dia 21/05

Jorge:
- apresentou para o novo integrante Gabriel suas resonsabilidades
- discutiu com Angel o futuro do CFV

Angel:
- observou Jorge apresentar a Gabriel suas responsabilidades
- discutiu com Jorge o futuro do CFV
- pasta lore criada

Gabriel:
=================   INGRESSOU NO PROJETO!!!   ================================
criou o guia: 
responsável por ser um guia da historia, ou guia que ensinar os recursos do game

# dia 24/05
Jorge:
- Iniciei a lore do nivel calourinho 
- lore do calouro alternativa
Angel:
- apostas criei randombets
 - definir a raridade das premiações
 - criei a função girar
 - inicio a função premiosbets

# 25/05

Jorge:
- inseriu as task na tabela tasks

Angel:
- criou pasta db
- conn.py
- crud.py
- tables.py
- função de criar tabelas
- função de deletar tabelas 


# 27/ 05

Angel:
- atualizações no crud:
1. create_user
2. update_level
3. update_score
4. register_user_tasks
5. get_data_user

- varias alterações em outras partes do projeto que estavam ultrapassadas
- rename init_db.py


# 28/05

Angel:
- inicialização atializada:
1. anotações deletada da lógica do projeto
2. boas_vindas_calouro atualizada
- session.json criado para salvar sessão do player
- tabelas criadas:
1. vaults
2. achievements
3. items
4. bags

para fazer:
1. chamada de tasks
2. definir categoria de items utilizaveis
3. definir achievements
4. definir items

Jorge:
- continuidade na lore
- primeiro dia feito com sucesso
- duas ramificações criadas ainda não testadas
 * numa delas vc chegou cedo e conseguiu ver aula da cálculo
 * na outra o usuario se perdeu e perdeu a aula de cálculo
  

# 31/05

Angel:
- deletei a tabela de achievements pois não havia necessidade, tudo vai permancer em items e agora com um campo de type poderá ser definido o tipo de objeto.
- função insert_in_tables para separar lógica de criação de tabelas da inserção


# horas_trabalhadas: 
48 horas