import mariadb
import sys

rule_db = [ {'percept':'1',
             'relation':'==',
             'action': 1},
            {'percept': '2',
             'relation': '==',
             'action': 4},
            {'percept': '2',
             'relation': '==',
             'action': 8},
            {'percept': '2',
             'relation': '==',
             'action': 19}]


# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        port=3307,
        database="testejulio"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

def eval_rule1(percept, relation, action, entrada):
    print(entrada)
    teste = str(entrada)
    if eval(teste + relation \
            + percept):
        return action
    else:
        return None
    
def rule_engine1(cur, entrada):
    actions = []
    cur.execute("SELECT * FROM rule where percept =?",(entrada,))
    for (percept, relation, action) in cur:
        actions.append(eval_rule1(percept, relation, action, entrada))
    return actions
escolha = 6
while escolha !=5:
    print('''
Escolha uma opçao:
    1 - comprar
    2 - adiocionar
    3 - pesquisar
    4 - excluir
    5 - sair''')
    escolha = int(input('DIgite a escolha selecionada: '))
    if(escolha==1):
        entrada = input("Digite a sua compra: ")
        print(rule_engine1(cur, entrada))
    if(escolha==2):
        adicionar = input("Digite a sua adiçao: ")
    if(escolha==3):
        buscar = input("Digite a sua busca: ")
    if(escolha==4):
        buscar = input("Digite o que deseja excluir: ")
    if(escolha==5):
        break       
    
