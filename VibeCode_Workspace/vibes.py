import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Top-Down Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load grass background
grass = pygame.image.load("grass.png")  # Ensure you have a "grass.png" file in the same directory
grass = pygame.transform.scale(grass, (800, 600))  # Scale the grass image to match the screen size

# Player attributes
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Background offset
bg_x = 0
bg_y = 0

# Fullscreen toggle flag
fullscreen = False

# Game loop flag
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Press 'F' to toggle fullscreen
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move background based on arrow keys (opposite direction of player movement)
    if keys[pygame.K_UP]:
        bg_y += player_speed
    if keys[pygame.K_DOWN]:
        bg_y -= player_speed
    if keys[pygame.K_LEFT]:
        bg_x += player_speed
    if keys[pygame.K_RIGHT]:
        bg_x -= player_speed

    # Clear screen
    screen.fill(WHITE)

    # Draw the grass background infinitely by tiling it
    for x in range(-800, 1600, 800):  # Adjust range to cover the screen and allow for scrolling
        for y in range(-600, 1200, 600):
            screen.blit(grass, (bg_x % 800 + x, bg_y % 600 + y))

    # Draw player (always at the center of the screen)
    pygame.draw.rect(screen, BLUE, (player_x - player_size // 2, player_y - player_size // 2, player_size, player_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()