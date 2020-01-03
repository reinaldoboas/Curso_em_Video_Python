### Curso em Vídeo - Exercicio: desafio021.py
### Faça um programa que abra e reproduza o audio de um arquivo MP3

# Importando a biblioteca Pygame
import pygame

# Iniciando a reprodução do audio em MP3
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()
