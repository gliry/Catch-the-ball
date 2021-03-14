import pygame
from pygame.draw import *
from random import randint, random, choice

pygame.init()

a = 500
b = 500
points = 0
FPS = 30
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
    list_cor = []
    x = randint(100, 400)
    y = randint(100, 400)
    r = randint(30, 50)
    vx = randint(1, 30)
    vy = randint(1, 30)
    rand = [-1, 1]
    dx = random() * choice(rand) * vx
    dy = random() * choice(rand) * vy
    x += dx
    y += dy
    list_cor = list((x, y, r, dx, dy))
    return list_cor


def draw_ball(x, y, r, dx, dy, points):
    color = COLORS[randint(0, 5)]

    not_killed = True
    while not_killed:
        x += dx
        y += dy
        screen.fill(BLACK)
        circle(screen, color, (x, y), r)
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                points, not_killed = click(event, x, y, r, position, points)
        if x + r >= a:
            dx = -dx
        if y + r >= b:
            dy = -dy
        if y - r <= 0:
            dy = -dy
        if x - r <= 0:
            dx = -dx
    return points


def click(event, x, y, r, position, points):
    not_killed = True
    if (position[0] > x - r and position[0] < x + r and position[1] > y - r and position[1] < y + r):
        points += 1
        print(f'Your points {points}')
        not_killed = False

    return points, not_killed


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    new_balls = new_ball()
    x = new_balls[0]
    y = new_balls[1]
    r = new_balls[2]
    dx = new_balls[3]
    dy = new_balls[4]

    points = draw_ball(x, y, r, dx, dy, points)

    pygame.display.update()


    screen.fill(BLACK)

pygame.quit()
