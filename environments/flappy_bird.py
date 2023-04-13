import pygame
from random import randint

(WID, HEIGHT) = (900, 800)
WIN = pygame.display.set_mode((WID, HEIGHT))
pygame.display.set_caption("flap bird fr")
pygame.display.flip()

 # CONSTANTS
blue = (0,138, 255)
black = (0,0,0)

def bricks(x_pos, y_pos):
    upper = pygame.draw.rect(WIN, blue, (x_pos, y_pos, 100, 100))
    lower = pygame.draw.rect(WIN, blue, (x_pos, (y_pos + 75), 100, 100))



def main():
    run = True
    x = 300
    y = 300

    pygame.time.Clock().tick(60)

    while run:
        for event in pygame.event.get():
            


            bricks(x,y)
            x -= 10
            y -= 10
            pygame.display.update()
            WIN.fill(black)

            if event.type == pygame.QUIT:
                run = False


main()



"""
TO DO 
* Why is the block so laggy moving across the screen??

* Make blocks move across screen in a good way 

* make bird 

* scoring system

* if bird hit block it die

* EXTREMELEY BASIC 



"""