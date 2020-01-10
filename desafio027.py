### Curso em Vídeo - Exercicio: desafio027.py
### Link: https://www.youtube.com/watch?v=SifYYsXhLM8&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=37
### Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
### e o último nome separadamente.
### ex: Ana Maria de Souza
### Primeiro = Ana
### Último = Souza

nome = str(input("Digite o seu nome completo: ")).strip().split() #usando a função split para separar as palavras

#setando as variaveis e sepando de acordo com o número da palavra
primeiro = nome[0]
ultimo = nome[len(nome) - 1]

print(f"O nome inteiro é: {nome}")
print(f"Primeiro nome: {primeiro}")
print(f"Último nome: {ultimo}")
