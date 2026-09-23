from local_database import Database

filtro = {
    "NOME": ("contains", "Dan"),
    "ID": (">", 10)
}

db = Database()
risultato = Database.leggi("test", filtro, False)
print(risultato)