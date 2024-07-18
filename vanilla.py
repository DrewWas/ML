import pygame

# Setup
pygame.init()
WIDTH, HEIGHT = 1400, 800
FPS = 120
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vanilla NN Visualization")

# Colors
BLACK = (0,0,0)
BLUE = (12,31,255)
RED = (255,31,21)
GRAY = (123,123,123,)

# Coordinates 
red_coords = []
blue_coords= []


def draw_grid():
    # Main grid lines
    for i in range(int(WIDTH / 35)):
        pygame.draw.line(SCREEN, GRAY, (i * 40, HEIGHT), (i * 40, 0), 1)

    for j in range(int(WIDTH / 35)):
        pygame.draw.line(SCREEN, GRAY, (0, j * 40), (WIDTH, j * 40), 1)

    # Thick coordinate lines 
    pygame.draw.line(SCREEN, GRAY, (720, HEIGHT), (720, 0), 5)
    pygame.draw.line(SCREEN, GRAY, (0, 403), (WIDTH, 403), 5)

def main():

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        draw_grid()
        pygame.display.update()

        clock.tick(FPS)
        SCREEN.fill(BLACK)


    pygame.quit()


if __name__ == "__main__":
    main()
