from pickleshare import *

# Creo base de datos vacía
database = PickleShareDB('./database')
database.clear()

def comprobar_login(username, password):
    '''Comprueba si un usuario y contraseña existen en la base de datos y son correctos (devuelve True o False)'''

    if database.keys(username):
        passw_key = username + "_c"

        if database[passw_key] == password:
            return True
        else:
            return False

def sign_up(username, password):
    '''Añade un usuario y contraseña a la base de datos si no existen de antes (devuelve True o False)'''

    if database.keys(username):
        return False
    else:
        passw_key = username + "_c"
        database[username] = username
        database[passw_key] = password

        return True




# Añado usuarios de prueba
database["prueba"] = "prueba"
database["prueba_c"] = "prueba"


# Codigo de comprobacion
if comprobar_login("prueba", "prueba"):
    print("jaja si funciono")
else:
    print("no")

if comprobar_login("prueba", "prueba_contra"):
    print("no funciono")
else:
    print("si funciono")

if comprobar_login("pruebaa", "prueba"):
    print("jaja no funciono")
else:
    print("ole ole")

print("PRUEBA REGISTRO")

sign_up("ana", "ana")

if comprobar_login("ana", "ana"):
    print("jaja si funciono")
else:
    print("no")

if comprobar_login("ana", "prueba_contra"):
    print("no funciono")
else:
    print("si funciono")

if comprobar_login("anaa", "ana"):
    print("jaja no funciono")
else:
    print("ole ole")