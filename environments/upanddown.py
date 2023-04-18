import pygame
from random import randint

(WID, HEIGHT) = (900, 800)
WIN = pygame.display.set_mode((WID, HEIGHT))
pygame.display.set_caption("flap bird fr")
pygame.display.flip()

# CONSTANTS
blue = (0,138, 255)
black = (0,0,0)
heights = [randint(0,500) for i in range(10)]



def bird(bird_y):
    return pygame.draw.rect(WIN, (200,100,100), (200, bird_y, 35,35))



    


def bricks(x_pos, y_pos):

    y_pos = heights
    
    upper_blocks = [pygame.draw.rect(WIN, blue, (x_pos + (i * 200), 0, 50, y_pos[i])) for i in range(10)]
    lower_blocks = [pygame.draw.rect(WIN, blue, (x_pos + (i * 200), (y_pos[i] + 150), 50, 800)) for i in range(10)]
    return None 



def main():
    run = True
    gameon = False
    brick_x = 400
    brick_y = 400
    reset = False

    bird_y = 200


    while run:
        # Basic shit 
        pygame.time.Clock().tick(60)
        pygame.display.update()
        WIN.fill(black)
        keys = pygame.key.get_pressed()

        # Movement functionality 
        if (keys[pygame.K_UP] or keys[pygame.K_w])and bird_y > 10:
                bird_y -= 8
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and bird_y < 760 :
            bird_y += 8

        #Start game functionality 
        if keys[pygame.K_SPACE]:
            gameon = True
        
        if gameon:
            brick_x -= 5

      
        bricks(brick_x, brick_y)
        bird(bird_y)
        for event in pygame.event.get():
            # Makes sure we can exit 
            if event.type == pygame.QUIT:
                run = False
            #Collision functionality 

            #This will have to change, but same basic idea 
            
            
            


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