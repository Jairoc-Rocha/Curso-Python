## O método startswith verifica se uma string começa com uma determinada palavra
frase = "Testando o começo e o fim da string"

print(frase.startswith("Testando"))
print(frase.startswith("string"))

if frase.startswith("Testando") == True:
    print("Encontramos a palavra!")