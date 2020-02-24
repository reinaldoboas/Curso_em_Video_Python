### Curso em Vídeo - Exercicio: desafio040.py
### Link: https://www.youtube.com/watch?v=QuWDyUeoaJs
### Crie um programa que leia duas notas de um aluno e calcule sua média.
### Mostrando uma mensagem no final, de acordo com a média atingida:
### - Média abaixo de 5.0 REPROVADO.
### - Média entre 5.0 e 6.9 RECUPERAÇÃO.
### - Média 7.0 ou superior APROVADO.

n1 = float(input("Digite a nota da primeira prova: "))
n2 = float(input("Digite a nota da segunda prova: "))

media = (n1 + n2) / 2

print(f"A média de {n1} e {n2} é: {media}")

if media < 5.0:
    print("REPROVADO.")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO.")
else:
    print("APROVADO!")
