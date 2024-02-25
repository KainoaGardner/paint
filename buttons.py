from settings import *

class Buttons():
    def __init__(self,text,textSize,x,y,width,height,color):
        self.surface = pygame.Surface((width,height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(topleft = (x,y))

        self.font = pygame.font.Font("font/LEMONMILK-Regular.otf", textSize)
        self.text = self.font.render(text,True,BLACK)
        self.textRect = self.text.get_rect(center = (x + width // 2,y + height // 2))

    def display(self):
        screen.blit(self.surface,self.rect)
        screen.blit(self.text,self.textRect)
        self.border()

    def border(self):
        for i in range(2):
            pygame.draw.line(screen,"black",(self.rect.x + i * self.rect.width,self.rect.y),(self.rect.x + i * self.rect.width,self.rect.y + self.rect.height),5)
            pygame.draw.line(screen, "black", (self.rect.x, self.rect.y + i * self.rect.height),(self.rect.x + self.rect.width, self.rect.y + i * self.rect.height), 5)

    def getClicked(self,pos):
        if self.rect.x <= pos[0] < self.rect.x + self.rect.width and self.rect.y <= pos[1] < self.rect.y + self.rect.height:
            return True
        return False


whiteButton = Buttons("",0,MARGINSIZE,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 10,"#ecf0f1")
blackButton = Buttons("",0,MARGINSIZE,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 10,"#2d3436")
redButton = Buttons("",0,MARGINSIZE + TILESIZE * 20,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 10,"#e74c3c")
orangeButton = Buttons("",0,MARGINSIZE + TILESIZE * 20,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 10,"#e67e22")
yellowButton = Buttons("",0,MARGINSIZE + TILESIZE * 30,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 10,"#f1c40f")
greenButton = Buttons("",0,MARGINSIZE + TILESIZE * 30,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 10,"#2ecc71")
blueButton = Buttons("",0,MARGINSIZE + TILESIZE * 40,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 10,"#3498db")
purpleButton = Buttons("",0,MARGINSIZE + TILESIZE * 40,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 10,"#9b59b6")
grayButton = Buttons("",0,MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 10,"#808e9b")
brownButton = Buttons("",0,MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 10,"#6f4e37")

smallButton = Buttons("1",30,MARGINSIZE + TILESIZE * 50,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 5,WHITE)
midButton = Buttons("2",30,MARGINSIZE + TILESIZE * 50,MARGINSIZE + TILESIZE * 105,TILESIZE *10,TILESIZE * 5,WHITE)
bigmidButton = Buttons("3",30,MARGINSIZE + TILESIZE * 50,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 5,WHITE)
bigButton = Buttons("4",30,MARGINSIZE + TILESIZE * 50,MARGINSIZE + TILESIZE * 115,TILESIZE *10,TILESIZE * 5,WHITE)

fill = Buttons("fill",20,MARGINSIZE + TILESIZE * 60,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 10,WHITE)
clear = Buttons("clear",20,MARGINSIZE + TILESIZE * 60,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 10,WHITE)

undo = Buttons("undo",20,MARGINSIZE + TILESIZE * 70,MARGINSIZE + TILESIZE * 100,TILESIZE *10,TILESIZE * 10,WHITE)
redo = Buttons("redo",20,MARGINSIZE + TILESIZE * 70,MARGINSIZE + TILESIZE * 110,TILESIZE *10,TILESIZE * 10,WHITE)

save = Buttons("save",30,MARGINSIZE + TILESIZE * 80,MARGINSIZE + TILESIZE * 100,TILESIZE *20,TILESIZE * 10,WHITE)
load = Buttons("load",30,MARGINSIZE + TILESIZE * 80,MARGINSIZE + TILESIZE * 110,TILESIZE *20,TILESIZE * 10,WHITE)


colorButtonList = [whiteButton,blackButton,grayButton,brownButton,redButton,orangeButton,yellowButton,greenButton,blueButton,purpleButton]
penSizeList = [smallButton,midButton,bigmidButton,bigButton]

buttonList = [fill,clear,undo,redo,save,load]

for button in penSizeList:
    buttonList.append(button)
for button in colorButtonList:
    buttonList.append(button)