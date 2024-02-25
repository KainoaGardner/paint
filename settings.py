import sys

import pygame

pygame.init()
sys.setrecursionlimit(10000)

TILESIZE = 8
MARGINSIZE = TILESIZE * 3
BOTTOMBAR = TILESIZE * 20
WIDTH = TILESIZE * 100 + MARGINSIZE * 2
HEIGHT = TILESIZE * 100 + MARGINSIZE * 2 + BOTTOMBAR
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()



WHITE = "#ecf0f1"
BLACK = "#2d3436"