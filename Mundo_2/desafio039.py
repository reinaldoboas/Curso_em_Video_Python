### Curso em Vídeo - Exercicio: desafio039.py
### Link: https://www.youtube.com/watch?v=ePwP4gU_waY
### Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
### - Se é a hora de se alistar.
### - Se já passou do tempo do alistamento.
### Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#importando a biblioteca para pegar o ano atual
from datetime import date

ano_nasc = int(input("Qual o seu ano de nascimento? "))

#realizando os calculos com as datas
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade == 18:
    print("Você tem 18 anos. Está na hora de se alistar!")
elif idade > 18:
    print(f"Você tem {idade} anos. Já passou o tempo de se alistar.")
    print(f"Você precisava ter se alistado no ano de {ano_nasc + 18}.")
else:
    print(f"Você ainda não tem 18 anos! Você está com {idade} anos e faltam {18 - idade} anos para se alistar no ano de {ano_nasc + 18}.")
