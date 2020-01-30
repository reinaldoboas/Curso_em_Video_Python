### Curso em Vídeo - Exercicio: desafio029.py
### Link: https://www.youtube.com/watch?v=hgJ_ETNGSj8&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=30
### Escreva um programa que leia a velocidade de um carro.
### Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
### A multa vai custa R$ 7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade do carro? "))

multa = 7 * (velocidade - 80)

if velocidade > 80:
    print("MULTADO!")
    print(f"Sua multa foi de R$ {multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade.")
print("Fim do programa")
