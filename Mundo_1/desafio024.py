### Curso em Vídeo - Exercicio: desafio024.py
### Link: https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=34
### - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# Recebendo a entrada do usuário com o nome da cidade e modificando todos os caracteres para minusculo e removendo os espaços antes e depois
cidade = str(input("Digite o nome da cidade: ")).lower().strip()

print(f"O nome da cidade digitado é: {cidade}")
print(f"A cidade começa com o nome de Santo?", (cidade[:5] == "santo")) # realizando o teste de verdadeiro ou false comparando os 5 primeiros caracteres com a string "santo"
