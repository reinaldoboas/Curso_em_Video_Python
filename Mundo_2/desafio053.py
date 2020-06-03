### Curso em Vídeo - Exercicio: desafio053.py
### Link: https://www.youtube.com/watch?v=5VBWe6BXzRo
### Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Temos um palíndromo!")
    print(f"{junto} = {inverso}")
else:
    print("A frase digitada não é um palíndromo...")
    print(f"{junto} != {inverso}")
