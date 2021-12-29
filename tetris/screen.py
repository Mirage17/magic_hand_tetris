import pygame
import random
import sys
from pygame import display
from pygame import surface
ancho=600
alto=900
ancho_juego=ancho-100
alto_juego=ancho-100
background_color=(25,25,25)
sqare_size=10


top_left_x = (ancho- ancho_juego) // 2
top_left_y =alto - alto_juego
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


def makeScreen(surface,grid):
    window=pygame.display.set_mode((ancho,alto))
    game_over=False
    while not game_over:
        surface.fill(background_color)
        pygame.font.init()
        font=pygame.font.SysFont('notosansregular',50)
        label=font.render('Tetris', 1, (255,255,255))
        surface.blit(label,(top_left_x+alto_juego/2-label.get_width()/2,30))
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                pygame.draw.rect(surface,grid[x][y],(top_left_x+y*sqare_size,top_left_y+x*sqare_size))
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                sys.exit()
        pygame.draw.rect(surface,grid[i][j],(top_left_x,top_left_y,ancho_juego,alto_juego))
        pygame.display.update()


def create_grid(ocuppied_space=[]):
    grid=[[background_color for i in range(50) for i in range (80)]]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if (x,y) in ocuppied_space:
                c=ocuppied_space[(y,x)]
                grid[x][y]=c
def select_shape(shapes):
    return random.choise(shapes)
