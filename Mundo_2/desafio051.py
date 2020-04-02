### Curso em Vídeo - Exercicio: desafio051.py
### Link: https://www.youtube.com/watch?v=-OnqSGh0u4g
### Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
### No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Digite o primeiro número: "))
razao = int(input("Qual a razão: "))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{0} '.format(c), end='-> ')
print('ACABOU')
