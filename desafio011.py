### Curso em Vídeo - Exercicio: desafio011.py
### Link: https://www.youtube.com/watch?v=mzSJpn9ldt4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=19
### Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
### Sabendo que cada litro de tinta, pinta uma área de 2m².

from time import sleep

# Recebendo os valores das variaveis
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura em metros: "))

area = largura * altura
tinta = area / 2

print("ANALISANDO...")
sleep(3)
print(f"Para pintar uma área de {area} metros é necessário {tinta} litros de tinta.")
