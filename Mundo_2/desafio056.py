### Curso em Vídeo - Exercicio: desafio056.py
### Link: https://www.youtube.com/watch?v=fokDF4th0IY
### Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
### No final do programa, mostre:
### - A média de idade do grupo.
### - Qual é o nome do homem mais velho.
### - Quantas mulheres têm menos de 20 anos.

# setando as variaveis de ambiente
velhinho = ""
idade_velho = 0
idades = 0
media = 0
mulheres_menores = 0

for count in range(1, 5):
    # recebendo a entrada de dados do usuário
    print(f"=-=-=-=-=-= {count}ª Pessoa =-=-=-=-=-=")
    nome = str(input("Digite o nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo M/F: ")).lower().strip()
    idades += idade
    # iniciando as lógicas 
    if sexo == "m":
        if count == 1:
            velhinho = nome
            idade_velho = idade
        elif idade > idade_velho:
            velhinho = nome
            idade_velho = idade
    elif sexo == "f":
        if idade < 20:
            mulheres_menores += 1
    else:
        print("Opção inválida.")

media = idades / 4
print(f"A média de idade é: {media}.")
print(f"O homem mais velho é o {velhinho} com {idade_velho} anos.")
print(f"No total {mulheres_menores} mulheres são menores de 20 anos.")
