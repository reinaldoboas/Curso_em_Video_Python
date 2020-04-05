### Curso em Vídeo - Exercicio: desafio052.py
### Link: https://www.youtube.com/watch?v=Er5Hyd4LyVw
### Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. (Divisivel por 1 e por ele mesmo.)

num = int(input("Digite um número para descobrir se ele é um número primo: "))
contador = 0
total = 0

for c in range(1, num +1, 1):
    contador += 1
    if num % c == 0:
        total += 1
        print("\033[32m", end="")
    else:
        print("\033[33m", end="")
    print(c, end=" ")

print("\033[m")
print(f"\nO número {num} foi divisível {total} vezes.")

if total == 2:
    print(f"O número {num} É PRIMO!")
else:
    print(f"O número {num} NÃO É PRIMO!")
