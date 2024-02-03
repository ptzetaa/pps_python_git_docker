# bayeta.py
from moodle import instanciacion, consulta, insercion

def frotar(n_frases: int = 1) -> list:
    cliente, frases_auspiciosas = instanciacion()
    resultado = consulta(cliente, frases_auspiciosas, n_frases)
    return resultado

def agregar_frase_auspiciosa(nueva_frase):
    cliente, frases_auspiciosas = instanciacion()
    insercion(frases_auspiciosas, nueva_frase)
    cliente.close()
