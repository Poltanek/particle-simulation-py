import pygame
import sys
import random


pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")




# ball properties
ball_colour = (255, 255, 255)
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 1
ball_speed_y = 1


# Main Game loop

gamerunning = True
while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False

    ball_x += ball_speed_x
    ball_y += ball_speed_y


    # Collisions with window edges
    # Check for collisions with the window edges
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x = -ball_speed_x
        ball_speed_x *= random.uniform(0.9, 1.1)  # Slightly randomize speed
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y = -ball_speed_y
        ball_speed_y *= random.uniform(0.9, 1.1)  # Slightly randomize speed
    

    screen.fill("Black")

    pygame.draw.circle(screen, ball_colour, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()
