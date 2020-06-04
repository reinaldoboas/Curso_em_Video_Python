### Curso em Vídeo - Exercicio: desafio055.py
### Link: https://www.youtube.com/watch?v=Kjpb_IAOKRQ
### Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

menor = 0
maior = 0

for pessoa in range(0, 5):
    peso = float(input("Digite o peso da pessoa: "))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso: {maior} Kg")
print(f"O menor peso: {menor} Kg")
