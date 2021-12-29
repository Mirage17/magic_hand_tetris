import pygame
import random
import sys
from pygame import display

ancho=600
alto=900

window=pygame.display.set_mode((ancho,alto))
game_over=False

while not game_over:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            sys.exit()