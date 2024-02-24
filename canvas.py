from settings import *
class Canvas():
    def __init__(self):
        self.canvas = []
        self.clearCanvas()
        self.white = "#ecf0f1"  #0
        self.black = "#2d3436"  #1
        self.gray = "#808e9b"   #2
        self.brown = "#6f4e37"  #3
        self.red = "#e74c3c"    #4
        self.orange = "#e67e22" #5
        self.yellow = "#f1c40f" #6
        self.green = "#2ecc71"  #7
        self.blue = "#3498db"   #8
        self.purple = "#9b59b6" #9


        self.selectedColor = 1
        self.penSize = 0
        self.penDown = False
        self.fillOn = False


        self.colorDict = {0:self.white,1:self.black,2:self.gray,3:self.brown,4:self.red,5:self.orange,6:self.yellow,7:self.green,8:self.blue,9:self.purple}

    def clearCanvas(self):
        canvas = []
        for r in range(100):
            row = []
            for c in range(100):
                row.append(0)
            canvas.append(row)
        self.canvas = canvas

    def drawLine(self):
        if self.penDown and not self.fillOn:
            mos = pygame.mouse.get_pos()
            if MARGINSIZE <= mos[0] < WIDTH - MARGINSIZE and MARGINSIZE <= mos[1] < HEIGHT - BOTTOMBAR - MARGINSIZE:
                r = (mos[1] - MARGINSIZE) // TILESIZE
                c = (mos[0] - MARGINSIZE) // TILESIZE
                self.canvas[r][c] = self.selectedColor
                top,bot = r,r
                right,left = c,c
                for i in range(self.penSize):
                    if r - i >= 0:
                        top = r - i
                    if c - i >= 0:
                        left = c -i
                    if r + i <= 100:
                        bot = r + i
                    if c + i <= 100:
                        right = c + i

                for k in range(bot - top):
                    for j in range(right - left):
                        self.canvas[top + k][left + j] = self.selectedColor


    def fillCursor(self):
        if self.fillOn:
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
        else:
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

    def fill(self,mos):
        if MARGINSIZE <= mos[0] < WIDTH - MARGINSIZE and MARGINSIZE <= mos[1] < HEIGHT - BOTTOMBAR - MARGINSIZE:
            r = (mos[1] - MARGINSIZE) // TILESIZE
            c = (mos[0] - MARGINSIZE) // TILESIZE
            self.penDown = False
            self.fillOn = False

    def displayLines(self):
        for i in range(2):
            pygame.draw.line(screen,self.black,(MARGINSIZE,MARGINSIZE + i * TILESIZE * 100),(WIDTH - MARGINSIZE,MARGINSIZE + i * TILESIZE * 100),TILESIZE // 2)
            pygame.draw.line(screen, self.black, (MARGINSIZE + i * TILESIZE * 100, MARGINSIZE),(MARGINSIZE + i * TILESIZE * 100, HEIGHT - MARGINSIZE - BOTTOMBAR), TILESIZE // 2)

    def displayCanvas(self):
        for r,row in enumerate(self.canvas):
            for c,tile in enumerate(row):
                pygame.draw.rect(screen,self.colorDict.get(tile),pygame.Rect(MARGINSIZE + c * TILESIZE,MARGINSIZE + r * TILESIZE,TILESIZE,TILESIZE))

    def displaySelectColor(self):
        x = MARGINSIZE + (TILESIZE * 10) * (self.selectedColor // 2) + (TILESIZE * 5)
        y = MARGINSIZE + TILESIZE * 100 + (TILESIZE * 10) * (self.selectedColor % 2) + (TILESIZE * 5)

        pygame.draw.circle(screen,"black",(x,y),5)

    def display(self):
        self.displayCanvas()
        self.displayLines()
        self.displaySelectColor()
        self.drawLine()
        self.fillCursor()

canvas = Canvas()

