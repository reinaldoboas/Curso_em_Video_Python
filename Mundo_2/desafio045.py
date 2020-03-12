### Curso em Vídeo - Exercicio: desafio045.py
### Link: https://www.youtube.com/watch?v=tapTa6KVG-A
### Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

jogador = int(input("""É a sua vez de jogar no Jokenpô!!!
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Escolha uma opção: """))

# Pseudo randomizando a esolha do computador.
pc = randint(1, 3)

print("JOOOO")
sleep(1)
print("KEEN")
sleep(1)
print("PÔ!!!")
print("=-" * 20)

if jogador == 1 and pc == 3:
    print("Você escolheu Pedra")
    print("O Computador escolheu Tesoura")
    print("Você Venceu!")
elif jogador == 2 and pc == 1:
    print("Você escolheu Papel")
    print("O Computador escolheu Pedra")
    print("Você Venceu!")
elif jogador == 3 and pc == 2:
    print("Você escolheu Tesoura")
    print("O Computador escolheu Papel")
    print("Você Venceu!")
elif pc == 1 and jogador == 3:
    print("Você escolheu Tesoura")
    print("O Computador escolheu Pedra")
    print("Você Perdeu...")
elif pc == 2 and jogador == 1:
    print("Você escolheu Pedra")
    print("O Computador escolheu Papel")
    print("Você Perdeu...")
elif pc == 3 and jogador == 2:
    print("Você escolheu Papel")
    print("O Computador escolheu Tesoura")
    print("Você Perdeu...")
elif jogador == pc:
    print("Empate!")
else:
    print("Opção inválida. Tente novamente...")
print("=-" * 20)
