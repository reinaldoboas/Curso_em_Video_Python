### Curso em Vídeo - Exercicio: desafio019.py
### Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
### Faça um programam que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

# Recebendo os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Agrupando os alunos em uma lista e utilizando o módulo para randomizar o sorteio do aluno 
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print(f"O aluno escolhido foi: {escolhido}")
