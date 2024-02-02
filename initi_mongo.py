# init_mongo.py

from pymongo import MongoClient
from moodle import datos

def inicializar_mongo():
    # Conexión con el motor de Mongo
    cliente_mongo = MongoClient('mongodb://mongo:27017/')
    
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la tabla (llamada colección en Mongo)
    frases_auspiciosas = bd['frases_auspiciosas']
    
    # Comprobamos que no se haya inicializado previamente
    if frases_auspiciosas.count_documents({}) == 0:
        # Inserción de datos
        frases_auspiciosas.insert_many(datos)
        print("Datos inicializados correctamente.")
    
    # Cerrar cliente
    cliente_mongo.close()

if __name__ == "__main__":
    inicializar_mongo()
