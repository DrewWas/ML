import pygame
import math
import numpy as np
import matplotlib.pyplot as plt

# Setup
pygame.init()
WIDTH, HEIGHT = 1400, 800
FPS = 120
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vanilla NN Visualization")

# Colors
BLACK = (0,0,0)
BLUE = (12,31,255)
GRAY = (123,123,123)
WHITE = (255,255,255)
YELLOW = (255,255,2)
GREEN = (12,255,24)

# Coordinates 
yellow_coords = []
blue_coords = []


def draw():
    
    font = pygame.font.SysFont("Arial", 25, bold=True)

    # Main grid lines
    for i in range(int(WIDTH / 35)):
        pygame.draw.line(SCREEN, GRAY, (i * 40, HEIGHT), (i * 40, 0), 1)

    for j in range(int(WIDTH / 35)):
        pygame.draw.line(SCREEN, GRAY, (0, j * 40), (WIDTH, j * 40), 1)

    # Thick coordinate lines 
    pygame.draw.line(SCREEN, GRAY, (720, HEIGHT), (720, 0), 5)
    pygame.draw.line(SCREEN, GRAY, (0, 403), (WIDTH, 403), 5)

    # Draw buttons
    pygame.draw.rect(SCREEN, WHITE, (1240, 10, 150, 110))
    pygame.draw.rect(SCREEN, BLUE, (1245, 15, 140, 30))
    pygame.draw.rect(SCREEN, YELLOW, (1245, 50, 140, 30))
    pygame.draw.rect(SCREEN, GREEN, (1245, 85, 140, 30))

    # Text
    SCREEN.blit(font.render("Add Blue", False, BLACK), (1260,17)) 
    SCREEN.blit(font.render("Add Yellow", False, BLACK), (1250,52)) 
    SCREEN.blit(font.render("Start NN", False, BLACK), (1260,87)) 

    # Points
    for i in blue_coords:
        pygame.draw.circle(SCREEN, BLUE, i, 8) 

    for j in yellow_coords:
        pygame.draw.circle(SCREEN, YELLOW, j, 8) 


def NN_setup():

    blue_labels = np.zeros(len(blue_coords))
    yellow_labels = np.zeros(len(yellow_coords))

    data = np.array(blue_coords + yellow_coords)
    labels = np.concatenate((blue_labels, yellow_labels))

    # Normalize data
    data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    # Shuffle data
    indices = np.arange(data.shape[0])
    np.random.shuffle(indices)
    data = data[indices]
    labels = labels[indices].reshape(-1, 1)
    print("blue: ", blue_coords)
    print("yellow: ", yellow_coords)

    return data, labels


def train():
    scale = 10 
    offset_x, offset_y = WIDTH // 2, HEIGHT // 2


    # Draw the parabola
    points = []
    for x in range(-offset_x // scale, offset_x // scale):
        y = 10 * math.cos(x)
        screen_x = x * scale + offset_x
        screen_y = offset_y - y * scale
        points.append((screen_x, screen_y))
    
    # Draw lines between points
    for i in range(len(points) - 1):
        pygame.draw.line(SCREEN, GREEN, points[i], points[i + 1], 2)





def main():
    run = True
    clock = pygame.time.Clock()
    selected = False
    selected_color = None
    mouse_in_box = False
    ttp = False
    
    button_areas = [
        (1245, 15, 140, 30, BLUE),
        (1245, 50, 140, 30, YELLOW),
        (1245, 85, 140, 30, GREEN)  
    ]
   

    while run:

        if selected and (selected_color != GREEN):
            pygame.draw.circle(SCREEN, selected_color, mouse_pos, 8) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_in_box = (1245 < mouse_pos[0] < 1385 and 15 < mouse_pos[1] < 115)


            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_in_box:
                    for x, y, w, h, color in button_areas:
                        if x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h:
                            selected = True
                            selected_color = color
                            break
                    
                    if selected_color == GREEN:
                        print("START TRAINING")
                        ttp = True 
                        data, labels = NN_setup()
                        # TESTING HERE

                        # DONE TESTING


                elif selected:
                    if selected_color == YELLOW and (mouse_pos not in yellow_coords):
                        yellow_coords.append(mouse_pos)
                    elif selected_color == BLUE and (mouse_pos not in blue_coords):
                        blue_coords.append(mouse_pos)


        if ttp:
            train()
            #NN_setup()
        
        draw()
        pygame.display.update()
        clock.tick(FPS)
        SCREEN.fill(BLACK)
    
    pygame.quit()


if __name__ == "__main__":
    main()




