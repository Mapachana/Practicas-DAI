# leer de fichero y obtener numero n-esimo de Fibonacci

def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fichero = open("numero.txt", "r")

n = int(fichero.read())

fichero.close()

salida = open("salida.txt", "w")

salida.write(str(fibonacci(n)))

salida.close()


