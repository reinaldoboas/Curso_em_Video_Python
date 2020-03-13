### Curso em Vídeo - Exercicio: desafio046.py
### Link: https://www.youtube.com/watch?v=NR1RKt6NT8s
### Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for contagem in range(10, -1, -1):
    print(contagem)
    sleep(0.5)
print("Acabou!!!")
