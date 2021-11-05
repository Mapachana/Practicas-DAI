from pickleshare import *


class Database:
# Creo base de datos vacía
    def __init__(self):
        self.database = PickleShareDB('./database')

    def comprobar_login(self, username, password):
        '''Comprueba si un usuario y contraseña existen en la base de datos y son correctos (devuelve True o False)'''

        if self.database.keys(username):
            if self.database[username]['password'] == password:
                return True
            else:
                return False

    def sign_up(self, username, name, password):
        '''Añade un usuario y contraseña a la base de datos si no existen de antes (devuelve True o False)'''

        if self.database.keys(username):
            return False
        else:
            self.database[username] = {'password': password, 'name': name}

            return True

    def get_user(self, username):
        return self.database[username]

    def actualizar_user(self, username, nombre, password):
        '''Actualiza los datos de un usuario'''
        if self.database.keys(username):
            self.database[username]['name'] = nombre
            self.database[username]['password'] = password

            self.database[username] = self.database[username]

            return self.database[username]
        else:
            return {}




# Añado usuarios de prueba
#database["prueba"] = "prueba_c"