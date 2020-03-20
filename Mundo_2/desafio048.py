### Curso em Vídeo - Exercicio: desafio048.py
### Link: https://www.youtube.com/watch?v=iHjsUxNA-wo
### Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no íntervalo de 1 até 500.

# Setando as variaveis para realizar os calculos da soma e quantidade de interações
soma = 0
contador = 0

# Uso do laço de repetição de 1 a 500 com salto de dois, e testando se o número é ímpar e fazendo os calculos
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        contador += 1

print(f"A soma de todos os números ímpares deu: {soma}", end=" ")
print(f"\nForam {contador} contagens.")
