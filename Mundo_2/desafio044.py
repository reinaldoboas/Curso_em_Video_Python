### Curso em Vídeo - Exercicio: desafio044.py
### Link: https://www.youtube.com/watch?v=I-SH3QchuZ4
### Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
### - À vista dinheiro/cheque: 10% de desconto.
### - À vista no cartão: 5% de desconto.
### - Em até 2x no cartão: preço normal.
### - 3x ou mais no cartão: 20% juros.

produto = float(input("Qual o valor do produto: R$ "))

opcao = int(input("""== Forma de pagamento ==
[ 1 ] - À vista
[ 2 ] - À vista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais

Escolha uma opção: """))

print("=-" * 20)
print(f"Você escolheu a opção: {opcao}")

if opcao == 1:
    desc = produto * (10 / 100)
    produto_desc = produto - desc
    print(f"O produto que custava R$ {produto:.2f} com um desconto total de R$ {desc:.2f} de 10% agora custará R$ {produto_desc:.2f}.")
elif opcao == 2:
    desc = produto * (5 / 100)
    produto_desc = produto - desc
    print(f"O produto qur custava R$ {produto:.2f} com um desconto de 5% de R$ {desc:.2f} agora custará R$ {produto_desc:.2f}.")
elif opcao == 3:
    print(f"Pagando em até 2x no cartão o preço do produto é normal: R$ {produto:.2f}.")
elif opcao == 4:
    juros = produto * (30 / 100)
    produto_juros = produto + juros
    print(f"O produto em 3x no cartão de R$ {produto:.2f}. \nCom acréscimo de juros de 30%: R$ {juros:.2f}\nValor final R$ {produto_juros:.2f}.")
else:
    print("Opção inválida. Tente novamente...")
