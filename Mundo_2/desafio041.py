### Curso em Vídeo - Exercicio: desafio041.py
### Link: https://www.youtube.com/watch?v=ZiC5NgSGJXU
### A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
### - Até 9 anos: MIRIM
### - Até 14 anos: INFANTIL
### - Até 19 anos: JUNIOR
### - Até 20 anos: SENIOR
### - Acima: MASTER

from datetime import date

ano_nasc = int(input("Qual o seu ano de nascimento? "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print(f"Você tem {idade} anos.")

if idade <= 9:
    print("MIRIM.")
elif idade > 9 and idade <= 14:
    print("INFANTIL.")
elif idade > 14 and idade <= 19:
    print("JUNIOR.")
elif idade == 20:
    print("SENIOR.")
else:
    print("MASTER.")
