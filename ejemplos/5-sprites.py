import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites")

FPS = 30
sprite_x, sprite_y = WIDTH // 2, HEIGHT // 2
square_size = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

move_x, move_y = 0, 0

# Load sprite images
sprite_folder = "../sprites/mario"  # Folder containing sprite images
sprites = []
for i in range(1, 9):
    sprite_path = os.path.join(sprite_folder, f"mario_{i}.png")
    sprite = pygame.image.load(sprite_path)
    sprites.append(sprite)

# Load the still sprite
sprite_still = pygame.image.load("../sprites/mario/mario_quieto.png")

# Set up variables for animation
frame_count = 8  # Number of frames in the sprite sheet
current_frame = 0
frame_duration = 100  # Duration of each frame in milliseconds
last_frame_update = pygame.time.get_ticks()

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
    sprite_x += move_x
    sprite_y += move_y

    clock.tick(FPS)

    # Calculate time elapsed since the last frame
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_frame_update

    # Update frame if it's time to do so
    if elapsed_time >= frame_duration:
        current_frame = (current_frame + 1) % frame_count
        last_frame_update = current_time

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white

    # Check if the sprite is walking
    walking = move_x != 0 or move_y != 0

    # Draw the current frame
    if walking:
        screen.blit(sprites[current_frame], (sprite_x, sprite_y))
    else:
        screen.blit(sprite_still, (sprite_x, sprite_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)


# Quit Pygame
pygame.quit()
sys.exit()
