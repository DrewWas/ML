import pygame
import math

# Constants
WIDTH, HEIGHT = 1000, 1000
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLUE = (0, 138, 255)
RED = (255, 34, 86)
BLACK = (0, 0, 0)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), display=1)
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('futura', 30)
FONT_SMALL = pygame.font.SysFont('futura', 18)
#print(pygame.font.get_fonts())


DATA = []

def main():
    run = True
    data_type_selected = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    
             

            # Weird math so that the origin is technically at the center
            x_pos = pygame.mouse.get_pos()[0] - (WIDTH // 2) 
            y_pos = (HEIGHT // 2) - pygame.mouse.get_pos()[1] 
            draw_grid_lines()
            draw_color_select(x_pos, y_pos)
            pygame.display.update()            
    


    pygame.quit()


def draw_grid_lines():
    for i in range(40):
        for j in range(40):
            pygame.draw.line(WINDOW, GRAY, (i * 25, 0), (i * 25, 1000)) 
            pygame.draw.line(WINDOW, GRAY, (0, i * 25), (1000, i * 25)) 

    pygame.draw.line(WINDOW, GRAY, (WIDTH // 2, 0), (WIDTH // 2, 1000), 5) 
    pygame.draw.line(WINDOW, GRAY, (0, HEIGHT // 2), (1000, HEIGHT // 2), 5) 


def draw_color_select(x_pos, y_pos):
    # SELECTION DISPLAY
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(10, 10, 190, 125))

    pygame.draw.rect(WINDOW, BLUE, pygame.Rect(20, 15, 170, 33))
    WINDOW.blit(FONT.render("Blue Data", False, BLACK), (40, 10))
    pygame.draw.rect(WINDOW, RED, pygame.Rect(20, 55, 170, 33))
    WINDOW.blit(FONT.render("Red Data", False, BLACK), (45, 50))

    pygame.draw.rect(WINDOW, BLACK, pygame.Rect(20, 95, 170, 33), 3)
    WINDOW.blit(FONT.render("RESET", False, BLACK), (60, 92))


    # COORDINATE DISPLAY
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(850, 10, 140, 30))
    WINDOW.blit(FONT_SMALL.render("X: " + str(x_pos) + "    Y: " + str(y_pos), False, BLACK), (853, 15))


main()


"""
TO DO:
* GET MOUSE INPUT

* SELECT/CHANGE COLORS

* ADD COLORS TO GRID

* ADD COLORS TO DATA POINTS

* RUN ACTUAL ALGORITHM

* 
"""


