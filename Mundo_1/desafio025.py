### Curso em Vídeo - Exercicio: desafio025.py
### Link: https://www.youtube.com/watch?v=WHWGz2Dy1ZU&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=35
### Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA no nome"

nome = str(input("Digite o seu nome completo: ")).strip().upper()

print(f"Olá, {nome}!")
print(f"Você tem Silva no nome?", "SILVA" in nome)
