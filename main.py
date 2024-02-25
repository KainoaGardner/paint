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
                        canvas.penSize = b * 3

                if clear.getClicked(mos):
                    canvas.clearCanvas()
                if fill.getClicked(mos):
                    canvas.fillOn = not canvas.fillOn
                if canvas.fillOn and MARGINSIZE <= mos[0] < WIDTH - MARGINSIZE and MARGINSIZE <= mos[1] < HEIGHT - BOTTOMBAR - MARGINSIZE:
                    canvas.floodFill(((mos[1] - MARGINSIZE) // TILESIZE,(mos[0] - MARGINSIZE) // TILESIZE))
                    canvas.penDown = False
                    canvas.fillOn = False

                if undo.getClicked(mos):
                    canvas.undo()
                if redo.getClicked(mos):
                    canvas.redo()

                if save.getClicked(mos):
                    canvas.saveGrid()
                if load.getClicked(mos):
                    canvas.saveImg()

            if event.type == pygame.MOUSEBUTTONUP:
                if canvas.tempHistory != []:
                    canvas.history.append(canvas.tempHistory.copy())
                    canvas.tempHistory.clear()
                    if len(canvas.redoHistory) > 0:
                        canvas.redoHistory = []
                canvas.penDown = False





        display()
    pygame.quit()


main()