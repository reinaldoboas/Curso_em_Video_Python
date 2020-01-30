### Curso em Vídeo - Exercicio: desafio028.py
### Link: https://www.youtube.com/watch?v=kchC5KLZSZ4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=39
### Escreva um programa que faça o pc "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
### descobrir qual foi o número escolhido pelo computador.
### O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
num = int(input("Digite um número de 0 a 5: "))

#usando o módulo para randomizar o número escolhido pelo computador 
num_pc = randint(0, 5)

print('Analisando...')
sleep(3)

print("-=" * 35)
if num == num_pc:
    print(f"Você ACERTOU!!! \nO número é o {num}.")
else:
    print(f"Você errou. \nO número correto era o {num_pc}.")
    if num >= 6:
        print("Você digitou um número maior que 5.")
print("-=" * 35)
