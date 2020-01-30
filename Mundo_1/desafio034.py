### Curso em Vídeo - Exercicio: desafio034.py
### Link: https://www.youtube.com/watch?v=Sfadj_AzKHw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=35
### Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
### Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
### Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o seu salário atual: "))

if salario > 1250:
    porcentagem = "10%"
    aumento = (10 / 100) * salario
    salario_novo = salario + aumento
else:
    porcentagem = "15%"
    aumento = (15 / 100) * salario
    salario_novo = salario + aumento
print(f"O seu salário que era R$ {salario:.2f} com aumento de {porcentagem} de R$ {aumento:.2f} foi para R$ {salario_novo}")
