import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Events")

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square_x -= 5
            elif event.key == pygame.K_RIGHT:
                square_x += 5
            elif event.key == pygame.K_UP:
                square_y -= 5
            elif event.key == pygame.K_DOWN:
                square_y += 5

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
