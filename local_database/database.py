import json
from .storage import Storage

class Database:
    def __init__(self):
        self._storage = Storage()

    def scrivi(nomeDatabase: str, nuoviDati: list):
        files = Storage.files(nomeDatabase)
        file_json = files["file_json"]
        file_txt = files["file_txt"]

        f_db = open(file_txt, "a")

        with open(file_json, "r") as f:
            f_json = json.load(f)

            for idx, nuovoDato in enumerate(nuoviDati):
                sizeLimit = f_json[str(idx)]["size"]
                columnName = f_json[str(idx)]["name"]
                spazioExtra = sizeLimit - len(str(nuovoDato))

                if spazioExtra < 0:
                    print("ERRORE!")
                    return f"ERRORE, {nuovoDato} troppo esteso per il limite di {sizeLimit} di {columnName} nel database {nomeDatabase}. nessuna modifica applicata!"

                f_db.write(str(nuovoDato) + " "*spazioExtra)
            f_db.write("\n")

            return f"SUCCESSO, Database scritto con successo!"

    def leggi(nomeDatabase: str, filtro: set, MonoRisultato: bool):
        files = Storage.files(nomeDatabase)
        file_json = files["file_json"]
        file_txt = files["file_txt"]

        with open(file_txt, "r") as f_db:
            result = f_db.read()

        return result