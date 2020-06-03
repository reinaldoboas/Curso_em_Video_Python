### Curso em Vídeo - Exercicio: desafio054.py
### Link: https://www.youtube.com/watch?v=IL5iBWoKRIs
### Crie um programa que leia o ano de nascimento de sete pessoas.
### No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0

for c in range(0, 7):
    ano_nasc=int(input("Digite o ano de nascimento da pessoa:"))
    idade = ano_atual - ano_nasc
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print(f"No final das contas temos {menores} menores de 18 anos e {maiores} maiores.")
