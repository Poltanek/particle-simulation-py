import pygame
import numpy as np
import sys
from math import *

WINDOW_SIZE =  800
ROTATE_SPEED = 0.05
window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
pygame.display.set_caption("Press A, D, W, S, Q, E to rotate, R to reset, move mouse to change scale")
clock = pygame.time.Clock()


projection_matrix = [[1,0,0],
                     [0,1,0],
                     [0,0,0]]

cube_points = [n for n in range(8)]
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1],[-1],[1]]
cube_points[2] = [[1],[1],[1]]
cube_points[3] = [[-1],[1],[1]]
cube_points[4] = [[-1],[-1],[-1]]
cube_points[5] = [[1],[-1],[-1]]
cube_points[6] = [[1],[1],[-1]]
cube_points[7] = [[-1],[1],[-1]]

def multiply_m(a, b):
    result = [[0 for col in range(len(b[0]))] for row in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [9, 10], [11, 12]]

result = multiply_m(a, b)

def connect_points(i, j, points):
    pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]) , (points[j][0], points[j][1]))

# Main Loop
scale = 100
angle_x = angle_y = angle_z = 0
pygame.mouse.set_visible(True)
pygame.event.set_grab(True)
is_dragging = False


while True:
    clock.tick(60)
    window.fill((0,0,0))

    # Mouse Feature
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_dragging = True
            pygame.event.set_grab(True)
        if event.type == pygame.MOUSEBUTTONUP:
            is_dragging = False
            pygame.event.set_grab(False)

    if is_dragging:
        dx, dy = pygame.mouse.get_rel()
        angle_x += dy * 0.01
        angle_y -= dx * 0.01
    else:
        pygame.mouse.get_rel()

    rotation_x = [[1, 0, 0],
                    [0, cos(angle_x), -sin(angle_x)],
                    [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                    [0, 1, 0],
                    [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                    [sin(angle_z), cos(angle_z), 0],
                    [0, 0, 1]]

    points = [0 for _ in range(len(cube_points))]
    i = 0
    for point in cube_points:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(projection_matrix, rotate_z)
    
        x = (point_2d[0][0] * scale) + WINDOW_SIZE/2
        y = (point_2d[1][0] * scale) + WINDOW_SIZE/2

        points[i] = (x,y)
        i += 1
        pygame.draw.circle(window, (255, 0, 0), (x, y), 5)

    # Connect the points to make a cube
    connect_points(0, 1, points)
    connect_points(0, 3, points)
    connect_points(0, 4, points)
    connect_points(1, 2, points)
    connect_points(1, 5, points)
    connect_points(2, 6, points)
    connect_points(2, 3, points)
    connect_points(3, 7, points)
    connect_points(4, 5, points)
    connect_points(4, 7, points)
    connect_points(6, 5, points)
    connect_points(6, 7, points)
          
    pygame.display.update()
