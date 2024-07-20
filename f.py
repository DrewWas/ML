import pygame
from random import uniform

# Setup
pygame.init()
WIDTH, HEIGHT = 1000, 1000
FPS = 120
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perceptron Visualization")

# Colors
BLACK = (0, 0, 0)
BLUE = (12, 31, 255)
GRAY = (123, 123, 123)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 2)
GREEN = (12, 255, 24)

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
    pygame.draw.line(SCREEN, GRAY, (4, HEIGHT), (4, 0), 7)
    pygame.draw.line(SCREEN, GRAY, (0, 996), (WIDTH, 996), 7)

    # Draw buttons
    pygame.draw.rect(SCREEN, WHITE, (840, 10, 150, 110))
    pygame.draw.rect(SCREEN, BLUE, (845, 15, 140, 30))
    pygame.draw.rect(SCREEN, YELLOW, (845, 50, 140, 30))
    pygame.draw.rect(SCREEN, GREEN, (845, 85, 140, 30))

    # Text
    SCREEN.blit(font.render("Add Blue", False, BLACK), (860, 17))
    SCREEN.blit(font.render("Add Yellow", False, BLACK), (850, 52))
    SCREEN.blit(font.render("Start NN", False, BLACK), (860, 87))

    # Points
    for i in blue_coords:
        pygame.draw.circle(SCREEN, BLUE, (i[0], 1000 - i[1]), 8)

    for j in yellow_coords:
        pygame.draw.circle(SCREEN, YELLOW, (j[0], 1000 - j[1]), 8)

# --------------------------------------------------------------------------

def matrix_ify():
    # 1 represents blue
    # 0 represents yellow

    data = []

    for i in blue_coords:
        data.append([1, i[0] / 1000, i[1] / 1000, 1])


    for j in yellow_coords:
        data.append([1, j[0] / 1000, j[1] / 1000, 0])

    return data

# --------------------------------------------------------------------------

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


# --------------------------------------------------------------------------

def predict(inputs, weights):
    total_activation = 0.0
    threshold = 0.0

    for inputt, weight in zip(inputs, weights):
        total_activation += inputt * weight
    
    if total_activation >= threshold:
        return 1.0
    else:
        return 0.0


# --------------------------------------------------------------------------

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

# --------------------------------------------------------------------------

def perceptron():
# 1 represents blue
    # 0 represents yellow

    data = matrix_ify()

    weights = [0.5, 0.3, 0.9]

    new_weights = train_weights(data, weights)  

    print("\nNew Weights: ", new_weights)

    m = new_weights[1] / new_weights[2]
    b = -new_weights[0] / new_weights[2]

    start_point = (0, int(b))
    end_point = (WIDTH, int((m * WIDTH) + b))

    return start_point, end_point


# --------------------------------------------------------------------------

def draw_boundary(start, end):
    pygame.draw.line(SCREEN, GREEN, start, end, 2)
    

# --------------------------------------------------------------------------

def main():
    run = True
    clock = pygame.time.Clock()
    selected = False
    selected_color = None
    start, end = (0,0), (0,0)

    button_areas = [
        (845, 15, 140, 30, BLUE),
        (845, 50, 140, 30, YELLOW),
        (845, 85, 140, 30, GREEN)
    ]

    while run:
        SCREEN.fill(BLACK)
        draw()
        draw_boundary(start, end)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_in_box = (845 < mouse_pos[0] < 985 and 15 < mouse_pos[1] < 115)

            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_in_box:
                    for x, y, w, h, color in button_areas:
                        if x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h:
                            selected = True
                            selected_color = color
                            break

                    if selected_color == GREEN:
                        print("START THE PERCEPTRON")
                        start, end = perceptron()

                elif selected:
                    if selected_color == YELLOW and (mouse_pos not in yellow_coords):
                        yellow_coords.append((mouse_pos[0], 1000 - mouse_pos[1]))

                    elif selected_color == BLUE and (mouse_pos not in blue_coords):
                        blue_coords.append((mouse_pos[0], 1000 - mouse_pos[1]))



        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()




if __name__ == "__main__":
    main()

