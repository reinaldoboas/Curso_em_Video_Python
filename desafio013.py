### Curso em Vídeo - Exercicio: desafio013.py
### Link: https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=21
### Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o seu salário atual: R$ "))

aum = salario * (15 / 100)
salario_novo = salario + aum

print(f"O seu salário que era de R$ {salario:.2f}. Agora passará a ser R$ {salario_novo:.2f}.")
