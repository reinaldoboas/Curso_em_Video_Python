### Curso em Vídeo - Exercicio: desafio043.py
### Link: https://www.youtube.com/watch?v=b7r34za963I
### Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
### - Abaixo de 18.5: Abaixo do peso.
### - Entre 18.5 e 25: Peso ideal.
### - 25 até 30: Sobrepeso.
### - 30 até 40: Obesidade.
### - Acima de 40: Obesidade mórbida. Peso ÷ altura x altura

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

# Calculando o IMC
imc = peso / (altura * altura)

print("=-" * 20)
print(f"Seu IMC é: {imc:.1f}")
print("Você está classificado como: ", end="")

if imc < 18.5:
    print("Abaixo do peso!")
elif 18.5 <= imc < 25:
    print("Peso ideal!")
elif 25 <= imc < 30:
    print("Sobrepeso.")
elif 30 <= imc < 40:
    print("Obesidade.")
elif imc >= 40:
    print("Obesidade mórbida!")
print("=-" * 20)
