import pygame
from random import uniform

import numpy as np   # Delete
import matplotlib.pyplot as plt  # Delete

# Setup
pygame.init()
WIDTH, HEIGHT = 1400, 800
FPS = 120
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perceptron Visualization")

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


# -----------------------------------------------------------------

def matrix_ify():

    # 1 represents blue
    # 0 represents yellow

    data = []

    for i in blue_coords:
        data.append([1, i[0], i[1], 1])

    for j in yellow_coords:
        data.append([1, j[0], j[1], 0])

    return data


# -----------------------------------------------------------------

def predict(inputs, weights):
    total_activation = 0.0
    threshold = 0.0

    for inputt, weight in zip(inputs, weights):
        total_activation += inputt * weight
    
    if total_activation >= threshold:
        return 1.0
    else:
        return 0.0


def accuracy(matrix, weights):
    num_correct = 0.0
    predictions = []
    
    for i in range(len(matrix)):
        pred = predict(matrix[i][:-1], weights)
        predictions.append(pred)

        if pred == matrix[i][-1]:
            num_correct += 1

    print("Predictions: ", predictions)

    return num_correct / float(len(matrix))
   

def train_weights(matrix, weights, epochs=100, learning_rate=2.0):

    for epoch in range(epochs):
        curr_acc = accuracy(matrix, weights)
        print("\nEpoch %d \nWeights: " %epoch, weights)
        print("Accuracy: ", curr_acc)

        if curr_acc == 1.0:  # and something else??
            break

        # plot (pygame draw) here???

        for i in range(len(matrix)):
            prediction = predict(matrix[i][:-1], weights)
            error = matrix[i][-1] - prediction

            for j in range(len(weights)):
                weights[j] += (learning_rate * error * matrix[i][j])

    return weights
        


def perception():
    
    # 1 represents blue
    # 0 represents yellow

    data = matrix_ify()

    weights = [0.5, 0.3, 0.9]

    new_weights = train_weights(data, weights)  

    print("\nNew Weights: ", new_weights)

    m = -new_weights[1] / new_weights[2]
    b = -new_weights[0] / new_weights[2]

    start_point = (0, int(b))
    end_point = (WIDTH, int((m * WIDTH) + b))

    pygame.draw.line(SCREEN, GREEN, start_point, end_point, 2)


# -----------------------------------------------------------------

def main():
    run = True
    clock = pygame.time.Clock()
    selected = False
    selected_color = None
    mouse_in_box = False
    
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
                        print("START THE PERCEPTRON")
                        perception()



                elif selected:
                    if selected_color == YELLOW and (mouse_pos not in yellow_coords):
                        yellow_coords.append(mouse_pos)
                    elif selected_color == BLUE and (mouse_pos not in blue_coords):
                        blue_coords.append(mouse_pos)
                    

        
        draw()
        pygame.display.update()
        clock.tick(FPS)
        SCREEN.fill(BLACK)
    
    pygame.quit()


# -----------------------------------------------------------------


if __name__ == "__main__":
    main()



