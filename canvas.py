from settings import *
from tkinter import filedialog


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
        self.tempHistory = []
        self.redoHistory = []
        self.history = []
        self.mouseHistory = []
        self.count = 0

        self.colorDict = {0:self.white,1:self.black,2:self.gray,3:self.brown,4:self.red,5:self.orange,6:self.yellow,7:self.green,8:self.blue,9:self.purple}

    def clearCanvas(self):
        canvas = []
        for r in range(100):
            row = []
            for c in range(100):
                row.append(0)
            canvas.append(row)
        self.canvas = canvas
        self.history = []
        self.redoHistory = []

    def drawLine(self):
        if self.penDown and not self.fillOn:
            mos = pygame.mouse.get_pos()
            if MARGINSIZE <= mos[0] < WIDTH - MARGINSIZE and MARGINSIZE <= mos[1] < HEIGHT - BOTTOMBAR - MARGINSIZE:
                self.getMouseDiff(mos)
                r = (mos[1] - MARGINSIZE) // TILESIZE
                c = (mos[0] - MARGINSIZE) // TILESIZE
                if self.canvas[r][c] != self.selectedColor:
                    self.tempHistory.append(((r, c), (self.canvas[r][c],self.selectedColor)))
                    self.canvas[r][c] = self.selectedColor

                self.bigBrush(r,c)


    def bigBrush(self,r,c):
        top, bot = r, r
        right, left = c, c
        for i in range(self.penSize):
            if r - i >= 0:
                top = r - i
            if c - i >= 0:
                left = c - i
            if r + i <= 100:
                bot = r + i
            if c + i <= 100:
                right = c + i

        for k in range(bot - top):
            for j in range(right - left):
                if self.canvas[top + k][left + j] != self.selectedColor:
                    self.tempHistory.append(((top + k, left + j), (self.canvas[top + k][left + j], self.selectedColor)))
                    self.canvas[top + k][left + j] = self.selectedColor


    def fillCursor(self):
        if self.fillOn:
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
        else:
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

    def getMouseDiff(self,mos):
        self.count += 1
        if self.count % 60 == 0:
            self.count = 0
        self.mouseHistory.append(mos)
        if len(self.mouseHistory) > 2:
            self.mouseHistory.pop(0)

        if len(self.mouseHistory) == 2:
            if self.mouseHistory[0] != self.mouseHistory[1]:
                self.fillGap()

    def fillGap(self):
        x1 = (self.mouseHistory[0][0] - MARGINSIZE) // TILESIZE
        y1 = (self.mouseHistory[0][1] - MARGINSIZE) // TILESIZE
        x2 = (self.mouseHistory[1][0] - MARGINSIZE) // TILESIZE
        y2 = (self.mouseHistory[1][1] - MARGINSIZE) // TILESIZE
        xDif = x2 - x1
        yDif = y2 - y1

        if abs(xDif) >= abs(yDif):
            big = xDif
            small = yDif
            i = 0
            k = 0
            while abs(i) < abs(big):
                if xDif > 0:
                    i += 1
                else:
                    i -= 1
                if small != 0:
                    if i % abs(big) // abs(small) == 0:
                        if yDif > 0:
                            k += 1
                        else:
                            k -= 1
                if 0 <= y1 + k < 100 and 0 <= x1 + i < 100:
                    if self.canvas[y1 + k][x1 + i] != self.selectedColor:
                        self.tempHistory.append(((y1 + k, x1 + i), (self.canvas[y1 + k][x1 + i], self.selectedColor)))
                        self.canvas[y1 + k][x1 + i] = self.selectedColor
                    self.bigBrush(y1 + k, x1 + i)
        else:
            big = yDif
            small = xDif
            i = 0
            k = 0
            while abs(i) < abs(big):
                if yDif > 0:
                    i += 1
                else:
                    i -= 1
                if small != 0:
                    if i % abs(big) // abs(small) == 0:
                        if xDif > 0:
                            k += 1
                        else:
                            k -= 1
                if 0 <= y1 + i < 100 and 0 <= x1 + k < 100:
                    if self.canvas[y1 + i][x1 + k] != self.selectedColor:
                        self.tempHistory.append(((y1 + i, x1 + k), (self.canvas[y1 + i][x1 + k], self.selectedColor)))
                        self.canvas[y1 + i][x1 + k] = self.selectedColor

                    self.bigBrush(y1 + i, x1 + k)






    def fill(self,pos):
        if pos[0] < 0 or pos[0] >= len(self.canvas) or pos[1] < 0 or pos[1] >= len(self.canvas[0]) or self.canvas[pos[0]][pos[1]] != self.firstColor:
            return
        else:
            self.tempHistory.append(((pos[0],pos[1]), (self.canvas[pos[0]][pos[1]],self.selectedColor)))
            self.canvas[pos[0]][pos[1]] = self.selectedColor
            self.fill((pos[0] + 1,pos[1]))
            self.fill((pos[0] - 1, pos[1]))
            self.fill((pos[0], pos[1] + 1))
            self.fill((pos[0], pos[1] - 1))

    def floodFill(self,pos):
        self.firstColor = self.canvas[pos[0]][pos[1]]
        if self.canvas[pos[0]][pos[1]] != self.firstColor:
            return
        else:
            self.fill((pos[0], pos[1]))

    def undo(self):
        if len(self.history) > 0:
            for place in self.history[-1]:
                self.canvas[place[0][0]][place[0][1]] = place[1][0]
            self.redoHistory.append(self.history[-1])
            self.history.pop(-1)

    def redo(self):
        if len(self.redoHistory) > 0:
            for place in self.redoHistory[-1]:
                self.canvas[place[0][0]][place[0][1]] = place[1][1]
            self.history.append(self.redoHistory[-1])
            self.redoHistory.pop(-1)

    def saveGrid(self):
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text file", ".txt")])
        if file is None:
            return
        filetext = ""
        for r,row in enumerate(self.canvas):
            for pixel in row:
                filetext += str(pixel)
            if r < len(self.canvas) - 1:
                filetext += "\n"

        file.write(filetext)
        file.close()

    def load(self):
        filepath = filedialog.askopenfilename()
        if filepath is None or filepath == '':
            return
        else:
            with open(filepath,"r") as file:
                text = file.readlines()
                for r,line in enumerate(text):
                    newline = line.replace("\n", "")
                    for c,pixel in enumerate(newline):
                        self.canvas[r][c] = int(pixel)
            file.close()

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

        y = MARGINSIZE + TILESIZE * 100 + (TILESIZE * 5) * (self.penSize // 3) + (TILESIZE * 2.5)
        pygame.draw.circle(screen, "black", (MARGINSIZE + TILESIZE * 50 + TILESIZE * 2 , y), 5)
        if self.fillOn:
            pygame.draw.circle(screen, "black", (MARGINSIZE + TILESIZE * 60 + TILESIZE * 5,MARGINSIZE + TILESIZE * 100 +TILESIZE * 2), 5)

    def display(self):
        self.displayCanvas()
        self.displayLines()
        self.displaySelectColor()
        self.drawLine()
        self.fillCursor()

canvas = Canvas()

