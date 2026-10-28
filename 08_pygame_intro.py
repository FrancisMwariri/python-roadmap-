"""
Python Lesson 8: Pygame Intro

Pygame is a Python library for making games.
It gives us tools for:
- creating a window
- drawing shapes
- handling keyboard input
- updating frames
- making animations

In the repo, Pygame is used to create the game window and draw all the visuals.
"""

import pygame

# ------------------------------------------------------
# 1) Initialize Pygame
# ------------------------------------------------------
pygame.init()

# ------------------------------------------------------
# 2) Create a window
# ------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# ------------------------------------------------------
# 3) Game loop setup
# ------------------------------------------------------
clock = pygame.time.Clock()
running = True

# ------------------------------------------------------
# 4) Colors
# ------------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
RED = (255, 70, 70)

# ------------------------------------------------------
# 5) Player rectangle position
# ------------------------------------------------------
player_x = 100
player_y = 100
player_width = 60
player_height = 60
player_speed = 5

# ------------------------------------------------------
# 6) Main loop
# ------------------------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep player inside the screen
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_width))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - player_height))

    # --------------------------------------------------
    # 7) Drawing
    # --------------------------------------------------
    screen.fill(BLACK)

    # Draw a blue player rectangle
    pygame.draw.rect(
        screen,
        BLUE,
        (player_x, player_y, player_width, player_height),
    )

    # Draw a red obstacle
    pygame.draw.rect(screen, RED, (500, 200, 80, 80))

    pygame.display.flip()
    clock.tick(60)

# ------------------------------------------------------
# 8) Quit
# ------------------------------------------------------
pygame.quit()

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how to create a Pygame window
# - a main game loop
# - keyboard input
# - drawing rectangles
# - updating the screen
# ------------------------------------------------------
