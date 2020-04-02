### Curso em Vídeo - Exercicio: desafio050.py
### Link: https://www.youtube.com/watch?v=rJaBLOW57Jg
### Desenvolva um programa que leia seis número inteiros e mostre a soma apenas daqueles que forem pares.
### Se o valor digitador for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range(0, 6, 1):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você digitou {cont} números pares. A soma dos pares deu: {soma}.")
