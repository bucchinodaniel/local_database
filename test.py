import os

nuoviDati = ["ciao1","Ciao2","Ciao5"]

nuovoDato = "Ciao"
spazioExtra = 5
print(nuovoDato + ""*spazioExtra+"????")

with open("database/test.txt", "a") as f_db:
    for nuovoDato in nuoviDati:
        f_db.write(nuovoDato + ""*spazioExtra)
    f_db.write("\n")
