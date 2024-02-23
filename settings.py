import pygame

pygame.init()
TILESIZE = 8
MARGINSIZE = TILESIZE * 3
BOTTOMBAR = TILESIZE * 20
WIDTH = TILESIZE * 100 + MARGINSIZE * 2
HEIGHT = TILESIZE * 100 + MARGINSIZE * 2 + BOTTOMBAR
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# font = pygame.font.Font("font/")

WHITE = "#ecf0f1"