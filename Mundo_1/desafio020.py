### Curso em Vídeo - Exercicio: desafio020.py
### Link: https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=29
### O mesmo professor do desafio quer sortear a ordem de apresentação de trabalhos dos alunos. 
### Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

# Pegando as informações de nome dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Usando o módulo de embaralhamento da lista de alunos
lista = [aluno1, aluno2, aluno3, aluno4]
sequencia = shuffle(lista)

# Exibindo os resultados
print("=-" * 30)
print("\nSegue a lista dos alunos com ordem sorteada:")
print(lista)
print("=-" * 30)
