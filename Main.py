import pygame
from pygame.draw import *
from random import randint
pygame.init()

a = 500
b = 500
points = 0
FPS = 1
x = 0
y = 0
r = 0
screen = pygame.display.set_mode((a, b))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    list_cor =[]
    x = randint(100,400)
    y = randint(100,400)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    list_cor = list((x, y, r))
    return list_cor

def click(event, x, y, r, position, points):

    print(x, y, r)
    print(position)

    if (position[0] > x - r and position[0] < x + r and position[1] > y - r and position[1] < y + r):
        points = points + 1
        print(f'Your points: {points}')
    return points

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    list_cor = new_ball()
    x = list_cor[0]
    y = list_cor[1]
    r = list_cor[2]

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            points = click(event, x, y, r, position, points)



    screen.fill(BLACK)

pygame.quit()