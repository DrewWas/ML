import pygame
from random import randint

(WID, HEIGHT) = (900, 800)
WIN = pygame.display.set_mode((WID, HEIGHT))
pygame.display.set_caption("flap bird fr")
pygame.display.flip()

 # CONSTANTS
blue = (0,138, 255)
black = (0,0,0)
#height = randint(-200,350)


def bird(bird_y):
    pygame.draw.rect(WIN, (200,100,100), (200, bird_y, 35,35))


def bricks(x_pos, y_pos):
    
    #blocks = [pygame.draw.rect(WIN, blue, (x_pos + (i * 200), y_pos, 100, 100)) for i in range(10)]
    pygame.draw.rect(WIN, blue, (x_pos,y_pos,100,100))
    



def main():
    run = True
    brick_x = 400
    brick_y = 400

    bird_y = 200


    while run:
        pygame.display.update()
        WIN.fill(black)
        pygame.time.Clock().tick(60)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and bird_y > 10:
                bird_y -= 8
        if keys[pygame.K_DOWN] and bird_y < 760 :
            bird_y += 8

        bricks(brick_x, brick_y)
        bird(bird_y)
        #brick_x -= 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            


main()



"""
TO DO 
* Why is the block so laggy moving across the screen?? (CHECK)

* Make blocks move across screen in a good way 

* Still a little bit laggy 

* make bird 

* scoring system

* if bird hit block it die

* EXTREMELEY BASIC 


"""