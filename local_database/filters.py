operatori = {
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    ">":  lambda a, b: a > b,
    "<":  lambda a, b: a < b,
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    "contains": lambda a, b: b in a,
}

def applica_filtro(record, filtro):
    for campo, (operatore, valore) in filtro.items():
        funzione = operatori[operatore]

        if not funzione(record[campo], valore):
            return False

    return True