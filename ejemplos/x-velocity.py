import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Text")

# Set up the font
font = pygame.font.SysFont(None, 36)
text = font.render("Bouncing Text", True, (0, 0, 255))
text_rect = text.get_rect()

# Set initial position and velocity
text_rect.centerx = WIDTH // 2
text_rect.centery = HEIGHT // 2
velocity_x = 100  # pixels per second
velocity_y = 100  # pixels per second

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate time elapsed since the last frame
    dt = clock.tick(30) / 1000.0  # Convert milliseconds to seconds

    # Move the text based on velocity and time elapsed
    text_rect.x += velocity_x * dt
    text_rect.y += velocity_y * dt

    # Bounce off the walls
    if text_rect.left < 0 or text_rect.right > WIDTH:
        velocity_x = -velocity_x
    if text_rect.top < 0 or text_rect.bottom > HEIGHT:
        velocity_y = -velocity_y

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white

    # Draw the text
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
