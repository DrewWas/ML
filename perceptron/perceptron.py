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

RED_DATA = []
BLUE_DATA = []

def main():
    run = True
    data_type_selected = BLACK 

    while run:
        for event in pygame.event.get():

            WINDOW.fill(BLACK)

            # Weird math so that the origin is technically at the center
            real_pos = pygame.mouse.get_pos()
            x_pos = pygame.mouse.get_pos()[0] - (WIDTH // 2) 
            y_pos = (HEIGHT // 2) - pygame.mouse.get_pos()[1] 

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if real_pos[0] > 20 and real_pos[0] < 190 and real_pos[1] > 15 and real_pos[1] < 50:   
                    data_type_selected = BLUE 

                if real_pos[0] > 20 and real_pos[0] < 190 and real_pos[1] > 55 and real_pos[1] < 90:   
                    data_type_selected = RED 

                if real_pos[0] > 20 and real_pos[0] < 190 and real_pos[1] > 95 and real_pos[1] < 130:   
                    data_type_selected = BLACK 

                elif data_type_selected == RED and (real_pos[0] > 200 or real_pos[1] > 140):
                    RED_DATA.append((x_pos, y_pos))
                    print("RED DATA: ", RED_DATA)

                elif data_type_selected == BLUE and (real_pos[0] > 200 or real_pos[1] > 140):
                    BLUE_DATA.append((x_pos, y_pos))
                    print("BLUE DATA: ", BLUE_DATA)



            # Unfortunately we have to redraw because otherwise the mouse would just paint over the entire screen
            for point in RED_DATA:
                pygame.draw.circle(WINDOW, RED, (point[0] + (WIDTH // 2), -point[1] + (HEIGHT // 2)), 10) 

            for point in BLUE_DATA:
                pygame.draw.circle(WINDOW, BLUE, (point[0] + (WIDTH // 2), -point[1] + (HEIGHT // 2)), 10) 


            pygame.draw.circle(WINDOW, data_type_selected, (x_pos + (WIDTH // 2), -y_pos + (HEIGHT // 2)), 10) 
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


