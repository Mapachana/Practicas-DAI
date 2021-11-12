from pickleshare import *

from pymongo import MongoClient

class DBPokemon:
    def __init__(self):
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
    
    def buscar(self, clave=None):
        return self.db.samples_pokemon.find(clave)