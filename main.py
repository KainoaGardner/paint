from settings import *
from display import display
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        display()
    pygame.quit()


main()