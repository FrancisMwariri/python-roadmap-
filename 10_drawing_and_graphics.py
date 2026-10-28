"""
Python Lesson 10: Drawing and Graphics

This lesson teaches how to draw game objects on the screen.
We will use:
- lines
- rectangles
- circles
- polygons
- text
- colors
"""

import pygame

pygame.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing Demo")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 80, 80)
BLUE = (90, 140, 255)
GREEN = (90, 220, 120)
YELLOW = (255, 220, 110)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(BLACK)

    # Draw a road-like rectangle
    pygame.draw.rect(screen, (30, 33, 40), (200, 50, 560, 620))

    # Draw lane lines
    for lane in range(1, 3):
        x = 200 + lane * 180
        pygame.draw.line(screen, (120, 120, 120), (x, 50), (x, 670), 3)

    # Draw dashed road markings
    for y in range(50, 670, 40):
        pygame.draw.rect(screen, WHITE, (468, y, 6, 20), border_radius=2)

    # Draw a car body
    car_x = 430
    car_y = 560
    car_w = 80
    car_h = 110
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_w, car_h), border_radius=10)

    # Draw windows
    pygame.draw.rect(screen, (160, 210, 255), (car_x + 15, car_y + 15, car_w - 30, 40), border_radius=6)

    # Draw wheels
    pygame.draw.rect(screen, BLACK, (car_x + 12, car_y + 12, 15, 25), border_radius=3)
    pygame.draw.rect(screen, BLACK, (car_x + car_w - 27, car_y + 12, 15, 25), border_radius=3)
    pygame.draw.rect(screen, BLACK, (car_x + 12, car_y + car_h - 37, 15, 25), border_radius=3)
    pygame.draw.rect(screen, BLACK, (car_x + car_w - 27, car_y + car_h - 37, 15, 25), border_radius=3)

    # Draw circles and text
    pygame.draw.circle(screen, RED, (150, 150), 40)
    pygame.draw.circle(screen, GREEN, (800, 150), 30)

    font = pygame.font.SysFont(None, 36)
    label = font.render("Morning Pursuit", True, YELLOW)
    screen.blit(label, (320, 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how to draw rectangles, lines, circles, and text
# - how to build a road scene
# - how to create visual game elements
# - why drawing is separated from game logic
# ------------------------------------------------------
