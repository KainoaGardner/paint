from settings import *
class Canvas():
    def __init__(self):
        self.canvas = self.clearCanvas()
        self.white = "#ecf0f1"  #0
        self.black = "#2d3436"  #1
        self.red = "#e74c3c"    #2
        self.orange = "#e67e22" #3
        self.yellow = "#f1c40f" #4
        self.green = "#2ecc71"  #5
        self.blue = "#3498db"   #6
        self.purple = "#9b59b6" #7

        self.selectedColor = 0

        self.colorDict = {0:self.white,1:self.black,2:self.red,3:self.orange,4:self.yellow,5:self.green,6:self.blue,7:self.purple}

    def clearCanvas(self):
        canvas = []
        for r in range(100):
            row = []
            for c in range(100):
                row.append(0)
            canvas.append(row)
        return canvas

    def displayLines(self):
        for i in range(101):
            if i % 100 == 0:
                pygame.draw.line(screen,self.black,(MARGINSIZE,MARGINSIZE + i * TILESIZE),(WIDTH - MARGINSIZE,MARGINSIZE + i * TILESIZE),TILESIZE // 2)
                pygame.draw.line(screen, self.black, (MARGINSIZE + i * TILESIZE, MARGINSIZE),(MARGINSIZE + i * TILESIZE, HEIGHT - MARGINSIZE - BOTTOMBAR), TILESIZE // 2)
            else:
                pygame.draw.line(screen, self.black, (MARGINSIZE, MARGINSIZE + i * TILESIZE),(WIDTH - MARGINSIZE, MARGINSIZE + i * TILESIZE), 1)
                pygame.draw.line(screen, self.black, (MARGINSIZE + i * TILESIZE, MARGINSIZE),(MARGINSIZE + i * TILESIZE, HEIGHT - MARGINSIZE - BOTTOMBAR), 1)


    def displayCanvas(self):
        for r,row in enumerate(self.canvas):
            for c,tile in enumerate(row):
                pygame.draw.rect(screen,self.colorDict.get(tile),pygame.Rect(MARGINSIZE + c * TILESIZE,MARGINSIZE + r * TILESIZE,TILESIZE,TILESIZE))

    def display(self):
        self.displayCanvas()
        self.displayLines()

canvas = Canvas()

