import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game loop")

FPS = 30
square_x, square_y = WIDTH // 2, HEIGHT // 2
square_size = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(FPS)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the square
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    square_x += 1

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
