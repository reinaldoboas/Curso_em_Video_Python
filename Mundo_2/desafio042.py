### Curso em Vídeo - Exercicio: desafio042.py
### Link:https://www.youtube.com/watch?v=ZX7sCPjcHA0
### Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
### - Equilátero: todas os lados iguais.
### - Isosceles: dois lados iguais.
### - Escaleno: todos os lados diferentes.

r1 = float(input("Digite a primeira reta: "))
r2 = float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas podem formar um triangulo: ", end="")
    if r1 == r2 == r3:
        print("Equilátero!")
    elif r1 != r2 != r3 != r1:
        print("Escaleno!")
    else:
        print("Isósceles!")
else:
    print("As retas não podem formar um triângulo.")
print("Fim")
