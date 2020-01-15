### Curso em Vídeo - Exercicio: desafio012.py
### Link: https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=20
### Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Inserindo os valores
produto = input("Digite o nome do produto: ")
valor = float(input("Digite o preço do produto: R$ "))

# Calculando o desconto
desc = valor * (5 / 100)
valor_desc = valor - desc

print(f"O produto {produto} que custa R$ {valor}, com um desconto de 5% custará R$ {valor_desc:.2f}.")
