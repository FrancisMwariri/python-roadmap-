"""
Python Lesson 9: Game Loop and Input

This lesson makes the game feel more interactive.
We will learn how to:
- handle keyboard input
- update positions each frame
- use a clock and FPS
- separate update and draw steps
"""

import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Loop Demo")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (60, 220, 120)
RED = (255, 80, 80)

# Game state
player_x = 200
player_y = 500
player_w = 50
player_h = 50
player_speed = 6
jump_force = 0

# Example target
target_x = 700
target_y = 250
target_w = 40
target_h = 40

running = True
while running:
    # 1) Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2) Read keyboard input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep the player inside the screen
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_w))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - player_h))

    # A simple collision example
    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    target_rect = pygame.Rect(target_x, target_y, target_w, target_h)

    if player_rect.colliderect(target_rect):
        print("Collision detected!")

    # 3) Drawing stage
    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, player_rect)
    pygame.draw.rect(screen, RED, target_rect)

    # 4) Refresh screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how input is processed in a loop
# - update and draw stages
# - collision detection with rectangles
# - how the game stays smooth with FPS control
# ------------------------------------------------------
