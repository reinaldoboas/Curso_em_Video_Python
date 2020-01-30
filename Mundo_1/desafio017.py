### Curso em Vídeo - Exercicio: desafio017.py
### Link: https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=26
### Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
### calcule e mostre o comprimento da hipotenusa.

# Importando o módulo da biblioteca math
from math import hypot

co = float(input("Digite o Cateto Oposto: "))
ca = float(input("Digite o Cateto Adjacente: "))

# Realizando o calculo matematico
hipotenusa = hypot(co, ca)

print(f"O Cateto Oposto {co} e o Cateto Adjacente {ca} têm o comprimento da Hipotenusa: {hipotenusa}.")
