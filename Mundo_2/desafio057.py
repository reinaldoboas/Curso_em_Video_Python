### Curso em Vídeo - Exercicio: desafio057.py
### Link: https://www.youtube.com/watch?v=JGztEBLGj5E
### Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
### Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo M/F: ")).lower().strip()

while sexo != "m" and sexo != "f":
    print("Opção inválida... tente novamente.")
    sexo = str(input("Informe seu sexo M/F: ")).lower().strip()

print(f"Entrada válida sexo: {sexo.upper()}.")
