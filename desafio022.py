### Curso em Vídeo - Exercicio: desafio022.py
### Crie um programa que leia o nome completo de uma pessoa e mostre:
### - O nome com todas as letras maiusculas.
### - O nome com todas as letras minúsculas.
### - Quantas letras ao todo (sem considerar os espaços).
### - Quantas letras tem o primeiro nome.'''

# Recebendo as variaveis e separando o nome
nome = str(input("Digite o seu nome completo: ")).strip()
primeiro_nome = nome.split()

print("=-" * 30)

# Convertendo a string para maiusculo
print(f"O nome com as letras maisculas: {nome.upper()}")

# Convertendo toda a string para minúscula
print(f"O nome com todas as letras minúsculas: {nome.lower()}")

# Medindo a quantidade de caracteres no nome e subtraindo pelo número de ocorrencias de espaço 
print(f"Quantidade de letras ao todo (sem considerar os espaços): {len(nome) - nome.count(' ')} ")

# Exibindo o primeiro nome já splitado e contando a quantidade de letras nele
print(f"O primeiro nome é: {primeiro_nome[0]}. Quantas letras tem o primeiro nome: {len(primeiro_nome[0])}")

print("=-" * 30)
