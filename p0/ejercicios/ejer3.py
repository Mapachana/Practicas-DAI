# Criba de erastotenes
import random
import math

n = random.randint(1, 100)
print(n)
print("\n")

long = int(math.sqrt(n))+1

vec = [False for i in range(0, n)]

for i in range(2, long):
    for j in range(i, int(n/i)+1):
        if (i*j) < n:
            vec[i*j] = True

for i in range(2, n):
    if not vec[i]:
        print(i, end=' ') 
print("\n")



