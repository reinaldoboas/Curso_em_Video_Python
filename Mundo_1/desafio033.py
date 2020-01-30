### Curso em Vídeo - Exercicio: desafio033.py
### Link: https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=34
### Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# recebendo as variáveis
num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Testando qual variável é a menor
menor = num1 # Assumimos que o primeiro número é o menor para evitar a necessidade de mais um if
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Testando qual variável é a maior
maior = num1 # Atribuimos o num1 como maior para evitar a necessidade de um if
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print("=-" * 35)
print(f"O menor número é: {menor}.")
print(f"O maior número é: {maior}.")
