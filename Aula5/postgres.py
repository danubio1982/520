#!/usr/bin/python3

import psycopg2

con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')

cur = con.cursor()
try:
    cur.execute("INSERT into scripts(nome, conteudo) values ('Josivaldo','programador')")
    con.commit()
except Exception as e:
    con.rolback()
    print(e)
finally:
    cur.close()
    con.close()
