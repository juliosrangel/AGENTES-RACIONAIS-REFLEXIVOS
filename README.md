# AGENTES-RACIONAIS-REFLEXIVOS

Julio Rangel

Modelo de banco:

CREATE DATABASE testejulio;

create table rule(
    percept varchar(255) not null,
    relation varchar(255) not null,
    action varchar(255) not null
);

INSERT INTO rule (percept,relation,action) VALUES ('"tenis"', '==', 'meia');
INSERT INTO rule (percept,relation,action) VALUES ('"tenis, meia"', '==', 'shorts');
INSERT INTO rule (percept,relation,action) VALUES ('"shorts"', '==', 'meia');
INSERT INTO rule (percept,relation,action) VALUES ('"tenis", shorts', '==', 'meia');
INSERT INTO rule (percept,relation,action) VALUES ('"meia"', '==', 'shorts');
INSERT INTO rule (percept,relation,action) VALUES ('"meia", shorts', '==', 'tenis');
