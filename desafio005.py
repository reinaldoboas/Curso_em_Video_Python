### Curso em Vídeo - Exercicio: desafio005.py
### Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor

# lendo a entrada de dados do teclado e realizando os calculos
num = int(input("Digite um número Inteiro: "))
num_antecessor = num - 1
num_sucessor = num + 1

# printando os resultados na tela
print(f"O número digitado foi {num}")
print(f"O seu antecessor é: {num_antecessor}")
print(f"E o número próximo número é o: {num_sucessor}")
