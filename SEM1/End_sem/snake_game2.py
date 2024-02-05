
import pygame
import time
import random

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Initialize snake
snake_list = []
snake_length = 1

# Initialize snake position and movement
snake_head = [width / 2, height / 2]
snake_direction = 'RIGHT'
change_to = snake_direction
speed = 15

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Update snake direction
    if change_to == 'UP' and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    # Update snake position
    if snake_direction == 'UP':
        snake_head[1] -= snake_block
    if snake_direction == 'DOWN':
        snake_head[1] += snake_block
    if snake_direction == 'LEFT':
        snake_head[0] -= snake_block
    if snake_direction == 'RIGHT':
        snake_head[0] += snake_block

    # Game over if snake hits the boundaries
    if (
        snake_head[0] >= width
        or snake_head[0] < 0
        or snake_head[1] >= height
        or snake_head[1] < 0
    ):
        game_over = True

    # Game over if snake collides with itself
    for segment in snake_list:
        if segment == snake_head:
            game_over = True

    # Update snake length
    snake_list.append(list(snake_head))
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Draw the snake
    window.fill(black)
    our_snake(snake_block, snake_list)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
