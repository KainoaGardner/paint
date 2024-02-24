from settings import *
from canvas import canvas
from buttons import *
def display():
    screen.fill("#bdc3c7")

    for button in buttonList:
        button.display()
    canvas.display()
    pygame.display.update()
    clock.tick(FPS)