import pygame
import sys

from pygame import display
#constantes basicas

ancho=800
alto=800
color_rojo=(250,0,0)
background_color=(0,0,0)
pos_player=[400,400]
size_player=[50,50]
window=pygame.display.set_mode((800,600))
game_over=False
print('hello')

while not game_over:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x=pos_player[0]
            if event.key==pygame.K_LEFT:
                x-=size_player[0]                
            if event.key==pygame.K_RIGHT:
                x+=size_player[0]
            pos_player[0]=x

    window.fill(background_color)
    #Dibujar jugador
    pygame.draw.rect(window,color_rojo,(pos_player[0],pos_player[1],
                                        size_player[0],size_player[1]))
    pygame.display.update()
