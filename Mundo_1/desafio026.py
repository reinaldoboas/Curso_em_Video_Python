### Curso em Vídeo - Exercicio: desafio026.py
### Link: https://www.youtube.com/watch?v=23UOVEetNPY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=36
### Faça um programa que leia uma frase pelo teclado e mostre:
###    - Quantas vezes aparece a letra "A".
###    - Em que posição ela aparece a primeira vez.
###    - Em que posição ela aparece a última vez.

#recebendo a frase do usuário, removendo os espaços antes e depois e modificando os caracteres para minusculos
frase = str(input("Digite uma frase: ")).strip().lower()

letra_a = frase.count("a") #fazendo a contagem do caracter "a"
primeira_a = frase.find("a") + 1 #buscando a primeira ocorrência e adicionando mais um 1 pois ele conta o primeiro como 0 
ultima_a = frase.rfind("a") + 1 #buscando a última ocorrência e adicionando mais 1

print(f"A letra A aparece {letra_a} vezes na frase.")
print(f"A primeira letra A aparece na posição {primeira_a}.")
print(f"A última letra A aparece na posição {ultima_a}.")
