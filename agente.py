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
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO rule (percept,relation,action) VALUES ('1', '==', '2')",
    ('2','==','4'))
cur.execute(
    "SELECT * FROM rule")


for (percept, relation, action) in cur:
    print(f"Percepti: {percept}, relation: {relation}, action: {action}")

def eval_rule(rule, percept):
    if eval(percept + rule['relation'] \
            + rule['percept']):
        return rule['action']
    else:
        return None

def rule_engine(rule_db, percept):
    actions = []
    for rule in rule_db:
        actions.append(eval_rule(rule, percept))
    return actions

def eval_rule1(rule, percept, relation, action):
    if eval(percept + relation \
            +def eval_rule(rule, percept):
    if eval(percept + rule['relation'] \
            + rule['percept']):
        return rule['action']
    else:
        return None rule['percept']):
        return action
    else:
        return None
def rule_engine1(cur, percept):
    actions = []
    cur.execute("SELECT * FROM rule")
    for (percept, relation, action) in cur:
        actions.append(eval_rule(rule, percept, relation))
    return actions

percept = '2'
codigo = input("Digite a opção selecionada")
print(rule_engine(rule_db, percept))

