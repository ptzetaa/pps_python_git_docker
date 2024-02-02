# moodle.py

from pymongo import MongoClient

datos = [
    {"frase": "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad"},
    {"frase": "La aventura de hoy es la historia de terror del mañana"},
    {"frase": "La felicidad es como un rayo de sol, disfrútala antes de que el cambio climático la arruine"},
    {"frase": "Enfrenta tus miedos, o pídeles alquiler por vivir en tu cabeza"},
    {"frase": "Recuerda, cada pequeño cambio cuenta. Especialmente los errores en tu declaración de la renta"},
    {"frase": "Aprovecha las oportunidades, son como los autobuses, los que no llegan tarde simplemente no pasan"},
    {"frase": "Ser agradecido está bien, pero no paga las facturas"},
    {"frase": "La creatividad es como jugar a la ruleta rusa, nunca sabes cuándo te tocará una 'buena' idea"},
    {"frase": "Ríe y el mundo reirá contigo. Llora, y te darán una cuenta de Twitter"},
    {"frase": "Sigue tu corazón, pero recuerda llevar tu cerebro contigo"}
]

def instanciar():
    return MongoClient('mongodb://mongo:27017/')

def inicializar(cliente, datos):
    bd = cliente['bayeta']
    frases_auspiciosas = bd['frases_auspiciosas']

    # Comprobamos que no se haya inicializado previamente
    if frases_auspiciosas.count_documents({}) == 0:
        # Inserción de datos
        frases_auspiciosas.insert_many(datos)
        print("Datos inicializados correctamente.")

def consultar(cliente, n_frases):
    bd = cliente['bayeta']
    frases_auspiciosas = bd['frases_auspiciosas']
    
    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))
    
    # Retornar las frases
    return [frase['frase'] for frase in frases_aleatorias]
