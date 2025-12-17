# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame
import time

print("Musiquinha para alegrar")
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)
