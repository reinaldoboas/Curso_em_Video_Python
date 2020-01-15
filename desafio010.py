### Curso em Vídeo - Exercicio: desafio010.py
### Link: https://www.youtube.com/watch?v=xM4AX3Lp2mo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=18
### Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27.

carteira = float(input("Diga quanto você tem na carteira: R$"))
convertido = carteira / 3.27

print(f"Você tem: R$ {carteira:.2f} e pode comprar US$ {convertido:.2f}.")
