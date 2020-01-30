### Curso em Vídeo - Exercicio: desafio015.py
### Link: https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=23
### Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
### Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

percorrido = int(input("Diga a quantidade de Km percorridos: "))
dias = int(input("Quantos dias o carro foi alugado: "))

pagar = float(60 * dias + (0.15 * percorrido))

print(f"Você alugou o carro por {dias} dias. \nPercorreu {percorrido} Km\nValor a pagar: R$ {pagar:.2f}")
