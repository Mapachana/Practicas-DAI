from pickleshare import *

from pymongo import MongoClient
from bson.json_util import dumps

class DBPokemon:
    def __init__(self):
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
        self.coll = self.db.samples_pokemon
    
    def buscar(self, clave=None):
        clave = '.*'+clave+'.*'


        return self.coll.find({"$or": [{'name': { "$regex": clave}}, {'type': { "$regex": clave}}]})

    def add_pokemon(self, nombre, img, type, height, weight, candy, egg):
        nuevo_pokemon = {'id': self.obtener_id(), 'name': nombre, 'type': type, 'height': height, 'weight': weight, 'candy': candy, 'egg': egg}
        aux = self.coll.insert_one(nuevo_pokemon)
        
        return aux.inserted_id

    def modify_pokemon(self, id, nombre, img, type, height, weight, candy, egg):
        filter = {'id': int(id) }
        nuevo_pokemon = {"$set": {'name': nombre, 'type': type, 'height': height, 'weight': weight, 'candy': candy, 'egg': egg} }
        res = self.coll.update_one(filter, nuevo_pokemon)
        
        if res.modified_count > 0:
            return True
        else:
            return False

    def delete_pokemon(self, id):
        
        res = self.coll.delete_one({ 'id': int(id) })
        
        if res.deleted_count > 0:
            return True
        else:
            return False

    def get_pokemon(self, id):
        poke = self.coll.find({'id':int(id)})
        res = []
        for pok in poke:
            res.append(pok)
        if len(res) > 0:
            return res[0]
        else:
            return None

    def obtener_id(self):
        id = 0
        for pokemon in self.coll.find():
            if 'id' in pokemon:
                if pokemon['id'] > id:
                    id = pokemon['id']

        id += 1
        return id