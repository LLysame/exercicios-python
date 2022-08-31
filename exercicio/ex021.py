# faça um programa em python que abra e
# reproduza o audio de um arquivo mp3

import pygame
pygame.mixer.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
while True:
    print('precione "p" para pausar, "r" para reproduzir')
    print('precione "e" para sair do programa')
    query = input('')

    if query == "p":
        pygame.mixer.music.pause()
    elif query == "r":
        pygame.mixer.music.unpause()
    elif query == "e":
        pygame.mixer.music.stop()
        break
