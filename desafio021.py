### Curso em Vídeo - Exercicio: desafio021.py
### Link: https://www.youtube.com/watch?v=9FiEji_fzvk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=30
### Faça um programa que abra e reproduza o audio de um arquivo MP3

# Importando a biblioteca Pygame
import pygame

# Iniciando a reprodução do audio em MP3
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()
