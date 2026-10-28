"""
Python Lesson 12: Game States

Game states are the different phases a game can be in.
Examples:
- menu
- playing
- paused
- game over
- restart

This is a very important concept for real games.
"""

import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game States Demo")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (90, 140, 255)
RED = (255, 80, 80)
YELLOW = (255, 220, 120)

# State variables
state = "menu"
score = 0
lives = 3

font = pygame.font.SysFont(None, 48)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == "menu":
                    state = "playing"
                elif state == "game_over":
                    state = "menu"
                    score = 0
                    lives = 3

    keys = pygame.key.get_pressed()

    if state == "menu":
        screen.fill(BLACK)
        label = font.render("Press SPACE to Start", True, YELLOW)
        screen.blit(label, (250, 300))

    elif state == "playing":
        if keys[pygame.K_LEFT]:
            score += 1
        if keys[pygame.K_RIGHT]:
            score += 1

        if score >= 200:
            state = "game_over"

        screen.fill(BLACK)
        label = font.render(f"Playing... Score: {score}", True, WHITE)
        screen.blit(label, (250, 300))

    elif state == "game_over":
        screen.fill(BLACK)
        label = font.render("Game Over! Press SPACE to restart", True, RED)
        screen.blit(label, (170, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how a game can exist in different states
# - how user input moves the game between states
# - how a menu and game over state works
# ------------------------------------------------------
