### Curso em Vídeo - Exercicio: desafio049.py
### Link: https://www.youtube.com/watch?v=QtElJDa9ICM
### Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Digite um número para descobrir a sua tabuada: "))
contador = 1

for c in range(1, 11, 1):
    print(f"{num} x {contador} = {num * contador}")
    contador += 1
