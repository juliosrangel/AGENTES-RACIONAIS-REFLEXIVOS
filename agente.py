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
    if eval(entrada + relation \
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
rule  = {'percept':'1',
         'relation':'==',
         'action': 1}

print(rule_engine1(cur, entrada))
