from settings import *
from display import display
from canvas import canvas
from buttons import *
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mos = pygame.mouse.get_pos()
                canvas.penDown = True
                for b, button in enumerate(colorButtonList):
                    if button.getClicked(mos):
                        canvas.selectedColor = b
                for b, button in enumerate(penSizeList):
                    if button.getClicked(mos):
                        canvas.penSize = b * 2

                if clear.getClicked(mos):
                    canvas.clearCanvas()
                if fill.getClicked(mos):
                    canvas.fillOn = not canvas.fillOn
                if canvas.fillOn:
                    canvas.fill(mos)


            if event.type == pygame.MOUSEBUTTONUP:
                canvas.penDown = False





        display()
    pygame.quit()


main()