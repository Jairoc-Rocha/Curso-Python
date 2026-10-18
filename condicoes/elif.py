aluno = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 0 and media <= 5:
    print(f"O aluno {aluno} foi reprovado com a média = {media}")
elif media > 5 and media <= 6:
    print(f"O aluno {aluno} ficou de recuperação com a média = {media}")
elif media >= 7 and media <= 10:
    print(f"O aluno {aluno} foi aprovado com a média = {media}")
else:
    print(f"Media inválida {media}")
