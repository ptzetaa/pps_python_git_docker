# bayeta.py

from moodle import instanciar, consultar

def frotar(n_frases: int = 1):
    # Aquí puedes llamar a la función de consulta
    # Asegúrate de tener la instancia del cliente de MongoDB
    cliente = instanciar()
    frases = consultar(cliente, n_frases)
    cliente.close()
    return frases
