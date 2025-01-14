import pygame

# Constants
WIDTH, HEIGHT = 1000, 1000
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLUE = (0, 138, 255)
RED = (255, 34, 86)
BLACK = (0, 0, 0)
GREEN = (12, 255, 35)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), display=1)
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('futura', 30)
FONT_SMALL = pygame.font.SysFont('futura', 18)

data_matrix = []
weight_vector = [0.5, 0.5, 0.5]

def main():
    run = True
    data_type_selected = BLACK 
    boundaries = [(0, 0), (0, 0)]

    while run:
        for event in pygame.event.get():

            WINDOW.fill(BLACK)

            real_pos = pygame.mouse.get_pos()

            x_pos = pygame.mouse.get_pos()[0] 
            y_pos = pygame.mouse.get_pos()[1] 

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if real_pos[0] > 20 and real_pos[0] < 190 and real_pos[1] > 15 and real_pos[1] < 50:   
                    data_type_selected = BLUE 

                if real_pos[0] > 20 and real_pos[0] < 190 and real_pos[1] > 55 and real_pos[1] < 90:   
                    data_type_selected = RED 

                if real_pos[0] > 20 and real_pos[0] < 190 and real_pos[1] > 95 and real_pos[1] < 130:   
                    data_type_selected = BLACK 
                    boundaries = train_weights()
                    pygame.draw.line(WINDOW, GREEN, boundaries[0], boundaries[1], 5) 

                if real_pos[0] > 20 and real_pos[0] < 190 and real_pos[1] > 135 and real_pos[1] < 170:   
                    data_matrix.clear()
                    weight_vector = [0.5, 0.5, 0.5]

                elif data_type_selected == RED and (real_pos[0] > 200 or real_pos[1] > 140):
                    # RED = 0 for data purposes
                    data_matrix.append([1, x_pos, y_pos, 0])

                elif data_type_selected == BLUE and (real_pos[0] > 200 or real_pos[1] > 140):
                    # BLUE =  1 for data purposes
                    data_matrix.append([1, x_pos, y_pos, 1])



            draw_grid_lines()

            # Unfortunately we have to redraw because otherwise the mouse would just paint over the entire screen
            for point in data_matrix:
                if point[3] == 0:
                    pygame.draw.circle(WINDOW, RED, (point[1], point[2]), 10)
                elif point[3] == 1:
                    pygame.draw.circle(WINDOW, BLUE, (point[1], point[2]), 10) 


            pygame.draw.line(WINDOW, GREEN, boundaries[0], boundaries[1], 5) 
            pygame.draw.circle(WINDOW, data_type_selected, (x_pos, y_pos), 10) 
            draw_color_select(x_pos, y_pos)
            pygame.display.update()            
    


    pygame.quit()


def draw_grid_lines():
    for i in range(40):
        for j in range(40):
            pygame.draw.line(WINDOW, GRAY, (i * 25, 0), (i * 25, 1000)) 
            pygame.draw.line(WINDOW, GRAY, (0, i * 25), (1000, i * 25)) 

    #pygame.draw.line(WINDOW, GRAY, (WIDTH // 2, 0), (WIDTH // 2, 1000), 5) 
    #pygame.draw.line(WINDOW, GRAY, (0, HEIGHT // 2), (1000, HEIGHT // 2), 5) 


def draw_color_select(x_pos, y_pos):
    # SELECTION DISPLAY
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(10, 10, 190, 165))

    pygame.draw.rect(WINDOW, BLUE, pygame.Rect(20, 15, 170, 33))
    WINDOW.blit(FONT.render("Blue Data", False, BLACK), (40, 10))
    pygame.draw.rect(WINDOW, RED, pygame.Rect(20, 55, 170, 33))
    WINDOW.blit(FONT.render("Red Data", False, BLACK), (45, 50))

    pygame.draw.rect(WINDOW, GREEN, pygame.Rect(20, 95, 170, 33), 3)
    WINDOW.blit(FONT.render("START", False, BLACK), (60, 92))

    pygame.draw.rect(WINDOW, RED, pygame.Rect(20, 135, 170, 33), 3)
    WINDOW.blit(FONT.render("RESET", False, BLACK), (60, 132))


    # COORDINATE DISPLAY
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(850, 10, 140, 30))
    WINDOW.blit(FONT_SMALL.render("X: " + str(x_pos) + "    Y: " + str(y_pos), False, BLACK), (853, 15))



def train_weights():
    learning_rate = 0.5
    epochs = 1000
    w0, w1, w2 = weight_vector

    for epoch in range(epochs):
        curr_acc = accuracy()

        print("\nEpoch: ", epoch, "\nWeights: ", weight_vector)
        print("\nAccuracy: ", curr_acc)

        # Also here add redrawing the line? pygame.display.line(...)

        if curr_acc == 1:
            break


        for i in data_matrix:
            prediction = perceptron(i[:-1], weight_vector) 
            error = i[-1] - prediction


            for j in range(len(weight_vector)):
                weight_vector[j] += learning_rate * error * i[j] 
              

    # Something like this, y-int (bias) is not being taken into account really
    return (-1000, -((-1000 * w1) + w0) / w2), (1000, -((1000 * w1) + w0) / w2)



def perceptron(inputs, weights):
    threshold = 0
    current_activation = 0

    for i, w in zip(inputs, weights):
        current_activation += i * w

    if current_activation >= threshold:
        return 1
    else:
        return 0


def accuracy():
    num_correct = 0

    for i in data_matrix:
        prediction = perceptron(i[:-1], weight_vector)
        if prediction == i[-1]:
            num_correct += 1

    return num_correct / float(len(data_matrix))




# HASHTAG NO OOP LOL
main()






