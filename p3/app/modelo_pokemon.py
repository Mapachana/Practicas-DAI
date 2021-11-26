from pickleshare import *

from pymongo import MongoClient
from bson.json_util import dumps

class DBPokemon:
    def __init__(self):
        '''Constructor de la base de datos'''
        client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
        self.db = client.SampleCollections        # Elegimos la base de datos de ejemplo
        self.coll = self.db.samples_pokemon
    
    def buscar(self, clave=None):
        '''Metodo para buscar pokemons que contengan la clave en el nombre o tipo'''
        clave = '.*'+clave+'.*'


        return self.coll.find({"$or": [{'name': { "$regex": clave}}, {'type': { "$regex": clave}}]})

    def add_pokemon(self, nombre, img, type, height, weight, candy, egg):
        '''Metodo para añadir un pokemon a la base de datos'''
        nuevo_pokemon = {'id': self.obtener_id(), 'name': nombre, 'img': img, 'type': type, 'height': height, 'weight': weight, 'candy': candy, 'egg': egg}
        aux = self.coll.insert_one(nuevo_pokemon)
        
        return aux.inserted_id

    def modify_pokemon(self, id, nombre, img, type, height, weight, candy, egg):
        '''Metodo para modificar los datos del pokemon con id id'''
        filter = {'id': int(id) }
        nuevo_pokemon = {"$set": {'name': nombre, 'img': img, 'type': type, 'height': height, 'weight': weight, 'candy': candy, 'egg': egg} }
        res = self.coll.update_one(filter, nuevo_pokemon)
        
        if res.modified_count > 0:
            return True
        else:
            return False

    def delete_pokemon(self, id):
        '''Metodo para borrar el pokemon con id id de la base de datos'''
        
        res = self.coll.delete_one({ 'id': int(id) })
        
        if res.deleted_count > 0:
            return True
        else:
            return False

    def get_pokemon(self, id):
        '''Metodo para obtener la informacion del pokemon con id id'''
        poke = self.coll.find({'id':int(id)})
        res = []
        for pok in poke:
            res.append(pok)
        if len(res) > 0:
            return res[0]
        else:
            return None

    def obtener_id(self):
        '''Metodo auxiliar para calcular el siguiente id disponible en la base de datos'''
        id = 0
        for pokemon in self.coll.find():
            if 'id' in pokemon:
                if pokemon['id'] > id:
                    id = pokemon['id']

        id += 1
        return id