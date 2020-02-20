### Curso em Vídeo - Exercicio: desafio038.py
### Link: https://www.youtube.com/watch?v=iuPbB9uHczM
### Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
### - O primeiro valor é maior.
### - O segundo valor é maior.
### - Não existe valor maior, os dois são iguais.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

print(20 * "=-")
if num1 > num2:
    print(f"O primeiro número digitado {num1} é maior que o segundo {num2}")
elif num2 > num1:
    print(f"O segundo número digitado {num2} é maior que o primeiro {num1}")
else:
    print(f"Os números digitados são iguais: {num2}")
