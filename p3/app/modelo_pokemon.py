from pickleshare import *

from pymongo import MongoClient

class DBPokemon:
    def __init__(self):
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
        self.coll = self.db.samples_pokemon
    
    def buscar(self, clave=None):
        return self.coll.find({'name': clave})

    def add_pokemon(self, nombre, img, type, height, weight, candy, egg):
        pass