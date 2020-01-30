### Curso em Vídeo - Exercicio: desafio032.py
### Link: https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=33
### Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# importando a biblioteca para descobrir o ano corrente
from datetime import date

ano = int(input("Digite o ano para saber se ele é Bissexto? Digite 0 para verificar o ano atual: "))

# confere se o número inserido é zero e se sim atribui o ano atual à variavel
if ano == 0:
    ano = date.today().year

# ano bissexto ocorre a cada quatro anos. Exceto anos múltiplos de 100 que não são múltiplos de 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} não é BISSEXTO.")
print("FIM DO PROGRAMA")
