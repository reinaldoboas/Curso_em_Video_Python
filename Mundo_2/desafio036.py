### Curso em Vídeo - Exercicio: desafio036.py
### Link: https://www.youtube.com/watch?v=IV13X0QOMU8&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=50
### Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
### O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
### Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Recebendo os valores
valor = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos: "))

# Realizando os cálculos
valor_mensal = float(valor / anos / 12)
trinta_porc = float((30 * salario) / 100)

print("=-=" * 15)
if valor_mensal < trinta_porc:
    print("Empréstimo APROVADO!")
    print(f"30% do salário é R$ {trinta_porc:.2f}")
else:
    print("Empréstimo NEGADO!!!")
    print(f"30% do salário é R$ {trinta_porc:.2f}")
print(f"O valor da mensalidade: R$ {valor_mensal:.2f}")
print("=-=" * 15)
