import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Food settings
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# Game settings
clock = pygame.time.Clock()
speed = 15

def change_dir(to):
    global direction
    if to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

def move_snake():
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        return True
    snake_body.pop()
    return False

def check_collision():
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        return True
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        return True
    for block in snake_body[1:]:
        if snake_pos == block:
            return True
    return False

def show_score(choice=1):
    s_font = pygame.font.SysFont('comicsans', 35)
    s_surf = s_font.render('Score : ' + str(len(snake_body) - 3), True, black)
    s_rect = s_surf.get_rect()
    if choice == 1:
        s_rect.midtop = (80, 10)
    else:
        s_rect.midtop = (width / 2, height / 4)
    screen.blit(s_surf, s_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    change_dir(change_to)
    if move_snake():
        food_spawn = False
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    screen.fill((255, 255, 255))
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if check_collision():
        show_score(0)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    show_score()
    pygame.display.flip()
    clock.tick(speed)
