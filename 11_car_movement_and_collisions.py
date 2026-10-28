"""
Python Lesson 11: Car Movement and Collision

This lesson combines movement, boundaries, and collision detection.
We will create a simple car object moving around the screen.
"""

import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Movement Demo")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (90, 140, 255)
RED = (255, 80, 80)

# Player car settings
player_x = 200
player_y = 500
player_w = 60
player_h = 100
player_speed = 5

# Obstacle car
obstacle_x = 600
obstacle_y = 200
obstacle_w = 60
obstacle_h = 100

running = True
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

    # Keep car inside screen
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_w))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - player_h))

    # Collision detection using rectangles
    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_w, obstacle_h)

    if player_rect.colliderect(obstacle_rect):
        print("Crash detected!")

    screen.fill(BLACK)

    # Draw road strip
    pygame.draw.rect(screen, (30, 33, 40), (140, 0, 620, SCREEN_HEIGHT))
    pygame.draw.line(screen, WHITE, (140 + 206, 0), (140 + 206, SCREEN_HEIGHT), 3)
    pygame.draw.line(screen, WHITE, (140 + 412, 0), (140 + 412, SCREEN_HEIGHT), 3)

    # Draw player car
    pygame.draw.rect(screen, BLUE, player_rect, border_radius=10)

    # Draw obstacle car
    pygame.draw.rect(screen, RED, obstacle_rect, border_radius=10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - basic car movement
# - screen bounds
# - collision detection using rectangles
# - how movement and collisions are combined in games
# ------------------------------------------------------
