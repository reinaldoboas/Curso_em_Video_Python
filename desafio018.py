### Curso em Vídeo - Exercicio: desafio018.py
### Link: https://www.youtube.com/watch?v=9GvsphwW26k&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=27
### Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importando a biblioteca Math
import math

angulo = float(input("Digite o ângulo: "))

# Realizando os calculos usando os módulos da biblioteca
seno = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print(f"O ângulo digitado {angulo} tem os seguintes resultados:\nO Seno: {seno}\nO Cosseno: {cos}\nE a Tangente: {tan}")
