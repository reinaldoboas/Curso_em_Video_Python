### Curso em Vídeo - Exercicio: desafio058.py
### Link: https://www.youtube.com/watch?v=-QkOIHJ1Chw
### Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
### Só que agora o jogador vai tentar adinhar até acertar mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(0, 10)
tentativas = 1
jogador = int(input("Digite um número de 0 a 10: "))

while pc != jogador:
    tentativas += 1
    if jogador > pc:
        print("Aposte menos....")
    elif jogador < pc:
        print("Aposte maior...")
    jogador = int(input("Não foi dessa vez. Tente um número de 0 a 10 novamente: "))
print(f"Computador {pc} o jogador {jogador}. Foram feitas {tentativas} tentativas.")
