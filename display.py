from settings import *
from canvas import canvas
def display():
    screen.fill("#bdc3c7")
    canvas.display()
    pygame.display.update()
    clock.tick(FPS)