## O operador in é utilizado para pesquisar palavras  e o not in é o inverso do in
frase = "Esta é a frase que queremos achar uma palavra"
print(frase)

if "palavra" in frase:
    print("Encontramos a palavra frase")

if "domingo" not in frase:
    print("Não encontramos a palavra domingo")
