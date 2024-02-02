# init_mongo.py

from pymongo import MongoClient
from moodle import datos, inicializar

def inicializar_mongo():
    # Conexión con el motor de Mongo
    cliente_mongo = MongoClient('mongodb://mongo:27017/')
    
    # Llamar a la función de inicialización
    inicializar(cliente_mongo, datos)
    
    # Cerrar cliente
    cliente_mongo.close()

if __name__ == "__main__":
    inicializar_mongo()
