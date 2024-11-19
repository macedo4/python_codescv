import pygame
import time

pygame.init()
pygame.mixer.music.load('musiquinha.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():  # Espera até a música terminar
    time.sleep(1)  # Faz uma pequena pausa enquanto a música toca
