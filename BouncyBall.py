import pygame
import sys
import random

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

ball_colour = (255, 255, 255)
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 0.2
ball_speed_y = 0.2

game_running = True
FPS = 60

clock = pygame.time.Clock() 

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    position = (ball_x, ball_y)
    acceleration = a = (0, 0.1)
    
    time = 1 / FPS

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    ball_speed_x += acceleration[0] * time
    ball_speed_y += acceleration[1] * time

    # Collisions with window edges
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x = -ball_speed_x
        ball_speed_x *= random.uniform(0.9, 1.1)
    
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y = -ball_speed_y
        ball_speed_y *= random.uniform(0.9, 1.1)
    
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, ball_colour, position, ball_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()


clock = pygame.time.Clock()
FPS = 60

while game_running:
    clock.tick(FPS)