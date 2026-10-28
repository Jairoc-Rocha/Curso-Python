lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)

for elemento in lista:
    if elemento == 4:
        del elemento[4]
        
print(elemento)