import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Events 2")

FPS = 30
square_x, square_y = WIDTH // 2, HEIGHT // 2
square_size = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

move_x, move_y = 0, 0

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -5
            elif event.key == pygame.K_RIGHT:
                move_x = 5
            elif event.key == pygame.K_UP:
                move_y = -5
            elif event.key == pygame.K_DOWN:
                move_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                move_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                move_y = 0

    # Update square position
    square_x += move_x
    square_y += move_y

    clock.tick(FPS)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the square
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
