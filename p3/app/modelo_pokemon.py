from pickleshare import *

from pymongo import MongoClient


class DBPokemon:
    def __init__(self):
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
        self.coll = self.db.samples_pokemon
    
    def buscar(self, clave=None):
        clave = '.*'+clave+'.*'


        return self.coll.find({"$or": [{'name': { "$regex": clave}}, {'type': { "$regex": clave}}]})

    def add_pokemon(self, nombre, img, type, height, weight, candy, egg):
        nuevo_pokemon = {'name': nombre, 'type': type, 'height': height, 'weight': weight, 'candy': candy, 'egg': egg}
        aux = self.coll.insert_one(nuevo_pokemon)
        
        return aux.inserted_id

    def update_pokemon(self, id, nombre, img, type, height, weight, candy, egg):
        pass

    def delete_pokemon(self, id):
        pass