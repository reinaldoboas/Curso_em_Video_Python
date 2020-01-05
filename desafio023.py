### Curso em Vídeo - Exercicio: desafio023.py
### Link: https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=24
### Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados:
### ex:
### Um número: 1984
### Unidade: 4
### Dezena: 8
### Centena: 9
### Milhar: 1

num = int(input("Digite um número de 0 a 9999: "))

# Fracionando o número recebido dividindo ele por 1, 10, 100 e 1000 e depois pegando o resto da divisão por 10 respectivamente
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print("=-" * 30)
print(f"O número inteiro digitado foi o: {num}")
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
print("=-" * 30)
