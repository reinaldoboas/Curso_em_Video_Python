### Curso em Vídeo - Exercicio: desafio035.py
### Link: https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=36
### Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

comp1 = float(input("Digite o primeiro comprimento: "))
comp2 = float(input("Digite o segundo comprimento: "))
comp3 = float(input("Digite o terceiro comprimento: "))

# Para formar um triângulo é necessário que cada um dos comprimentos sejam menores do que a soma dos outros dois.
if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp2 + comp1:
    print("Os segmentos podem formar um triângulo!")
else:
    print("Os segmentos NÂO PODEM formar um triângulo!")
