# bayeta.py

from moodle import instanciar, consultar

def frotar(n_frases: int = 1):
    cliente = instanciar()
    frases = consultar(cliente, n_frases)
    cliente.close()
    return frases
