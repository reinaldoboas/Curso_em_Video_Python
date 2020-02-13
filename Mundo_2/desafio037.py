### Curso em Vídeo - Exercicio: desafio037.py
### Link: https://www.youtube.com/watch?v=B3F0IjH5WAM&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=38
### Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual base será a base de conversão:
### - 1 para binário
### - 2 para octal
### - 3 para hexadecimal

num = int(input("Digite um número inteiro: "))
escolha = (int(input("Escolha qual opção você deseja: \n\t(1) - Converter para binário\n\t(2) - Converter para octal\n\t(3) - Converter para hexadecimal\nQual a sua opção: ")))

if escolha == 1:
    print("Você escolheu a opção 1")
    print(f"O número {num} convertido em bínario: {bin(num)[2:]}")
elif escolha == 2:
    print("Você optou pela opção 2")
    print(f"O número {num} convertido em Octal: {oct(num)[2:]}")
elif escolha == 3:
    print("Você selecionou a opção 3")
    print(f"O número {num} convertido em Hexadecimal: {hex(num)[2:]}")
else:
    print("Opção invalida! Tente novamente.")
