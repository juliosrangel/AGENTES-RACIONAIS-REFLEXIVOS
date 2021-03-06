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

def busca(cur, entrada):
    inserts = []
    cur.execute("SELECT * FROM rule where percept =?",(entrada,))
    for (percept, relation, action) in cur:
        insert='Percept: '+percept+' Relacao: '+ relation+' Acao: ' +action+' || '
        inserts.append(insert)
    return inserts
        
def insert(cur, compra, relacao, acao):
    cur.execute(
    "INSERT INTO rule (percept,relation,action) VALUES (?, ?, ?)", 
    (compra, relacao, acao))
    
def excluir(cur, exclusao):
    cur.execute(
    "DELETE FROM rule WHERE percept ='?'", (exclusao))
    return 'registro deletado'
    
escolha = 6
while escolha !=5:
    print('''
Escolha uma opçao:
    1 - comprar
    2 - adicionar
    3 - pesquisar
    4 - excluir
    5 - sair''')
    escolha = int(input('Digite a escolha selecionada: '))
    if(escolha==1):
        print('a compra desejada deve ser colocada em parenteses, ex: "meia"')
        entrada = input("Digite a sua compra: ")
        print(rule_engine1(cur, entrada))
    if(escolha==2):
        print('a entrada desejada deve ser colocada em parenteses, ex: "meia"')
        compra = input("Digite o seu produto: ")
        relacao = input("Digite a sua relacao: ")
        acao = input("Digite a sua acao: ")
        print(insert(cur, compra, relacao, acao))
    if(escolha==3):
        print('a entrada desejada deve ser colocada em parenteses, ex: "meia"\n')
        buscar = input("Digite o que deseja pesquisar: ")
        print(busca(cur, buscar))
    if(escolha==4):
        print('a entrada desejada deve ser colocada em parenteses, ex: "meia"\n')
        exclusao = input("Digite o que deseja excluir: ")
        print(excluir(cur, exclusao))
        
        
    if(escolha==5):
        break       
    

