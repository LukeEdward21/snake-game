#!/usr/bin/env python3
import pygame
from pygame.locals import *
from random import randint


# Screen size
GRID_WIDTH = 600
GRID_HEIGHT = 600

# align food function
def position_generator():
    x = (randint(0, GRID_WIDTH))
    y = (randint(0, GRID_HEIGHT))
    return (x//10 * 10, y//10 * 10)

# screen edge function
def new_coords(x, y):
    return (x % GRID_WIDTH, y % GRID_HEIGHT)

# collision function
def collision(p1, p2):
    return (p1[0] == p2[0]) and (p1[1] == p2[1])

# Window
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
pygame.display.set_caption('Snake')

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Snake
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))
# default direction
direction = LEFT

# food
food_position = position_generator()
food = pygame.Surface((10, 10))
food.fill((255, 0, 0))

# fps
clock = pygame.time.Clock()

while True:
    # 10 fps
    clock.tick(10)
    # enable close window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # snake controls
        if event.type == KEYDOWN:
            if event.key == K_w:
                if direction != DOWN:
                    direction = UP

            if event.key == K_s:
                if direction != UP:
                    direction = DOWN
            
            if event.key == K_a:
                if direction != RIGHT:
                    direction = LEFT
            if event.key == K_d:
                if direction != LEFT:
                    direction = RIGHT
    
    # snake move
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if direction == UP:
        snake[0] = new_coords(snake[0][0], snake[0][1] - 10)

    if direction == RIGHT:
        snake[0] = new_coords(snake[0][0] + 10, snake[0][1])

    if direction == DOWN:
        snake[0] = new_coords(snake[0][0], snake[0][1] + 10)

    if direction == LEFT:
        snake[0] = new_coords(snake[0][0] - 10, snake[0][1])
    
    

    # screen color
    screen.fill((0,0,0))

    # draw snake
    for position in snake:
        screen.blit(snake_skin, position)

    # draw food
    screen.blit(food, food_position)

    # hit food
    if collision(snake[0], food_position):
        food_position = position_generator()
        snake.append((0,0))
    
    # hit itself
    for i in snake[1:]:
        if collision(snake[0], i):
            pygame.quit()
    
    # update screen
    pygame.display.update()
