### Curso em Vídeo - Exercicio: desafio031.py
### Link: https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=32
### Desenvolva um programa que pergunte a distância de uma viagem em km.
### Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

distancia = float(input("Qual a distância da viagem em km: "))

print("=-" * 35)
if distancia <= 200:
    preco = distancia * 0.50
    print(f"A sua viagem de {distancia} Km tem o valor total de R$ {preco:.2f}.")
else:
    preco = distancia * 0.45
    print(f"Sua viagem de {distancia} Km é mais longa e tem o valor de R$ {preco:.2f}.")
print("=-" * 35)
print("FIM DO PROGRAMA")
