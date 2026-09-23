import os

class Storage:
    def cartellaDatabase():
        cwd = os.getcwd()
        print(cwd)
        database = f"{cwd}/database"
        print(database)
        return database

    def files(nomeDatabase: str):
        folder_database = Storage.cartellaDatabase()
        file_json = f"{folder_database}/{nomeDatabase}.json"
        file_txt = f"{folder_database}/{nomeDatabase}.txt"

        return {"file_json": file_json, "file_txt": file_txt}