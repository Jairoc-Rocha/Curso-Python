numero = int(input("Digite o valor do número: "))

if numero > 10:
    print(f"O número digitado: {numero} é maior que 10")
    
    if numero > 20:
        print(f" {numero * 2} ")
    else:
        print(f" {numero * 5} ")
    
else:
    print(f"Para prosseguir o número digitado: {numero} tem que ser maior que 10")