# Metodos de ordenacion
import random

# Burbuja
def burbuja(vector):
    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[i] < vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    return vector

n = 10
vec = [random.randint(0,100) for i in range(n)]
print(vec)
burbuja(vec)
print("\n")
print(vec)

